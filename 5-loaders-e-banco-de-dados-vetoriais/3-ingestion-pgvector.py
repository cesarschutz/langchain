# ========================================
# INGESTÃO EM PGVECTOR - BANCO DE DADOS VETORIAL
# ========================================
# Este exemplo demonstra como carregar documentos PDF, criar embeddings
# e armazená-los em um banco de dados vetorial PostgreSQL com pgvector.
# ========================================

import os
from pathlib import Path
from dotenv import load_dotenv

# PyPDFLoader já explicado no script 5-loaders-e-banco-de-dados-vetoriais/2-carregamento-de-pdf.py
from langchain_community.document_loaders import PyPDFLoader
# RecursiveCharacterTextSplitter já explicado no script 2-chains-e-processamento/5-sumarizacao.py
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Importa OpenAIEmbeddings para criar vetores dos documentos
from langchain_openai import OpenAIEmbeddings
# Document já explicado no script 5-loaders-e-banco-de-dados-vetoriais/1-carregamento-usando-WebBaseLoader copy.py
from langchain_core.documents import Document
# Importa PGVector para armazenar vetores no PostgreSQL
from langchain_postgres import PGVector

load_dotenv()

# ===== VERIFICAÇÃO DE VARIÁVEIS DE AMBIENTE =====
# Verifica se todas as variáveis necessárias estão configuradas
for k in ("OPENAI_API_KEY", "PGVECTOR_URL","PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

# ===== CONFIGURAÇÃO DE CAMINHOS =====
# Path(__file__).parent: Obtém o diretório do script atual
current_dir = Path(__file__).parent
# Constrói caminho para o arquivo PDF
pdf_path = current_dir / "gpt5.pdf"

# ===== CARREGAMENTO DO PDF =====
# PyPDFLoader já explicado no script 5-loaders-e-banco-de-dados-vetoriais/2-carregamento-de-pdf.py
docs = PyPDFLoader(str(pdf_path)).load()

# ===== DIVISÃO EM CHUNKS =====
# RecursiveCharacterTextSplitter já explicado no script 2-chains-e-processamento/5-sumarizacao.py
splits = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=150, add_start_index=False).split_documents(docs)
if not splits:
    raise SystemExit(0)

# ===== LIMPEZA E ENRIQUECIMENTO DOS DOCUMENTOS =====
# Remove metadados vazios ou nulos dos documentos
enriched = [
    Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
    )
    for d in splits
]    

# ===== CRIAÇÃO DE IDs ÚNICOS =====
# Gera IDs únicos para cada documento
ids = [f"doc-{i}" for i in range(len(enriched))]

# ===== CONFIGURAÇÃO DOS EMBEDDINGS =====
# OpenAIEmbeddings: Cria vetores numéricos dos textos
embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))

# ===== CONFIGURAÇÃO DO BANCO VETORIAL =====
# PGVector: Armazena vetores no PostgreSQL com extensão pgvector
store = PGVector(
    embeddings=embeddings,  # Modelo para criar embeddings
    collection_name=os.getenv("PGVECTOR_COLLECTION"),  # Nome da coleção
    connection=os.getenv("PGVECTOR_URL"),  # URL de conexão com PostgreSQL
    use_jsonb=True,  # Usa JSONB para metadados (mais eficiente)
)

# ===== INGESTÃO DOS DOCUMENTOS =====
# add_documents: Armazena documentos e seus embeddings no banco
store.add_documents(documents=enriched, ids=ids)

# ===== CÓDIGO COMENTADO - VERSÃO ALTERNATIVA =====
# enriched = []
# for d in splits:
#     meta = {k: v for k, v in d.metadata.items() if v not in ("", None)}
#     new_doc = Document(
#         page_content=d.page_content,
#         metadata=meta
#     )
#     enriched.append(new_doc)