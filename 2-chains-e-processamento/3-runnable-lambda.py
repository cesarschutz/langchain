# ========================================
# RUNNABLE LAMBDA - FUNÇÕES SIMPLES EM CHAINS
# ========================================
# Este exemplo demonstra como usar RunnableLambda para transformar
# funções Python simples em componentes compatíveis com LCEL.
# RunnableLambda é uma alternativa mais simples ao decorador @chain
# para funções que não precisam de entrada/saída como dicionários.
# ========================================

# Importa RunnableLambda para criar componentes de funções simples
from langchain_core.runnables import RunnableLambda

# Define uma função Python simples que converte texto em número
# - text:str: Recebe uma string como entrada
# - -> int: Retorna um inteiro
def parse_number(text:str) -> int:
    return int(text.strip())  # Remove espaços e converte para inteiro

# Cria um componente RunnableLambda a partir da função
# RunnableLambda: Transforma a função em um componente compatível com LCEL
parse_runnable = RunnableLambda(parse_number)

# Invoca o componente passando uma string
# O componente executa a função parse_number("10") e retorna 10
number = parse_runnable.invoke("10")

print(number)