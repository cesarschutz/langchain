from dotenv import load_dotenv
load_dotenv()

# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                           PASTA 01 - FUNDAMENTOS                                   ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌─────────────────────────────────────────┐
# │  Script 01/01: Hello World - ChatOpenAI │
# └─────────────────────────────────────────┘
def script_01_01_hello_world():
    """Demonstra uso básico do ChatOpenAI"""
    from langchain_openai import ChatOpenAI
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    message = model.invoke("Olá, conte-me uma piada de política")
    print(f"\n📝 Script 01/01 - Hello World ChatOpenAI:")
    print(f"{message.content}")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 01/02: init_chat_model           │
# └──────────────────────────────────────────┘
def script_01_02_init_chat_model():
    """Demonstra uso do init_chat_model genérico"""
    from langchain.chat_models import init_chat_model
    model = init_chat_model(model="gpt-3.5-turbo", model_provider="openai")
    message = model.invoke("Olá, conte-me uma piada de política")
    print(f"\n📝 Script 01/02 - init_chat_model:")
    print(f"{message.content}")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 01/03: PromptTemplate            │
# └──────────────────────────────────────┘
def script_01_03_prompt_template():
    """Demonstra uso de PromptTemplate simples"""
    from langchain.prompts import PromptTemplate
    template = PromptTemplate(
        input_variables=["name"],
        template="Olá, {name}! Como vai?"
    )
    text = template.format(name="Cesar")
    print(f"\n📝 Script 01/03 - PromptTemplate:")
    print(f"{text}")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 01/04: ChatPromptTemplate       │
# └──────────────────────────────────────┘
def script_01_04_chat_prompt_template():
    """Demonstra uso de ChatPromptTemplate com roles"""
    from langchain.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    
    # Define as mensagens
    system = ("system", "Você é um assistente que responde perguntas no estilo {style}")
    user = ("user", "{question}")
    chat_prompt = ChatPromptTemplate([system, user])
    
    # Formata as mensagens
    messages = chat_prompt.format_messages(style="divertido", question="Quem foi Uncle Bob?")
    
    print(f"\n📝 Script 01/04 - ChatPromptTemplate:")
    for msg in messages:
        print(f"  [{msg.type}]: {msg.content}")
    
    # Envia para o modelo
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    response = model.invoke(messages)
    print(f"\n  Resposta: {response.content}")
    print("-" * 50)

# ════════════════════════════════════════════════════════════════════
#                    EXECUÇÃO DOS SCRIPTS DA PASTA 01
# ════════════════════════════════════════════════════════════════════
def executar_pasta_01():
    """Executa todos os scripts da Pasta 01 - Fundamentos"""
    print("\n" + "=" * 70)
    print("              EXECUTANDO SCRIPTS DA PASTA 01 - FUNDAMENTOS")
    print("=" * 70)
    
    # Descomente as funções que deseja executar:
    
    #script_01_01_hello_world()        # Hello World com ChatOpenAI
    #script_01_02_init_chat_model()    # Modelo genérico init_chat_model
    #script_01_03_prompt_template()    # Template simples de prompt
    #script_01_04_chat_prompt_template() # Template de chat com roles
    
    print("\n✅ Scripts da Pasta 01 finalizados!\n")


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                        PASTA 02 - CHAINS E PROCESSAMENTO                          ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌──────────────────────────────────────────┐
# │  Script 02/01: Iniciando com Chains      │
# └──────────────────────────────────────────┘
def script_02_01_iniciando_com_chains():
    """Demonstra o básico de chains no LangChain"""
    # TODO: Adicionar código do script 1-iniciando-com-chains.py
    print(f"\n📝 Script 02/01 - Iniciando com Chains:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 02/02: Chains com Decorators     │
# └──────────────────────────────────────────┘
def script_02_02_chains_com_decorators():
    """Demonstra uso de chains com decorators"""
    # TODO: Adicionar código do script 2-chains-com-decorators.py
    print(f"\n📝 Script 02/02 - Chains com Decorators:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 02/03: Runnable Lambda           │
# └──────────────────────────────────────────┘
def script_02_03_runnable_lambda():
    """Demonstra uso de RunnableLambda"""
    # TODO: Adicionar código do script 3-runnable-lambda.py
    print(f"\n📝 Script 02/03 - Runnable Lambda:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 02/04: Pipeline de Processamento │
# └──────────────────────────────────────────┘
def script_02_04_pipeline_de_processamento():
    """Demonstra criação de pipelines de processamento"""
    # TODO: Adicionar código do script 4-pipeline-de-processamento.py
    print(f"\n📝 Script 02/04 - Pipeline de Processamento:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 02/05: Sumarização               │
# └──────────────────────────────────────────┘
def script_02_05_sumarizacao():
    """Demonstra técnicas de sumarização de texto"""
    # TODO: Adicionar código do script 5-sumarizacao.py
    print(f"\n📝 Script 02/05 - Sumarização:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 02/06: Sumarização com Map-Reduce│
# └──────────────────────────────────────────┘
def script_02_06_sumarizacao_com_map_reduce():
    """Demonstra sumarização usando Map-Reduce"""
    # TODO: Adicionar código do script 6-sumarizacao-com-map-reduce.py
    print(f"\n📝 Script 02/06 - Sumarização com Map-Reduce:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 02/07: Pipeline de Sumarização   │
# └──────────────────────────────────────────┘
def script_02_07_pipeline_de_sumarizacao():
    """Demonstra pipeline completo de sumarização"""
    # TODO: Adicionar código do script 7-pipeline-de-sumarizacao.py
    print(f"\n📝 Script 02/07 - Pipeline de Sumarização:")
    print("TODO: Implementar")
    print("-" * 50)

# ════════════════════════════════════════════════════════════════════
#                    EXECUÇÃO DOS SCRIPTS DA PASTA 02
# ════════════════════════════════════════════════════════════════════
def executar_pasta_02():
    """Executa todos os scripts da Pasta 02 - Chains e Processamento"""
    print("\n" + "=" * 70)
    print("           EXECUTANDO SCRIPTS DA PASTA 02 - CHAINS E PROCESSAMENTO")
    print("=" * 70)
    
    # Descomente as funções que deseja executar:
    
    #script_02_01_iniciando_com_chains()          # Básico de chains
    #script_02_02_chains_com_decorators()         # Chains com decorators
    #script_02_03_runnable_lambda()               # RunnableLambda
    #script_02_04_pipeline_de_processamento()     # Pipeline de processamento
    #script_02_05_sumarizacao()                   # Sumarização de texto
    #script_02_06_sumarizacao_com_map_reduce()    # Map-Reduce
    #script_02_07_pipeline_de_sumarizacao()       # Pipeline completo
    
    print("\n✅ Scripts da Pasta 02 finalizados!\n")


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                           PASTA 03 - AGENTES E TOOLS                              ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌──────────────────────────────────────────┐
# │  Script 03/01: Agente React e Tools      │
# └──────────────────────────────────────────┘
def script_03_01_agente_react_e_tools():
    """Demonstra agentes React com ferramentas"""
    # TODO: Adicionar código do script 1-agente-react-e-tools.py
    print(f"\n📝 Script 03/01 - Agente React e Tools:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 03/02: Agente React - Prompt Hub │
# └──────────────────────────────────────────┘
def script_03_02_agente_react_prompt_hub():
    """Demonstra agentes React usando Prompt Hub"""
    # TODO: Adicionar código do script 2-agente-react-usando-prompt-hub.py
    print(f"\n📝 Script 03/02 - Agente React com Prompt Hub:")
    print("TODO: Implementar")
    print("-" * 50)

# ════════════════════════════════════════════════════════════════════
#                    EXECUÇÃO DOS SCRIPTS DA PASTA 03
# ════════════════════════════════════════════════════════════════════
def executar_pasta_03():
    """Executa todos os scripts da Pasta 03 - Agentes e Tools"""
    print("\n" + "=" * 70)
    print("             EXECUTANDO SCRIPTS DA PASTA 03 - AGENTES E TOOLS")
    print("=" * 70)
    
    # Descomente as funções que deseja executar:
    
    #script_03_01_agente_react_e_tools()          # Agente React com ferramentas
    #script_03_02_agente_react_prompt_hub()       # Agente React com Prompt Hub
    
    print("\n✅ Scripts da Pasta 03 finalizados!\n")


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                       PASTA 04 - GERENCIAMENTO DE MEMÓRIA                         ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌──────────────────────────────────────────┐
# │  Script 04/01: Armazenamento Histórico   │
# └──────────────────────────────────────────┘
def script_04_01_armazenamento_historico():
    """Demonstra armazenamento de histórico de conversas"""
    # TODO: Adicionar código do script 1-armazenamento-de-historico.py
    print(f"\n📝 Script 04/01 - Armazenamento de Histórico:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 04/02: Sliding Window Memory     │
# └──────────────────────────────────────────┘
def script_04_02_sliding_window_memory():
    """Demonstra memória com janela deslizante"""
    # TODO: Adicionar código do script 2-historico-baseado-em-sliding-window.py
    print(f"\n📝 Script 04/02 - Sliding Window Memory:")
    print("TODO: Implementar")
    print("-" * 50)

# ════════════════════════════════════════════════════════════════════
#                    EXECUÇÃO DOS SCRIPTS DA PASTA 04
# ════════════════════════════════════════════════════════════════════
def executar_pasta_04():
    """Executa todos os scripts da Pasta 04 - Gerenciamento de Memória"""
    print("\n" + "=" * 70)
    print("          EXECUTANDO SCRIPTS DA PASTA 04 - GERENCIAMENTO DE MEMÓRIA")
    print("=" * 70)
    
    # Descomente as funções que deseja executar:
    
    #script_04_01_armazenamento_historico()       # Armazenamento de histórico
    #script_04_02_sliding_window_memory()         # Memória com janela deslizante
    
    print("\n✅ Scripts da Pasta 04 finalizados!\n")


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                    PASTA 05 - LOADERS E BANCO DE DADOS VETORIAIS                  ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌──────────────────────────────────────────┐
# │  Script 05/01: WebBaseLoader             │
# └──────────────────────────────────────────┘
def script_05_01_web_base_loader():
    """Demonstra carregamento de dados da web"""
    # TODO: Adicionar código do script 1-carregamento-usando-WebBaseLoader.py
    print(f"\n📝 Script 05/01 - WebBaseLoader:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 05/02: Carregamento de PDF       │
# └──────────────────────────────────────┘
def script_05_02_carregamento_de_pdf():
    """Demonstra carregamento de arquivos PDF"""
    # TODO: Adicionar código do script 2-carregamento-de-pdf.py
    print(f"\n📝 Script 05/02 - Carregamento de PDF:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────┐
# │  Script 05/03: Ingestion PGVector        │
# └──────────────────────────────────────────┘
def script_05_03_ingestion_pgvector():
    """Demonstra ingestão de dados no PGVector"""
    # TODO: Adicionar código do script 3-ingestion-pgvector.py
    print(f"\n📝 Script 05/03 - Ingestion PGVector:")
    print("TODO: Implementar")
    print("-" * 50)

# ┌──────────────────────────────────────────┐
# │  Script 05/04: Search Vector             │
# └──────────────────────────────────────────┘
def script_05_04_search_vector():
    """Demonstra busca vetorial"""
    # TODO: Adicionar código do script 4-search-vector.py
    print(f"\n📝 Script 05/04 - Search Vector:")
    print("TODO: Implementar")
    print("-" * 50)

# ════════════════════════════════════════════════════════════════════
#                    EXECUÇÃO DOS SCRIPTS DA PASTA 05
# ════════════════════════════════════════════════════════════════════
def executar_pasta_05():
    """Executa todos os scripts da Pasta 05 - Loaders e Banco Vetorial"""
    print("\n" + "=" * 70)
    print("       EXECUTANDO SCRIPTS DA PASTA 05 - LOADERS E BANCO VETORIAL")
    print("=" * 70)
    
    # Descomente as funções que deseja executar:
    
    #script_05_01_web_base_loader()               # Carregamento de dados da web
    #script_05_02_carregamento_de_pdf()           # Carregamento de PDFs
    #script_05_03_ingestion_pgvector()            # Ingestão no PGVector
    #script_05_04_search_vector()                 # Busca vetorial
    
    print("\n✅ Scripts da Pasta 05 finalizados!\n")


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                              EXECUÇÃO PRINCIPAL                                   ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

if __name__ == "__main__":
    print("\n" + "🎉" * 35)
    print("            🚀 INICIANDO EXECUÇÃO DO CURSO LANGCHAIN 🚀")
    print("🎉" * 35 + "\n")
    
    # Descomente as pastas que deseja executar:
    
    executar_pasta_01()  # FUNDAMENTOS
    #executar_pasta_02()  # CHAINS E PROCESSAMENTO
    #executar_pasta_03()  # AGENTES E TOOLS
    #executar_pasta_04()  # GERENCIAMENTO DE MEMÓRIA
    #executar_pasta_05()  # LOADERS E BANCO VETORIAL
    
    print("\n" + "🎉" * 35)
    print("            🏁 EXECUÇÃO COMPLETA FINALIZADA COM SUCESSO! 🏁")
    print("🎉" * 35 + "\n")