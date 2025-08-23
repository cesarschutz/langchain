# ========================================
# INICIANDO COM CHAINS - LCEL (LangChain Expression Language)
# ========================================
# Este exemplo demonstra como criar chains usando o operador pipe (|)
# do LCEL. Chains permitem conectar diferentes componentes do LangChain
# em um pipeline sequencial de processamento.
# ========================================

# Importações já explicadas nos scripts anteriores
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Cria um template de prompt já explicado no script 1-fundamentos/3-prompt-template.py
question_template = PromptTemplate(
    input_variables=["name"],
    template="Ola, eu sou o  {name}! conteme uma piada!"
)

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

# Cria uma chain conectando o template ao modelo usando o operador pipe (|)
# O operador | conecta componentes em sequência: template -> modelo
chain = question_template | model

# Invoca a chain passando as variáveis como dicionário
# A chain executa: template.format() -> model.invoke()
result = chain.invoke({"name": "Wesley"})

# Exibe o resultado já explicado no script 1-fundamentos/1-hello-world.py
print(result.content)