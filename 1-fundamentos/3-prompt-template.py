# ========================================
# TEMPLATES DE PROMPT COM LANGCHAIN
# ========================================
# Este exemplo demonstra como criar templates de prompt reutilizáveis
# usando PromptTemplate. Templates permitem criar prompts dinâmicos
# onde partes do texto podem ser substituídas por variáveis.
# ========================================

# Importa PromptTemplate para criar templates de prompt reutilizáveis
from langchain.prompts import PromptTemplate

# Cria um template de prompt com variáveis dinâmicas
# - input_variables=["name"]: Define quais variáveis o template aceita
# - template="...": Define o texto do prompt com placeholders {variavel}
template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name!"
)

# Formata o template substituindo as variáveis por valores reais
# - name="Wesley": Substitui {name} por "Wesley" no template
text = template.format(name="Wesley")

# Exibe o prompt formatado
print(text)



