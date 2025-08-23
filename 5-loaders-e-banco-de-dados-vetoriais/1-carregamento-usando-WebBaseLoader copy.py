# ========================================
# CARREGAMENTO USANDO WEBBASELOADER - LOADERS DE DOCUMENTOS
# ========================================
# Este exemplo demonstra como carregar conteúdo de páginas web usando
# WebBaseLoader e dividir o texto em chunks usando RecursiveCharacterTextSplitter.
# ========================================

# Importa WebBaseLoader para carregar conteúdo de páginas web
from langchain_community.document_loaders import WebBaseLoader
# RecursiveCharacterTextSplitter já explicado no script 2-chains-e-processamento/5-sumarizacao.py
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ===== CARREGAMENTO DE CONTEÚDO WEB =====
# WebBaseLoader: Carrega conteúdo de URLs da web
loader = WebBaseLoader("https://www.langchain.com/")
# load(): Faz a requisição HTTP e extrai o texto da página
docs = loader.load()

# ===== DIVISÃO EM CHUNKS =====
# RecursiveCharacterTextSplitter já explicado no script 2-chains-e-processamento/5-sumarizacao.py
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# split_documents(): Divide os documentos em chunks menores
chunks = splitter.split_documents(docs)

# ===== EXIBIÇÃO DOS CHUNKS =====
# Itera sobre cada chunk e exibe seu conteúdo
for chunk in chunks:
    print(chunk)
    print("-"*30)

    