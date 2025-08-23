# ========================================
# PIPELINE DE PROCESSAMENTO - CHAINS COMPLEXAS
# ========================================
# Este exemplo demonstra como criar pipelines complexos com múltiplas
# etapas de processamento. Mostra tradução seguida de sumarização,
# usando StrOutputParser para extrair apenas o texto das respostas.
# ========================================

# Importações já explicadas nos scripts anteriores
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# Importa StrOutputParser para extrair apenas o texto das respostas
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# Template para tradução já explicado no script 1-fundamentos/3-prompt-template.py
template_translate = PromptTemplate(
    input_variables=["initial_text"],
    template="Translate the following text to English:\n ```{initial_text}````"
)

# Template para sumarização já explicado no script 1-fundamentos/3-prompt-template.py
template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words:\n ```{text}```"
)

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
llm_en = ChatOpenAI(model="gpt-5-mini", temperature=0)

# Cria a primeira chain: tradução
# template_translate -> llm_en -> StrOutputParser
# StrOutputParser: Extrai apenas o texto da resposta, removendo metadados
translate = template_translate | llm_en | StrOutputParser()

# Cria o pipeline completo usando dicionário para mapear saída da tradução
# {"text": translate}: Mapeia a saída da tradução para a variável "text"
# template_summary -> llm_en -> StrOutputParser
pipeline = {"text": translate} | template_summary | llm_en | StrOutputParser()

# Invoca o pipeline passando o texto inicial
# O pipeline executa: tradução -> sumarização
result = pipeline.invoke({"initial_text": "*LangChain* é um framework para desenvolvimento de aplicações de IA"})

# Curiosidade: difernenca entre:
# *LangChain* é um framework para desenvolvimento de aplicações de IA"
# LangChain é um framework para desenvolvimento de aplicações de IA"

# Exibe o resultado final (sumarização em 4 palavras)
print(result)