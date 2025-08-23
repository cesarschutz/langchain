# ========================================
# CARREGAMENTO DE PDF - LOADERS DE DOCUMENTOS
# ========================================
# Este exemplo demonstra como carregar conteúdo de arquivos PDF usando
# PyPDFLoader e dividir o texto em chunks usando RecursiveCharacterTextSplitter.
# ========================================

# Importa PyPDFLoader para carregar arquivos PDF
from langchain_community.document_loaders import PyPDFLoader
# RecursiveCharacterTextSplitter já explicado no script 2-chains-e-processamento/5-sumarizacao.py
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ===== CARREGAMENTO DE ARQUIVO PDF =====
# PyPDFLoader: Carrega conteúdo de arquivos PDF locais
loader = PyPDFLoader("./gpt5.pdf")
# load(): Extrai texto de todas as páginas do PDF
docs = loader.load()

# ===== DIVISÃO EM CHUNKS =====
# RecursiveCharacterTextSplitter já explicado no script 2-chains-e-processamento/5-sumarizacao.py
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# split_documents(): Divide os documentos em chunks menores
chunks = splitter.split_documents(docs)

# ===== EXIBIÇÃO DO RESULTADO =====
# Exibe o número total de chunks criados
print(len(chunks))


