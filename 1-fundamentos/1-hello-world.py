# ========================================
# HELLO WORLD COM LANGCHAIN E OPENAI
# ========================================
# Este é o primeiro exemplo do curso, demonstrando como fazer uma
# integração básica entre LangChain e OpenAI para gerar respostas
# usando modelos de linguagem.
# ========================================

# Importa a classe ChatOpenAI do LangChain
# Esta classe permite interagir com os modelos da OpenAI (GPT-3.5, GPT-4, etc.)
from langchain_openai import ChatOpenAI

# Importa a função load_dotenv para carregar variáveis de ambiente
# Isso permite carregar a chave da API da OpenAI do arquivo .env
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
# Isso torna disponível a variável OPENAI_API_KEY para o LangChain
load_dotenv()

# Cria uma instância do modelo de linguagem
# - model="gpt-5-nano": Especifica qual modelo da OpenAI usar
# - temperature=0.5: Controla a criatividade das respostas (0 = mais determinístico, 1 = mais criativo)
model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

# Envia uma mensagem para o modelo e recebe a resposta
# O método invoke() é usado para fazer uma chamada única ao modelo
message = model.invoke("Olá Mundo!")

# Exibe o conteúdo da resposta do modelo
# message.content contém o texto gerado pela IA
print(message.content)