import os
from pathlib import Path
import re
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def main():
    """Função principal para executar o desafio"""
    print("Iniciando o desafio...")
    
    # Processa o PDF e salva na base de dados
    #process_pdf_to_database("Prompt-Engineering-para-Desenvolvedores.pdf")

    perguntas = [
        "O que é o Prompt Engineering?",
        "Quais são as técnicas de prompt engineering?",
        "Como fazer few-shot prompting?"
    ]

    for pergunta in perguntas:
        print(f"\n📝 Pergunta: {pergunta}\n")
        resposta = call_model(pergunta)
        print(f"🤖 Resposta:\n{resposta}\n")
        print("-"*50)
    
    print("Desafio finalizado!")

def process_pdf_to_database(pdf_name: str):
    """Processa um PDF e salva na base de dados"""
    print(f"📚 Processando o PDF: {pdf_name}")
    
    # Lê pdf de prompt engineering
    doc = read_pdf(pdf_name)
    print(f"✅ PDF carregado: {len(doc)} páginas")

    # Cria chunks
    chunks = create_chunks(doc)
    print(f"✅ Chunks criados: {len(chunks)} chunks")

    # Enriquece documents
    enriched = enrich_chunks(chunks)
    print(f"✅ Documentos enriquecidos: {len(enriched)} documentos")

    # Salva na base de dados
    save_to_db(enriched)

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

# funcao para chamar modelo com pergunta do usuário
def call_model(query: str) -> str:
    """Chama um modelo com uma pergunta do usuário"""
    # Busca documentos relevantes na base de dados
    results = search_in_db(query)
    
    # Constrói o contexto com os documentos encontrados
    context = "\n\n".join([
        f"Documento {i+1}:\n{doc.page_content}" 
        for i, (doc, score) in enumerate(results)
    ])
    
    # Cria o prompt com o contexto e a pergunta
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente especializado em Prompt Engineering. Use o contexto fornecido para responder a pergunta do usuário. Se a resposta não estiver no contexto, diga que não encontrou a informação nos documentos."),
        ("user", """Contexto dos documentos:
{context}

Pergunta: {question}

Responda com base no contexto fornecido.""")
    ])
    
    # Inicializa o modelo
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_CHAT", "gpt-3.5-turbo"),
        temperature=0.7
    )
    
    # Cria a chain
    chain = prompt_template | llm
    
    # Executa a chain
    response = chain.invoke({
        "context": context,
        "question": query
    })
    
    return response.content

# funcao para buscar na base de dados
def search_in_db(query: str) -> list[float]:
    """Busca por um texto na base de dados"""
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))
    store = PGVector(
      embeddings=embeddings,  # Modelo para criar embeddings
      collection_name=os.getenv("PGVECTOR_COLLECTION"),  # Nome da coleção
      connection=os.getenv("PGVECTOR_URL"),  # URL de conexão com PostgreSQL
      use_jsonb=True,  # Usa JSONB para metadados (mais eficiente)
    )
    results = store.similarity_search_with_score(query, k=3)

    print(f"\n🔍 Encontrados {len(results)} documentos relevantes para: '{query}'\n")
    
    # ===== EXIBIÇÃO DOS RESULTADOS =====
    #for i, (doc, score) in enumerate(results, start=1):
    #    print("="*50)
    #    print(f"Resultado {i} (score: {score:.2f}):")
    #    print("="*50)

        # Exibe o conteúdo do documento
    #    print("\nTexto:\n")
    #    print(doc.page_content.strip())

        # Exibe os metadados do documento
    #    print("\nMetadados:\n")
    #    for k, v in doc.metadata.items():
    #        print(f"{k}: {v}")

    return results

main()