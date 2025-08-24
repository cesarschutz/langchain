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
# └──────────────────────────────────────────┘
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
# └──────────────────────────────────────────┘
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
#                        EXECUÇÃO DOS SCRIPTS DA PASTA 01
# ════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("              EXECUTANDO SCRIPTS DA PASTA 01 - FUNDAMENTOS")
    print("=" * 70)
    
    # Descomente as funções que deseja executar:
    
    # script_01_01_hello_world()        # Hello World com ChatOpenAI
    # script_01_02_init_chat_model()    # Modelo genérico init_chat_model
    # script_01_03_prompt_template()    # Template simples de prompt
    # script_01_04_chat_prompt_template() # Template de chat com roles
    
    print("\n✅ Scripts da Pasta 01 finalizados!\n")


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                        PASTA 02 - CHAINS E PROCESSAMENTO                          ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌──────────────────────────────────────────┐
# │  Script 02/01: Iniciando com Chains      │
# └──────────────────────────────────────────┘


# ┌──────────────────────────────────────────┐
# │  Script 02/02: Chains com Decorators     │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 2-chains-com-decorators.py


# ┌──────────────────────────────────────────┐
# │  Script 02/03: Runnable Lambda           │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 3-runnable-lambda.py


# ┌──────────────────────────────────────────┐
# │  Script 02/04: Pipeline de Processamento │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 4-pipeline-de-processamento.py


# ┌──────────────────────────────────────────┐
# │  Script 02/05: Sumarização               │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 5-sumarizacao.py


# ┌──────────────────────────────────────────┐
# │  Script 02/06: Sumarização com Map-Reduce│
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 6-sumarizacao-com-map-reduce.py


# ┌──────────────────────────────────────────┐
# │  Script 02/07: Pipeline de Sumarização   │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 7-pipeline-de-sumarizacao.py


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                           PASTA 03 - AGENTES E TOOLS                              ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌──────────────────────────────────────────┐
# │  Script 03/01: Agente React e Tools      │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 1-agente-react-e-tools.py


# ┌──────────────────────────────────────────┐
# │  Script 03/02: Agente React - Prompt Hub │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 2-agente-react-usando-prompt-hub.py


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                       PASTA 04 - GERENCIAMENTO DE MEMÓRIA                         ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌──────────────────────────────────────────┐
# │  Script 04/01: Armazenamento Histórico   │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 1-armazenamento-de-historico.py


# ┌──────────────────────────────────────────┐
# │  Script 04/02: Sliding Window Memory     │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 2-historico-baseado-em-sliding-window.py


# ╔════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                    ║
# ║                    PASTA 05 - LOADERS E BANCO DE DADOS VETORIAIS                  ║
# ║                                                                                    ║
# ╚════════════════════════════════════════════════════════════════════════════════════╝

# ┌──────────────────────────────────────────┐
# │  Script 05/01: WebBaseLoader             │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 1-carregamento-usando-WebBaseLoader.py


# ┌──────────────────────────────────────────┐
# │  Script 05/02: Carregamento de PDF       │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 2-carregamento-de-pdf.py


# ┌──────────────────────────────────────────┐
# │  Script 05/03: Ingestion PGVector        │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 3-ingestion-pgvector.py


# ┌──────────────────────────────────────────┐
# │  Script 05/04: Search Vector             │
# └──────────────────────────────────────────┘
# TODO: Adicionar código do script 4-search-vector.py
