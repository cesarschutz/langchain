
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

def main():
    """Função principal para executar o desafio"""
    print("Iniciando o desafio...")
    
    # Lê pdf de prompt engineering
    doc = read_pdf("Prompt-Engineering-para-Desenvolvedores.pdf")

    # Cria chunks
    chunks = create_chunks(doc)

    # Enriquece documents
    enriched = enrich_chunks(chunks)

    # Salva na base de dados
    save_to_db(enriched)
    

    print("Desafio finalizado!")

# funcao para ler pdf
def read_pdf(pdf_name: str) -> str:
    """Lê um arquivo pdf com langchain"""
    current_dir = Path(__file__).parent
    doc = PyPDFLoader(str(current_dir / pdf_name)).load()
    #print(f"doc:\n{doc}")
    return doc

# funcao para criar os chunks
def create_chunks(text: str) -> list[str]:
    """Cria chunks para um texto"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100, add_start_index=False)
    chunks = splitter.split_documents(text)
    #for chunk in chunks:
    #  print(f"chunk:\n{chunk.page_content}")
    #  print(f"metadata:\n{chunk.metadata}")
    #  print("-"*100)
    return chunks

# funcao para enriquecer os chunks
def enrich_chunks(chunks: list[str]) -> list[str]:
    """Enriquece os chunks com o modelo de embeddings"""
    enriched = [
      Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
      )
      for d in chunks
    ]
    #for enriched in enriched:
    #  print(f"enriched:\n{enriched.page_content}")
    #  print(f"metadata:\n{enriched.metadata}")
    #  print("-"*100)
    return enriched

# funcao para salvar na base de dados
def save_to_db(enriched: list[str]):
    """Salva embeddings na base de dados"""
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))
    store = PGVector(
      embeddings=embeddings,  # Modelo para criar embeddings
      collection_name=os.getenv("PGVECTOR_COLLECTION"),  # Nome da coleção
      connection=os.getenv("PGVECTOR_URL"),  # URL de conexão com PostgreSQL
      use_jsonb=True,  # Usa JSONB para metadados (mais eficiente)
    )
    ids = [f"doc-{i}" for i in range(len(enriched))]
    store.add_documents(documents=enriched, ids=ids)
    print(f"Documentos salvos na base de dados: {len(enriched)}")

# funcao para buscar na base de dados
def search_in_db(query: str) -> list[float]:
    """Busca por um texto na base de dados"""


# funcao para chamar modelo com pergunta do usuário
def call_model(query: str) -> str:
    """Chama um modelo com uma pergunta do usuário"""

main()