# ========================================
# HISTÓRICO BASEADO EM SLIDING WINDOW - CONTROLE DE TOKENS
# ========================================
# Este exemplo demonstra como implementar um sistema de memória que
# controla automaticamente o tamanho do histórico usando "sliding window",
# mantendo apenas as mensagens mais recentes dentro de um limite de tokens.
# ========================================

# Importações já explicadas nos scripts anteriores
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
# Importa trim_messages para controlar tamanho do histórico
from langchain_core.messages import trim_messages
# Importa RunnableLambda já explicado no script 2-chains-e-processamento/3-runnable-lambda.py
from langchain_core.runnables import RunnableLambda

load_dotenv()

# ===== CONFIGURAÇÃO DO PROMPT =====
# Prompt já explicado no script 4-gerenciamento-de-memoria/1-armazenamento-de-historico.py
prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful assistant that answers with a short joke when possible."),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])

# ===== CONFIGURAÇÃO DO MODELO =====
# Modelo já explicado no script 1-fundamentos/1-hello-world.py
llm = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

# ===== FUNÇÃO DE PREPARAÇÃO COM SLIDING WINDOW =====
# Função que controla o tamanho do histórico usando trim_messages
def prepare_inputs(payload: dict) -> dict:
    # Obtém o histórico bruto (todas as mensagens)
    raw_history = payload.get("raw_history", [])
    
    # Aplica sliding window: mantém apenas as mensagens mais recentes
    # trim_messages: Reduz o histórico para caber no limite de tokens
    trimmed = trim_messages(
        raw_history,  # Histórico completo
        token_counter=len,  # Função para contar tokens (neste caso, conta caracteres)
        max_tokens=2,  # Limite máximo de tokens (muito baixo para demonstração)
        strategy="last",  # Estratégia: manter as últimas mensagens
        start_on="human",  # Começar a contar a partir de mensagens humanas
        include_system=True,  # Incluir mensagem do sistema
        allow_partial=False,  # Não permitir mensagens cortadas
    )
    
    # Retorna payload com histórico reduzido
    return {"input": payload.get("input",""), "history": trimmed}

# ===== CHAIN COM CONTROLE DE HISTÓRICO =====
# RunnableLambda já explicado no script 2-chains-e-processamento/3-runnable-lambda.py
prepare = RunnableLambda(prepare_inputs)
# Chain já explicada no script 2-chains-e-processamento/1-iniciando-com-chains.py
chain = prepare | prompt | llm

# ===== GERENCIAMENTO DE SESSÕES =====
# session_store já explicado no script 4-gerenciamento-de-memoria/1-armazenamento-de-historico.py
session_store: dict[str, InMemoryChatMessageHistory] = {}

# get_session_history já explicado no script 4-gerenciamento-de-memoria/1-armazenamento-de-historico.py
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

# ===== CHAIN COM MEMÓRIA E SLIDING WINDOW =====
# RunnableWithMessageHistory já explicado no script 4-gerenciamento-de-memoria/1-armazenamento-de-historico.py
conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    # raw_history: Chave para histórico bruto (antes do trim)
    history_messages_key="raw_history"
)

# ===== CONFIGURAÇÃO DA SESSÃO =====
# config já explicado no script 4-gerenciamento-de-memoria/1-armazenamento-de-historico.py
config = {"configurable": {"session_id": "demo-session"}}

# ===== TESTANDO O SLIDING WINDOW =====

# Primeira interação: Usuário se apresenta
resp1 = conversational_chain.invoke({"input": "My name is Wesley. Reply only with 'OK' and do not mention my name."}, config=config)
print("Assistant:", resp1.content)

# Segunda interação: Pede fato divertido
resp2 = conversational_chain.invoke({"input": "Tell me a one-sentence fun fact. Do not mention my name."}, config=config)
print("Assistant:", resp2.content)

# Terceira interação: Testa se o modelo lembra do nome (deve ter esquecido devido ao sliding window)
resp3 = conversational_chain.invoke({"input": "What is my name?"}, config=config)
print("Assistant:", resp3.content)

