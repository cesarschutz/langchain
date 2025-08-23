# ========================================
# ARMAZENAMENTO DE HISTÓRICO - MEMÓRIA DE CONVERSA
# ========================================
# Este exemplo demonstra como implementar memória de conversa usando
# InMemoryChatMessageHistory e RunnableWithMessageHistory para manter
# o contexto entre múltiplas interações com o modelo.
# ========================================

# Importações já explicadas nos scripts anteriores
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# Importa InMemoryChatMessageHistory para armazenar histórico em memória
from langchain_core.chat_history import InMemoryChatMessageHistory
# Importa RunnableWithMessageHistory para adicionar memória às chains
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

# ===== CONFIGURAÇÃO DO PROMPT COM HISTÓRICO =====

# Cria um prompt template que inclui histórico de mensagens
# MessagesPlaceholder: Reserva espaço para inserir mensagens do histórico
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),  # Placeholder para histórico
    ("human", "{input}"),  # Mensagem atual do usuário
])

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
chat_model = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

# Cria a chain básica já explicada no script 2-chains-e-processamento/1-iniciando-com-chains.py
chain = prompt | chat_model

# ===== GERENCIAMENTO DE SESSÕES E HISTÓRICO =====

# Dicionário para armazenar histórico de diferentes sessões
# Cada session_id tem seu próprio histórico de mensagens
session_store: dict[str, InMemoryChatMessageHistory] = {}

# Função para obter ou criar histórico de uma sessão
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        # Cria novo histórico se a sessão não existir
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

# ===== CHAIN COM MEMÓRIA =====

# Cria uma chain que mantém histórico de mensagens
# RunnableWithMessageHistory: Adiciona capacidade de memória à chain
conversational_chain = RunnableWithMessageHistory(
    chain,  # Chain base (prompt + modelo)
    get_session_history,  # Função para obter histórico da sessão
    input_messages_key="input",  # Chave para mensagem de entrada
    history_messages_key="history",  # Chave para histórico no prompt
)

# Configuração da sessão
# session_id: Identifica unicamente uma conversa
config = {"configurable": {"session_id": "demo-session"}}

# ===== TESTANDO A MEMÓRIA =====

# Primeira interação: Usuário se apresenta
response1 = conversational_chain.invoke({"input": "Hello, my name is Wesley. how are you?"}, config=config)
print("Assistant: ", response1.content)
print("-"*30)

# Segunda interação: Testa se o modelo lembra do nome
response2 = conversational_chain.invoke({"input": "Can you repeat my name?"}, config=config)
print("Assistant: ", response2.content)
print("-"*30)

# Terceira interação: Usa o nome em contexto diferente
response3 = conversational_chain.invoke({"input": "Can you repeat my name in a motivation phrase?"}, config=config)
print("Assistant: ", response3.content)
print("-"*30)
