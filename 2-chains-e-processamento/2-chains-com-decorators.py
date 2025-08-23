# ========================================
# CHAINS COM DECORATORS - FUNÇÕES PERSONALIZADAS
# ========================================
# Este exemplo demonstra como criar funções personalizadas usando
# o decorador @chain e integrá-las em pipelines de processamento.
# Permite adicionar lógica customizada entre os componentes do LangChain.
# ========================================

# Importações já explicadas nos scripts anteriores
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# Importa o decorador @chain para criar funções personalizadas
from langchain_core.runnables import chain
from dotenv import load_dotenv
load_dotenv()

# Cria uma função personalizada usando o decorador @chain
# @chain: Transforma a função em um componente compatível com LCEL
# input_dict:dict: Recebe um dicionário como entrada
# -> dict: Retorna um dicionário como saída
@chain
def square(input_dict:dict) -> dict:
    x = input_dict["x"]  # Extrai o valor "x" do dicionário de entrada
    return {"square_result": x * x}  # Retorna o quadrado em um novo dicionário

# Cria um template que usa o resultado da função square
# Já explicado no script 1-fundamentos/3-prompt-template.py
question_template2 = PromptTemplate(
    input_variables=["square_result"],
    template="fale-me sobre o numero {square_result}"
)

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

# Cria uma chain com 3 componentes: função personalizada -> template -> modelo
# square: Calcula o quadrado do número
# question_template2: Formata o prompt com o resultado
# model: Gera a resposta sobre o número
chain2 = square | question_template2 | model

# Invoca a chain passando o valor inicial
# A chain executa: square({"x":10}) -> template.format() -> model.invoke()
result = chain2.invoke({"x":10})

# Exibe o resultado já explicado no script 1-fundamentos/1-hello-world.py
print(result.content)





