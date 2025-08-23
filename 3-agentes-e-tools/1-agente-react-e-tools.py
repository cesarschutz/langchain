# ========================================
# AGENTE REACT COM TOOLS - RAZÃO E AÇÃO
# ========================================
# Este exemplo demonstra como criar um agente ReAct (Reasoning and Acting)
# que pode usar ferramentas (tools) para responder perguntas. O agente
# raciocina sobre qual ferramenta usar e executa ações para obter informações.
# ========================================

# Importações já explicadas nos scripts anteriores
from langchain.tools import tool
from langchain_openai import ChatOpenAI
# Importa funções para criar agentes ReAct
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

# ===== CRIANDO TOOLS (FERRAMENTAS) =====

# Tool para cálculos matemáticos
# @tool: Decorador que transforma função em ferramenta do agente
# return_direct=True: Retorna resultado diretamente sem processamento adicional
@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and return the result as a string."""
    try:
        result = eval(expression)  # cuidado: apenas para exemplo didático
    except Exception as e:
        return f"Error: {e}"
    return str(result)

# Tool para busca simulada de informações
# Simula uma busca web com dados de capitais de países
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

# ===== CONFIGURAÇÃO DO AGENTE =====

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
# disable_streaming=True: Desabilita streaming para melhor compatibilidade com agentes
llm = ChatOpenAI(model="gpt-5-mini", disable_streaming=True)

# Lista de ferramentas disponíveis para o agente
tools = [calculator, web_search_mock]

# Prompt template para o agente ReAct
# Define o formato de raciocínio: Question → Thought → Action → Action Input → Observation
prompt = PromptTemplate.from_template(
"""
Answer the following questions as best you can. You have access to the following tools.
Only use the information you get from the tools, even if you know the answer.
If the information is not provided by the tools, say you don't know.

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action

... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Rules:
- If you choose an Action, do NOT include Final Answer in the same step.
- After Action and Action Input, stop and wait for Observation.
- Never search the internet. Only use the tools provided.

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
)

# Cria o agente ReAct combinando modelo, ferramentas e prompt
# stop_sequence=False: Permite múltiplas iterações de raciocínio
agent_chain = create_react_agent(llm, tools, prompt, stop_sequence=False)

# Cria o executor do agente que gerencia a execução
# verbose=True: Mostra o processo de raciocínio do agente
# handle_parsing_errors: Mensagem de erro para formato inválido
# max_iterations=3: Limita o número de tentativas para evitar loops infinitos
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent_chain, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors="Invalid format. Either provide an Action with Action Input, or a Final Answer only.",
    max_iterations=3)

# ===== TESTANDO O AGENTE =====

# Teste 1: Pergunta que não está nos dados simulados
print(agent_executor.invoke({"input": "What is the capital of Iran?"}))

# Teste 2: Cálculo matemático
print(agent_executor.invoke({"input": "How much is 10 + 10?"}))