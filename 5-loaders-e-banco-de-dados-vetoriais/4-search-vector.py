# ========================================
# BUSCA VETORIAL - CONSULTA SEMÂNTICA EM BANCO VETORIAL
# ========================================
# Este exemplo demonstra como fazer busca semântica em documentos
# armazenados no banco vetorial PostgreSQL usando similaridade de embeddings.
# ========================================

import os
from dotenv import load_dotenv

# OpenAIEmbeddings já explicado no script 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
from langchain_openai import OpenAIEmbeddings
# PGVector já explicado no script 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
from langchain_postgres import PGVector

load_dotenv()

# ===== VERIFICAÇÃO DE VARIÁVEIS DE AMBIENTE =====
# Verificação já explicada no script 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
for k in ("OPENAI_API_KEY", "PGVECTOR_URL","PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

# ===== DEFINIÇÃO DA CONSULTA =====
# Query: Pergunta ou termo de busca para encontrar documentos similares
query = "Tell me more about the gpt-5 thinking evaluation and performance results comparing to gpt-4"

# ===== CONFIGURAÇÃO DOS EMBEDDINGS =====
# OpenAIEmbeddings já explicado no script 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))

# ===== CONFIGURAÇÃO DO BANCO VETORIAL =====
# PGVector já explicado no script 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

# ===== BUSCA POR SIMILARIDADE =====
# similarity_search_with_score: Busca documentos similares e retorna scores de similaridade
# k=3: Retorna os 3 documentos mais similares
results = store.similarity_search_with_score(query, k=3)

# ===== EXIBIÇÃO DOS RESULTADOS =====
# Itera sobre os resultados ordenados por similaridade
for i, (doc, score) in enumerate(results, start=1):
    print("="*50)
    print(f"Resultado {i} (score: {score:.2f}):")
    print("="*50)

    # Exibe o conteúdo do documento
    print("\nTexto:\n")
    print(doc.page_content.strip())

    # Exibe os metadados do documento
    print("\nMetadados:\n")
    for k, v in doc.metadata.items():
        print(f"{k}: {v}")

