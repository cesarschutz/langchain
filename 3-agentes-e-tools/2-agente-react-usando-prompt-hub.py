# ========================================
# AGENTE REACT COM PROMPT HUB - TEMPLATES PRÉ-DEFINIDOS
# ========================================
# Este exemplo demonstra como usar o Prompt Hub do LangChain para
# obter prompts pré-definidos e testados pela comunidade, em vez de
# criar prompts personalizados do zero.
# ========================================

# Importações já explicadas nos scripts anteriores
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
# Importa o hub para acessar prompts da comunidade
from langchain import hub
from dotenv import load_dotenv
load_dotenv()

# Tool para cálculos matemáticos já explicado no script 3-agentes-e-tools/1-agente-react-e-tools.py
@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and return the result as a string."""
    try:
        result = eval(expression)  # cuidado: apenas para exemplo didático
    except Exception as e:
        return f"Error: {e}"
    return str(result)

# Tool para busca simulada já explicado no script 3-agentes-e-tools/1-agente-react-e-tools.py
@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Return the capital of a given country if it exists in the mock data."""
    data = {
        "Brazil": "Brasília",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United States": "Washington, D.C."
        
    }
    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"The capital of {country} is {capital}."
    return "I don't know the capital of that country."

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

# Lista de ferramentas (apenas web_search_mock neste exemplo)
tools = [web_search_mock]

# ===== USANDO PROMPT HUB =====

# Obtém um prompt ReAct pré-definido do Prompt Hub
# "hwchase17/react": Prompt ReAct criado por Harrison Chase (criador do LangChain)
# hub.pull(): Baixa o prompt da comunidade LangChain
prompt = hub.pull("hwchase17/react")

# Cria o agente ReAct já explicado no script 3-agentes-e-tools/1-agente-react-e-tools.py
agent_chain = create_react_agent(llm, tools, prompt)

# Cria o executor do agente já explicado no script 3-agentes-e-tools/1-agente-react-e-tools.py
# max_iterations comentado: permite mais tentativas (padrão é 5)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent_chain, 
    tools=tools, 
    verbose=True, 
    # max_iterations=5
)

# ===== TESTANDO O AGENTE =====

# Teste com prompt do Prompt Hub
print(agent_executor.invoke({"input": "What is the capital of Iran?"}))

# Teste comentado para comparação
# print(agent_executor.invoke({"input": "How much is 10 + 10?"}))