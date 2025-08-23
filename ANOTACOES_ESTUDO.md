# 📚 Anotações de Estudo - LangChain

Este arquivo contém anotações e explicações sobre cada script do projeto para facilitar o estudo e consulta.

---

# 🌍 PASTA 1: FUNDAMENTOS

---

## 🌍 Script 1: 1-fundamentos/1-hello-world.py

### Explicação do ChatOpenAI:
```python
ChatOpenAI(model="gpt-5-nano", temperature=0.5)
```

**Parâmetros:**
- **`model="gpt-5-nano"`**: Especifica qual modelo da OpenAI usar
  - `gpt-5-nano`: Modelo mais rápido e econômico
  - Outras opções: `gpt-4`, `gpt-3.5-turbo`, `gpt-4-turbo`
- **`temperature=0.5`**: Controla a criatividade das respostas
  - `0.0`: Respostas muito determinísticas e consistentes
  - `0.5`: Equilíbrio entre criatividade e consistência
  - `1.0`: Respostas muito criativas e variadas

**Quando usar:**
- Para projetos específicos da OpenAI
- Quando você precisa de controle fino sobre os parâmetros
- Para integrações diretas com modelos OpenAI

---

## 🔧 Script 2: 1-fundamentos/2-init-chat-model.py

### Explicação do init_chat_model:
```python
gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
```

**Parâmetros:**
- **`model="gemini-2.5-flash"`**: Especifica o modelo específico do provedor
  - `gemini-2.5-flash`: Modelo rápido do Google
  - Outras opções: `gemini-2.0-flash`, `gemini-1.5-pro`
- **`model_provider="google_genai"`**: Indica qual provedor usar
  - `google_genai`: Para modelos Google Gemini
  - `openai`: Para modelos OpenAI
  - `anthropic`: Para modelos Anthropic Claude

**Vantagens:**
- Flexibilidade para trocar entre provedores
- Código mais genérico e reutilizável
- Suporte a múltiplos provedores de IA

**Quando usar:**
- Para projetos que podem usar diferentes provedores
- Quando você quer flexibilidade para trocar modelos
- Para código mais portável entre diferentes serviços

---

## 📝 Script 3: 1-fundamentos/3-prompt-template.py

### Explicação do PromptTemplate:
```python
template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name!"
)
```

**Parâmetros:**
- **`input_variables=["name"]`**: Lista das variáveis que o template aceita
  - Define quais placeholders podem ser usados no template
  - Pode ter múltiplas variáveis: `["name", "age", "city"]`
- **`template="..."`**: O texto do prompt com placeholders
  - Use `{variavel}` para criar placeholders
  - O texto pode ser qualquer prompt que você queira reutilizar

### Explicação do método format():
```python
text = template.format(name="Wesley")
```

**Funcionalidade:**
- **Substitui as variáveis** por valores reais
- **`name="Wesley"`**: Substitui `{name}` por "Wesley" no template
- **Retorna o prompt final** pronto para ser usado

### Vantagens dos Templates:
- **Reutilização**: Crie um template e use com diferentes valores
- **Consistência**: Mantém a estrutura do prompt sempre igual
- **Manutenibilidade**: Mude o template uma vez, afeta todos os usos
- **Legibilidade**: Código mais limpo e organizado

### Exemplo prático:
```python
# Template criado uma vez
template = PromptTemplate(
    input_variables=["name", "age"],
    template="Olá {name}, você tem {age} anos!"
)

# Usado múltiplas vezes
text1 = template.format(name="João", age="25")
text2 = template.format(name="Maria", age="30")
# Resultado: "Olá João, você tem 25 anos!" e "Olá Maria, você tem 30 anos!"
```

---

## 💬 Script 4: 1-fundamentos/4-chat-prompt-template.py

### Explicação do ChatPromptTemplate:
```python
system = ("system", "you are an assistant that answers questions in a {style} style")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])
```

**Diferença do PromptTemplate simples:**
- **PromptTemplate**: Cria um texto único com variáveis
- **ChatPromptTemplate**: Cria múltiplas mensagens estruturadas (system, user, assistant)

**Estrutura das mensagens:**
- **`("system", "...")`**: Define o papel/comportamento da IA
  - Controla como a IA deve se comportar
  - Pode definir estilo, tom, especialização
- **`("user", "...")`**: Define a entrada/pergunta do usuário
  - O que o usuário está perguntando
  - Pode conter variáveis para personalização

### Explicação do format_messages():
```python
messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")
```

**Funcionalidade:**
- **Substitui variáveis** em todas as mensagens do template
- **Retorna lista de mensagens** estruturadas
- **Preserva a estrutura** system/user/assistant

### Vantagens do ChatPromptTemplate:
- **Estrutura de conversa**: Mantém o contexto de chat
- **Controle de comportamento**: System message define o papel da IA
- **Flexibilidade**: Pode ter múltiplas mensagens (system, user, assistant)
- **Compatibilidade**: Funciona melhor com modelos de chat

### Exemplo de saída:
```python
# Após format_messages():
# system: you are an assistant that answers questions in a funny style
# user: Who is Alan Turing?

# Após invoke():
# assistant: [Resposta engraçada sobre Alan Turing]
```

### Comparação com PromptTemplate:
```python
# PromptTemplate (simples):
template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}!"
)

# ChatPromptTemplate (estruturado):
chat_prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("user", "Tell me about {topic}")
])
```

---

# 🔗 PASTA 2: CHAINS E PROCESSAMENTO

---

## 🔗 Script 1: 2-chains-e-processamento/1-iniciando-com-chains.py

### Explicação do operador pipe (|):
```python
chain = question_template | model
```

**O que é o operador |:**
- **LCEL (LangChain Expression Language)**: Sintaxe para conectar componentes
- **Operador pipe (|)**: Conecta componentes em sequência
- **Pipeline**: Cria um fluxo de processamento: template → modelo

**Como funciona:**
1. **question_template**: Formata o prompt com as variáveis
2. **|**: Conecta o template formatado ao modelo
3. **model**: Recebe o prompt formatado e gera a resposta

### Explicação do invoke com dicionário:
```python
result = chain.invoke({"name": "Wesley"})
```

**Diferença do invoke simples:**
- **Modelo simples**: `model.invoke("texto direto")`
- **Chain**: `chain.invoke({"variavel": "valor"})`

**Vantagens das Chains:**
- **Modularidade**: Cada componente tem uma função específica
- **Reutilização**: Pode trocar componentes facilmente
- **Legibilidade**: Código mais limpo e organizado
- **Flexibilidade**: Pode adicionar mais componentes na sequência

### Exemplo de fluxo:
```python
# 1. Template formata: "Ola, eu sou o Wesley! conteme uma piada!"
# 2. Modelo recebe o texto formatado
# 3. Modelo gera a resposta
# 4. Resultado final é retornado
```

---

## 🔧 Script 2: 2-chains-e-processamento/2-chains-com-decorators.py

### Explicação do decorador @chain:
```python
@chain
def square(input_dict:dict) -> dict:
    x = input_dict["x"]
    return {"square_result": x * x}
```

**O que é o decorador @chain:**
- **Transforma funções Python** em componentes compatíveis com LCEL
- **Permite criar lógica customizada** entre componentes do LangChain
- **Mantém a compatibilidade** com o operador pipe (|)

**Estrutura da função:**
- **`input_dict:dict`**: Recebe um dicionário como entrada
- **`-> dict`**: Retorna um dicionário como saída
- **Deve seguir o padrão**: entrada e saída como dicionários

### Explicação da chain com 3 componentes:
```python
chain2 = square | question_template2 | model
```

**Fluxo de execução:**
1. **square**: Recebe `{"x": 10}` → retorna `{"square_result": 100}`
2. **question_template2**: Recebe `{"square_result": 100}` → formata prompt
3. **model**: Recebe o prompt formatado → gera resposta

### Vantagens das funções personalizadas:
- **Lógica customizada**: Pode adicionar qualquer processamento
- **Reutilização**: Funções podem ser usadas em diferentes chains
- **Flexibilidade**: Pode conectar lógica Python pura com LangChain
- **Testabilidade**: Funções podem ser testadas independentemente

### Exemplo de uso:
```python
# Função personalizada
@chain
def process_data(input_dict: dict) -> dict:
    data = input_dict["data"]
    processed = data.upper()  # Qualquer lógica Python
    return {"processed_data": processed}

# Chain com função customizada
chain = process_data | template | model
result = chain.invoke({"data": "hello world"})
```

---

## ⚡ Script 3: 2-chains-e-processamento/3-runnable-lambda.py

### Explicação do RunnableLambda:
```python
def parse_number(text:str) -> int:
    return int(text.strip())

parse_runnable = RunnableLambda(parse_number)
```

**O que é RunnableLambda:**
- **Transforma funções Python simples** em componentes LCEL
- **Alternativa mais simples** ao decorador @chain
- **Permite tipos diretos** (não precisa de dicionários)

### Diferença entre @chain e RunnableLambda:

**@chain (decorador):**
```python
@chain
def square(input_dict:dict) -> dict:
    x = input_dict["x"]
    return {"square_result": x * x}  # SEMPRE dicionário
```

**RunnableLambda:**
```python
def parse_number(text:str) -> int:
    return int(text.strip())  # Pode retornar qualquer tipo

parse_runnable = RunnableLambda(parse_number)
```

### Quando usar cada um:

**Use @chain quando:**
- ✅ Integrando com outros componentes LangChain
- ✅ Precisando passar dados entre componentes
- ✅ Trabalhando em pipelines complexos

**Use RunnableLambda quando:**
- ✅ Função simples com tipos diretos
- ✅ Processamento básico de dados
- ✅ Não precisa de entrada/saída como dicionário

### Vantagens do RunnableLambda:
- **Simplicidade**: Não precisa de dicionários
- **Flexibilidade**: Pode usar qualquer tipo de entrada/saída
- **Legibilidade**: Código mais direto e simples
- **Reutilização**: Funções Python existentes podem ser facilmente convertidas

### Exemplo de uso:
```python
# Função simples
def clean_text(text: str) -> str:
    return text.strip().lower()

# Transforma em componente
clean_runnable = RunnableLambda(clean_text)

# Usa em chain
chain = clean_runnable | template | model
result = chain.invoke("  HELLO WORLD  ")
```

---

## 🔄 Script 4: 2-chains-e-processamento/4-pipeline-de-processamento.py

### Explicação do StrOutputParser:
```python
from langchain_core.output_parsers import StrOutputParser

translate = template_translate | llm_en | StrOutputParser()
```

**O que é StrOutputParser:**
- **Extrai apenas o texto** das respostas dos modelos
- **Remove metadados** e informações extras
- **Retorna string pura** em vez de objeto complexo

### Explicação do pipeline complexo:
```python
pipeline = {"text": translate} | template_summary | llm_en | StrOutputParser()
```

**Estrutura do pipeline:**
1. **`{"text": translate}`**: Mapeia a saída da tradução para a variável "text"
2. **`template_summary`**: Usa o texto traduzido para criar prompt de sumarização
3. **`llm_en`**: Gera a sumarização
4. **`StrOutputParser()`**: Extrai apenas o texto da resposta

### Fluxo de execução:
```python
# 1. Entrada: "LangChain é um framework para desenvolvimento de aplicações de IA"
# 2. Tradução: "LangChain is a framework for AI application development"
# 3. Sumarização: "AI framework for development"
# 4. Saída: "AI framework for development"
```

### Vantagens dos pipelines complexos:
- **Processamento sequencial**: Múltiplas etapas em uma única chain
- **Reutilização**: Cada etapa pode ser usada independentemente
- **Modularidade**: Fácil de modificar ou adicionar etapas
- **Eficiência**: Processamento otimizado em sequência

### Exemplo de uso do StrOutputParser:
```python
# Sem StrOutputParser:
response = model.invoke("Hello")
# Resultado: AIMessage(content="Hello there!", additional_kwargs={}, ...)

# Com StrOutputParser:
chain = model | StrOutputParser()
response = chain.invoke("Hello")
# Resultado: "Hello there!"
```

### Padrão de mapeamento com dicionário:
```python
# Mapeia saída de uma chain para entrada de outra
pipeline = {"variavel": chain_anterior} | proxima_chain

# Exemplo:
chain1 = template1 | model1 | StrOutputParser()
chain2 = template2 | model2 | StrOutputParser()
pipeline = {"texto_processado": chain1} | chain2
```

---

## 📝 Script 5: 2-chains-e-processamento/5-sumarizacao.py

### Explicação do RecursiveCharacterTextSplitter:
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=70, 
)
parts = splitter.create_documents([long_text])
```

**O que é RecursiveCharacterTextSplitter:**
- **Divide textos longos** em chunks menores
- **Mantém contexto** entre chunks com sobreposição
- **Permite processamento** de textos que excedem o limite dos modelos

**Parâmetros importantes:**
- **`chunk_size=250`**: Tamanho máximo de cada chunk (caracteres)
- **`chunk_overlap=70`**: Sobreposição entre chunks para manter contexto
- **`create_documents()`**: Converte texto em lista de documentos

### Explicação da técnica "stuff":
```python
chain_sumarize = load_summarize_chain(llm, chain_type="stuff", verbose=False)
```

**O que é a técnica "stuff":**
- **Coloca todo o texto** em um único prompt
- **Funciona bem** para textos que cabem no contexto do modelo
- **Processamento simples** e direto

**Vantagens:**
- ✅ Simples de implementar
- ✅ Mantém contexto completo
- ✅ Rápido para textos menores

**Limitações:**
- ❌ Limitado pelo tamanho do contexto do modelo
- ❌ Pode ser ineficiente para textos muito longos

### Fluxo de processamento:
```python
# 1. Texto longo → RecursiveCharacterTextSplitter
# 2. Chunks menores → load_summarize_chain
# 3. Técnica "stuff" → Resumo final
```

### Exemplo de uso:
```python
# Dividir texto
splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=70)
parts = splitter.create_documents([texto_longo])

# Sumarizar
chain = load_summarize_chain(llm, chain_type="stuff")
result = chain.invoke({"input_documents": parts})
resumo = result["output_text"]
```

### Quando usar a técnica "stuff":
- ✅ Textos que cabem no contexto do modelo
- ✅ Sumarizações simples e diretas
- ✅ Quando você quer manter todo o contexto
- ✅ Processamento rápido

---

## 🔄 Script 6: 2-chains-e-processamento/6-sumarizacao-com-map-reduce.py

### Explicação da técnica "map_reduce":
```python
chain_sumarize = load_summarize_chain(llm, chain_type="map_reduce", verbose=False)
```

**O que é a técnica "map_reduce":**
- **Processa cada chunk separadamente** (fase "map")
- **Combina os resumos** em um resumo final (fase "reduce")
- **Funciona com textos muito longos** que não cabem no contexto

### Diferença detalhada entre "stuff" e "map_reduce":

**Técnica "stuff" (Script 5):**
```python
chain_type="stuff"
```
- **Processamento**: Coloca TODO o texto em um único prompt
- **Limitação**: Limitado pelo tamanho do contexto do modelo
- **Velocidade**: Mais rápido (uma única chamada)
- **Contexto**: Mantém contexto completo
- **Uso**: Textos que cabem no contexto

**Técnica "map_reduce" (Script 6):**
```python
chain_type="map_reduce"
```
- **Processamento**: 
  1. **Map**: Sumariza cada chunk separadamente
  2. **Reduce**: Combina todos os resumos em um resumo final
- **Limitação**: Não tem limite de tamanho (processa por partes)
- **Velocidade**: Mais lento (múltiplas chamadas)
- **Contexto**: Pode perder contexto entre chunks
- **Uso**: Textos muito longos

### Fluxo de processamento map_reduce:
```python
# Fase 1 - MAP: Processa cada chunk
Chunk 1 → Sumarização → Resumo 1
Chunk 2 → Sumarização → Resumo 2
Chunk 3 → Sumarização → Resumo 3
...

# Fase 2 - REDUCE: Combina os resumos
[Resumo 1, Resumo 2, Resumo 3, ...] → Sumarização Final → Resumo Final
```

### Comparação prática:

**"Stuff" (Script 5):**
```python
# Uma única chamada
Texto completo → Modelo → Resumo
```

**"Map_reduce" (Script 6):**
```python
# Múltiplas chamadas
Chunk 1 → Modelo → Resumo 1
Chunk 2 → Modelo → Resumo 2
...
[Resumos] → Modelo → Resumo Final
```

### Quando usar cada técnica:

**Use "stuff" quando:**
- ✅ Texto cabe no contexto do modelo
- ✅ Quer processamento rápido
- ✅ Precisa manter contexto completo
- ✅ Textos até ~4000 tokens

**Use "map_reduce" quando:**
- ✅ Texto é muito longo (excede contexto)
- ✅ Pode aceitar perda de contexto entre partes
- ✅ Precisa processar documentos grandes
- ✅ Textos com mais de ~4000 tokens

### Vantagens e desvantagens:

**"Stuff":**
- ✅ Rápido, mantém contexto, simples
- ❌ Limitado pelo contexto do modelo

**"Map_reduce":**
- ✅ Funciona com textos ilimitados, escalável
- ❌ Mais lento, pode perder contexto, complexo

---

## 🔧 Script 7: 2-chains-e-processamento/7-pipeline-de-sumarizacao.py

### Explicação do pipeline manual map-reduce:
```python
# Fase MAP
map_prompt = PromptTemplate.from_template("Write a concise summary of the following text:\n{context}")
map_chain = map_prompt | llm | StrOutputParser()
prepare_map_inputs = RunnableLambda(lambda docs: [{"context": d.page_content} for d in docs])
map_stage = prepare_map_inputs | map_chain.map()

# Fase REDUCE
reduce_prompt = PromptTemplate.from_template("Combine the following summaries into a single concise summary:\n{context}")
reduce_chain = reduce_prompt | llm | StrOutputParser()
prepare_reduce_input = RunnableLambda(lambda summaries: {"context": "\n".join(summaries)})

# Pipeline completo
pipeline = map_stage | prepare_reduce_input | reduce_chain
```

### Diferença entre pipeline manual e load_summarize_chain:

**load_summarize_chain (Script 6):**
```python
chain = load_summarize_chain(llm, chain_type="map_reduce")
```
- ✅ Mais simples de implementar
- ❌ Menos controle sobre cada etapa
- ❌ Prompts fixos (não personalizáveis)

**Pipeline manual (Script 7):**
```python
# Controle total sobre cada etapa
map_prompt = PromptTemplate.from_template("Seu prompt personalizado")
reduce_prompt = PromptTemplate.from_template("Seu prompt personalizado")
```
- ✅ Controle total sobre prompts
- ✅ Personalização completa
- ✅ Flexibilidade máxima
- ❌ Mais código para implementar

### Explicação do PromptTemplate.from_template():
```python
map_prompt = PromptTemplate.from_template("Write a concise summary of the following text:\n{context}")
```

**Vantagem:**
- **Criação rápida** de templates simples
- **Não precisa definir** input_variables explicitamente
- **Detecta automaticamente** as variáveis no template

### Explicação do método .map():
```python
map_stage = prepare_map_inputs | map_chain.map()
```

**O que faz:**
- **Aplica a chain** a cada item da lista de inputs
- **Processamento paralelo** de múltiplos documentos
- **Retorna lista** de resultados

### Fluxo detalhado do pipeline:

**Fase MAP:**
```python
# 1. prepare_map_inputs: Converte documentos em lista de dicionários
# 2. map_chain.map(): Aplica sumarização a cada chunk
# 3. Resultado: Lista de resumos individuais
```

**Fase REDUCE:**
```python
# 1. prepare_reduce_input: Junta todos os resumos em uma string
# 2. reduce_chain: Combina os resumos em um resumo final
# 3. Resultado: Resumo final consolidado
```

### Vantagens do pipeline manual:
- **Controle total**: Personaliza cada etapa
- **Prompts customizados**: Adapta para seu caso de uso
- **Flexibilidade**: Pode adicionar etapas intermediárias
- **Debugging**: Fácil de identificar problemas
- **Otimização**: Pode ajustar cada componente

### Exemplo de personalização:
```python
# Prompt personalizado para sumarização
map_prompt = PromptTemplate.from_template(
    "Summarize this text in exactly 3 bullet points:\n{context}"
)

# Prompt personalizado para combinação
reduce_prompt = PromptTemplate.from_template(
    "Create a poetic summary of these summaries:\n{context}"
)
```

---

# 🤖 PASTA 3: AGENTES E TOOLS

---

## 🤖 Script 1: 3-agentes-e-tools/1-agente-react-e-tools.py

### Explicação do Agente ReAct:
```python
from langchain.agents import create_react_agent, AgentExecutor
```

**O que é um Agente ReAct:**
- **ReAct**: Reasoning and Acting (Raciocínio e Ação)
- **Raciocina** sobre qual ferramenta usar
- **Executa ações** para obter informações
- **Combina** pensamento e ação

### Explicação do decorador @tool:
```python
@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and return the result as a string."""
    return str(result)
```

**O que é o decorador @tool:**
- **Transforma funções Python** em ferramentas do agente
- **`return_direct=True`**: Retorna resultado diretamente
- **`return_direct=False`**: Permite processamento adicional pelo agente

### Explicação do formato ReAct:
```python
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [tools]
Action Input: the input to the action
Observation: the result of the action
```

**Fluxo de raciocínio:**
1. **Question**: Pergunta original
2. **Thought**: Agente pensa sobre o que fazer
3. **Action**: Escolhe qual ferramenta usar
4. **Action Input**: Parâmetros para a ferramenta
5. **Observation**: Resultado da ferramenta
6. **Repete** até ter a resposta final

### Explicação do AgentExecutor:
```python
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent_chain, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors="Invalid format...",
    max_iterations=3
)
```

**Parâmetros importantes:**
- **`verbose=True`**: Mostra o processo de raciocínio
- **`max_iterations=3`**: Limita tentativas (evita loops infinitos)
- **`handle_parsing_errors`**: Mensagem para erros de formato

### Vantagens dos Agentes ReAct:
- **Raciocínio explícito**: Pode ver como o agente pensa
- **Flexibilidade**: Pode usar múltiplas ferramentas
- **Extensibilidade**: Fácil adicionar novas ferramentas
- **Controle**: Define limites e regras

### Exemplo de uso:
```python
# Criar ferramenta
@tool("search")
def search(query: str) -> str:
    return "Resultado da busca"

# Criar agente
tools = [search]
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools)

# Usar agente
result = executor.invoke({"input": "Pergunta do usuário"})
```

### Diferença entre Tools e Funções normais:
- **Função normal**: Executa diretamente
- **Tool**: Integrada ao agente, pode ser escolhida dinamicamente
- **Tool**: Tem descrição que o agente usa para decidir

---

## 🔗 Script 2: 3-agentes-e-tools/2-agente-react-usando-prompt-hub.py

### Explicação do Prompt Hub:
```python
from langchain import hub
prompt = hub.pull("hwchase17/react")
```

**O que é o Prompt Hub:**
- **Repositório de prompts** da comunidade LangChain
- **Prompts testados** e otimizados
- **Reutilização** de templates comprovados
- **Padrões** estabelecidos pela comunidade

### Diferença entre prompt personalizado e Prompt Hub:

**Prompt personalizado (Script 1):**
```python
prompt = PromptTemplate.from_template("""
Answer the following questions as best you can...
{tools}
Use the following format:
Question: {input}
Thought: {agent_scratchpad}
""")
```
- ✅ Controle total sobre o prompt
- ❌ Precisa escrever do zero
- ❌ Pode ter bugs ou ineficiências

**Prompt Hub (Script 2):**
```python
prompt = hub.pull("hwchase17/react")
```
- ✅ Prompt testado e otimizado
- ✅ Criado por especialistas
- ✅ Padrão da comunidade
- ❌ Menos flexibilidade

### Explicação do "hwchase17/react":
```python
hub.pull("hwchase17/react")
```

**O que é:**
- **"hwchase17"**: Harrison Chase (criador do LangChain)
- **"react"**: Prompt para agentes ReAct
- **Prompt oficial** do LangChain para ReAct
- **Testado extensivamente** pela comunidade

### Vantagens do Prompt Hub:
- **Qualidade**: Prompts testados e otimizados
- **Padronização**: Usa formatos estabelecidos
- **Rapidez**: Não precisa criar prompts do zero
- **Confiabilidade**: Menos bugs e problemas
- **Comunidade**: Beneficia-se de melhorias coletivas

### Exemplo de outros prompts do hub:
```python
# Diferentes tipos de prompts disponíveis
prompt1 = hub.pull("hwchase17/react")           # Agente ReAct
prompt2 = hub.pull("hwchase17/react-chat")      # ReAct para chat
prompt3 = hub.pull("hwchase17/zero-shot-react") # ReAct zero-shot
```

### Quando usar cada abordagem:

**Use Prompt Hub quando:**
- ✅ Quer um prompt testado e confiável
- ✅ Está começando com agentes
- ✅ Precisa de padrões estabelecidos
- ✅ Quer rapidez na implementação

**Use prompt personalizado quando:**
- ✅ Precisa de controle total
- ✅ Tem requisitos específicos
- ✅ Quer otimizar para seu caso de uso
- ✅ Precisa de funcionalidades customizadas

### Fluxo de uso do Prompt Hub:
```python
# 1. Importar hub
from langchain import hub

# 2. Baixar prompt
prompt = hub.pull("hwchase17/react")

# 3. Usar no agente
agent = create_react_agent(llm, tools, prompt)
```

---

# 🧠 PASTA 4: GERENCIAMENTO DE MEMÓRIA

---

## 🧠 Script 1: 4-gerenciamento-de-memoria/1-armazenamento-de-historico.py

### Explicação do MessagesPlaceholder:
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])
```

**O que é MessagesPlaceholder:**
- **Reserva espaço** no prompt para inserir mensagens do histórico
- **Variável dinâmica** que é preenchida com mensagens anteriores
- **Mantém contexto** entre múltiplas interações

### Explicação do InMemoryChatMessageHistory:
```python
from langchain_core.chat_history import InMemoryChatMessageHistory

session_store: dict[str, InMemoryChatMessageHistory] = {}
```

**O que é InMemoryChatMessageHistory:**
- **Armazena histórico** de mensagens em memória
- **Temporário**: Perdido quando aplicação é fechada
- **Rápido**: Acesso direto na memória RAM
- **Simples**: Ideal para testes e desenvolvimento

### Explicação do RunnableWithMessageHistory:
```python
from langchain_core.runnables import RunnableWithMessageHistory

conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
```

**Parâmetros importantes:**
- **`chain`**: Chain base (prompt + modelo)
- **`get_session_history`**: Função para obter histórico da sessão
- **`input_messages_key="input"`**: Chave para mensagem atual
- **`history_messages_key="history"`**: Chave para histórico no prompt

### Explicação do gerenciamento de sessões:
```python
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

config = {"configurable": {"session_id": "demo-session"}}
```

**Como funciona:**
- **session_id**: Identifica unicamente uma conversa
- **session_store**: Dicionário que armazena históricos por sessão
- **get_session_history**: Cria ou recupera histórico da sessão
- **config**: Configuração passada para identificar a sessão

### Fluxo de funcionamento:
```python
# 1. Primeira mensagem
response1 = conversational_chain.invoke({"input": "Hello, my name is Wesley"}, config=config)
# Histórico: [HumanMessage("Hello, my name is Wesley"), AIMessage("Hi Wesley!")]

# 2. Segunda mensagem
response2 = conversational_chain.invoke({"input": "What's my name?"}, config=config)
# Histórico: [mensagens anteriores + HumanMessage("What's my name?"), AIMessage("Your name is Wesley")]
```

### Vantagens da memória de conversa:
- **Contexto contínuo**: Modelo lembra informações anteriores
- **Conversas naturais**: Pode referenciar mensagens passadas
- **Múltiplas sessões**: Diferentes usuários/conversas isoladas
- **Flexibilidade**: Pode ser implementada de várias formas

### Limitações do InMemoryChatMessageHistory:
- **Temporário**: Perdido ao reiniciar aplicação
- **Limitado**: Pode consumir muita memória com conversas longas
- **Sem persistência**: Não salva em banco de dados

### Exemplo de uso prático:
```python
# Configurar memória
session_store = {}
def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

# Criar chain com memória
chain_with_memory = RunnableWithMessageHistory(
    chain, get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Usar com diferentes sessões
config1 = {"configurable": {"session_id": "user1"}}
config2 = {"configurable": {"session_id": "user2"}}
```

---

## 🧠 Script 2: 4-gerenciamento-de-memoria/2-historico-baseado-em-sliding-window.py

### Explicação do trim_messages:
```python
from langchain_core.messages import trim_messages

trimmed = trim_messages(
    raw_history,
    token_counter=len,
    max_tokens=2,
    strategy="last",
    start_on="human",
    include_system=True,
    allow_partial=False,
)
```

**O que é trim_messages:**
- **Controla tamanho** do histórico de mensagens
- **Reduz automaticamente** para caber no limite de tokens
- **Implementa sliding window** para manter contexto recente
- **Evita overflow** de contexto do modelo

### Parâmetros importantes:

**`token_counter=len`:**
- **Função para contar** tokens/mensagens
- **`len`**: Conta caracteres (simples para demonstração)
- **Em produção**: Use tokenizer real do modelo

**`max_tokens=2`:**
- **Limite máximo** de tokens/mensagens
- **Muito baixo** neste exemplo para demonstrar o efeito
- **Em produção**: Use limite real do modelo (ex: 4000)

**`strategy="last"`:**
- **Estratégia de corte**: manter as últimas mensagens
- **Alternativas**: `"first"` (primeiras), `"middle"` (meio)
- **Mais comum**: `"last"` para manter contexto recente

**`start_on="human"`:**
- **Ponto de início** para contar tokens
- **`"human"`**: Começa a contar de mensagens humanas
- **Alternativas**: `"assistant"`, `"system"`

**`include_system=True`:**
- **Inclui mensagem** do sistema no histórico
- **Importante**: Manter instruções do sistema
- **Sempre True**: Para manter comportamento do assistente

**`allow_partial=False`:**
- **Não corta** mensagens no meio
- **Mantém integridade** das mensagens
- **Mais seguro**: Evita contexto incompleto

### Explicação do Sliding Window:
```python
def prepare_inputs(payload: dict) -> dict:
    raw_history = payload.get("raw_history", [])
    trimmed = trim_messages(raw_history, ...)
    return {"input": payload.get("input",""), "history": trimmed}
```

**Como funciona:**
- **Histórico bruto**: Todas as mensagens da conversa
- **Processamento**: `trim_messages` reduz para limite
- **Sliding window**: Mantém apenas mensagens recentes
- **Resultado**: Modelo "esquece" informações antigas

### Diferença entre raw_history e history:
```python
conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="raw_history"  # Histórico bruto
)
```

**raw_history vs history:**
- **`raw_history`**: Histórico completo (antes do trim)
- **`history`**: Histórico processado (depois do trim)
- **Fluxo**: raw_history → trim_messages → history → modelo

### Fluxo completo do Sliding Window:

**1. Armazenamento:**
```python
# Todas as mensagens são salvas em raw_history
session_store[session_id] = InMemoryChatMessageHistory()
```

**2. Processamento:**
```python
# trim_messages reduz o histórico para caber no limite
trimmed = trim_messages(raw_history, max_tokens=2, strategy="last")
```

**3. Envio ao modelo:**
```python
# Modelo recebe apenas as mensagens mais recentes
chain.invoke({"input": "nova mensagem", "history": trimmed})
```

### Vantagens do Sliding Window:
- **Controle de custos**: Limita tokens enviados ao modelo
- **Performance**: Evita contextos muito longos
- **Conformidade**: Respeita limites de API
- **Flexibilidade**: Diferentes estratégias de corte

### Limitações do Sliding Window:
- **Perda de contexto**: Informações antigas são perdidas
- **Configuração complexa**: Precisa ajustar parâmetros
- **Token counting**: Precisa de tokenizer preciso
- **Estratégia de corte**: Pode perder informações importantes

### Exemplo prático de uso:
```python
# Configuração realista
trimmed = trim_messages(
    raw_history,
    token_counter=tokenizer.count_tokens,  # Tokenizer real
    max_tokens=4000,  # Limite do modelo
    strategy="last",
    start_on="human",
    include_system=True,
    allow_partial=False,
)
```

### Comparação com memória simples:

**Memória simples (Script 1):**
```python
# Mantém todo o histórico
history_messages_key="history"
```
- ✅ Contexto completo
- ❌ Pode exceder limites
- ❌ Custo crescente

**Sliding Window (Script 2):**
```python
# Controla tamanho do histórico
history_messages_key="raw_history"
prepare_inputs = RunnableLambda(lambda p: trim_messages(p["raw_history"]))
```
- ✅ Controle de custos
- ✅ Performance consistente
- ❌ Perda de contexto antigo

---

## 📝 Notas Gerais

### Diferença entre os métodos:
- **ChatOpenAI**: Específico para OpenAI, mais direto
- **init_chat_model**: Genérico, funciona com múltiplos provedores

### Dicas importantes:
- Sempre use `load_dotenv()` para carregar variáveis de ambiente
- Configure suas API keys no arquivo `.env`
- O método `invoke()` é usado para fazer chamadas aos modelos
- Acesse a resposta com `.content`

---

*Este arquivo será atualizado conforme avançarmos no estudo dos scripts.*
