# ========================================
# CHAT PROMPT TEMPLATE COM LANGCHAIN
# ========================================
# Este exemplo demonstra como criar templates de prompt estruturados
# para conversas com IA usando ChatPromptTemplate. Diferente do PromptTemplate
# simples, este permite criar prompts com múltiplas mensagens (system, user, etc.)
# ========================================

# Importa ChatPromptTemplate para criar prompts estruturados de conversa
from langchain.prompts import ChatPromptTemplate
# Importações já explicadas nos scripts anteriores
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Define mensagens do sistema e do usuário como tuplas
# - ("system", "...") : Define o papel/comportamento da IA
# - ("user", "...") : Define a pergunta/entrada do usuário
system = ("system", "you are an assistant that answers questions in a {style} style")
user = ("user", "{question}")

# Cria o template de chat combinando as mensagens
# ChatPromptTemplate aceita uma lista de mensagens estruturadas
chat_prompt = ChatPromptTemplate([system, user])

# Formata as mensagens substituindo as variáveis
# - style="funny": Define o estilo de resposta
# - question="Who is Alan Turing?": Define a pergunta
messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

# Exibe cada mensagem formatada para ver a estrutura
# msg.type mostra o tipo (system, user) e msg.content o texto
for msg in messages:
    print(f"{msg.type}: {msg.content}")

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

# Envia as mensagens estruturadas para o modelo
# invoke() já explicado no script 1-fundamentos/1-hello-world.py
result = model.invoke(messages)

# Exibe a resposta do modelo
print(result.content)


