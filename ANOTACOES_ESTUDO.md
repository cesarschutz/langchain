# 📚 Anotações de Estudo - LangChain

Este arquivo contém anotações e explicações sobre cada script do projeto para facilitar o estudo e consulta.

## 📋 ÍNDICE RÁPIDO

### 🌍 PASTA 1: FUNDAMENTOS
- **Script 1**: ChatOpenAI - Como usar modelos OpenAI (GPT) com parâmetros
- **Script 2**: init_chat_model - Como usar modelos de diferentes provedores (Google, OpenAI)
- **Script 3**: PromptTemplate - Como criar prompts reutilizáveis com variáveis
- **Script 4**: ChatPromptTemplate - Como criar conversas estruturadas (system, user, assistant)

### 🔧 PASTA 2: CHAINS E PROCESSAMENTO
- **Script 1**: LCEL e pipe operator (`|`) - Como conectar componentes em sequência
- **Script 2**: @chain decorator - Como criar funções customizadas que funcionam em chains
- **Script 3**: RunnableLambda - Como integrar funções simples em chains
- **Script 4**: Pipeline complexo - Como criar processamento com múltiplas etapas
- **Script 5**: Sumarização "stuff" - Como resumir textos curtos em uma única operação
- **Script 6**: Sumarização "map_reduce" - Como resumir textos muito longos em duas etapas
- **Script 7**: Pipeline manual map-reduce - Como controlar completamente o processo de sumarização

### 🤖 PASTA 3: AGENTES E TOOLS
- **Script 1**: ReAct agent e tools - Como criar agentes que pensam e usam ferramentas
- **Script 2**: Prompt Hub - Como usar prompts otimizados da comunidade

### 🧠 PASTA 4: GERENCIAMENTO DE MEMÓRIA
- **Script 1**: Armazenamento de histórico - Como fazer o modelo lembrar conversas anteriores
- **Script 2**: Sliding window - Como controlar o tamanho da memória para economizar tokens

### 📚 PASTA 5: LOADERS E BANCO DE DADOS VETORIAIS
- **Script 1**: WebBaseLoader - Como carregar conteúdo de páginas web
- **Script 2**: PyPDFLoader - Como extrair texto de arquivos PDF
- **Script 3**: Ingestão PGVector - Como armazenar documentos em banco vetorial PostgreSQL
- **Script 4**: Busca vetorial - Como encontrar documentos similares usando busca semântica

## 🎯 CONCEITOS FUNDAMENTAIS

### 🔑 Componentes Principais
- **Models**: ChatOpenAI, init_chat_model
- **Prompts**: PromptTemplate, ChatPromptTemplate
- **Chains**: LCEL, @chain, RunnableLambda
- **Agents**: ReAct, tools, Prompt Hub
- **Memory**: InMemoryChatMessageHistory, RunnableWithMessageHistory
- **Loaders**: WebBaseLoader, PyPDFLoader
- **Vector Stores**: PGVector, OpenAIEmbeddings

### 🔄 Fluxos Comuns
1. **Processamento básico**: Prompt → Model → Response
2. **Chain complexa**: Input → Process → Output
3. **Agente**: Question → Thought → Action → Observation
4. **Memória**: Input → History → Context → Response
5. **Vector DB**: Document → Embedding → Store → Search

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

# 📚 PASTA 5: LOADERS E BANCO DE DADOS VETORIAIS

---

## 📚 Script 1: 5-loaders-e-banco-de-dados-vetoriais/1-carregamento-usando-WebBaseLoader copy.py

### Explicação do WebBaseLoader:
```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.langchain.com/")
docs = loader.load()
```

**O que é WebBaseLoader:**
- **Carrega conteúdo** de páginas web via HTTP
- **Extrai texto limpo** removendo HTML e formatação
- **Suporta múltiplas URLs** em uma única requisição
- **Automatiza** o processo de coleta de dados da web

### Explicação do método load():
```python
docs = loader.load()
```

**O que faz:**
- **Faz requisição HTTP** para a URL especificada
- **Extrai conteúdo** da página web
- **Remove HTML** e formatação desnecessária
- **Retorna lista** de documentos (Document objects)

### Explicação do split_documents():
```python
chunks = splitter.split_documents(docs)
```

**O que faz:**
- **Recebe lista** de documentos
- **Aplica splitter** a cada documento
- **Retorna chunks** menores e gerenciáveis
- **Mantém metadados** dos documentos originais

### Fluxo completo de carregamento:

**1. Carregamento:**
```python
loader = WebBaseLoader("https://www.langchain.com/")
docs = loader.load()
# Resultado: Lista de Document objects com conteúdo da página
```

**2. Divisão em chunks:**
```python
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)
# Resultado: Lista de chunks menores para processamento
```

**3. Processamento:**
```python
for chunk in chunks:
    print(chunk)  # Cada chunk é um Document object
```

### Estrutura do Document object:
```python
# Cada documento tem:
chunk.page_content  # Conteúdo do texto
chunk.metadata      # Metadados (URL, título, etc.)
```

### Vantagens do WebBaseLoader:
- **Simplicidade**: Uma linha para carregar conteúdo web
- **Automação**: Remove necessidade de scraping manual
- **Robustez**: Lida com diferentes tipos de páginas
- **Flexibilidade**: Suporta múltiplas URLs

### Limitações do WebBaseLoader:
- **Dependência de internet**: Requer conexão ativa
- **Rate limiting**: Pode ser bloqueado por sites
- **Conteúdo dinâmico**: Não carrega JavaScript
- **Formatação**: Pode perder estrutura complexa

### Exemplo de uso com múltiplas URLs:
```python
# Carregar múltiplas páginas
urls = [
    "https://www.langchain.com/",
    "https://www.langchain.com/docs/",
    "https://www.langchain.com/community/"
]
loader = WebBaseLoader(urls)
docs = loader.load()
```

### Exemplo de configuração avançada:
```python
# Configurar headers personalizados
loader = WebBaseLoader(
    "https://www.langchain.com/",
    requests_kwargs={
        "headers": {
            "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0)"
        }
    }
)
```

---

## 📚 Script 2: 5-loaders-e-banco-de-dados-vetoriais/2-carregamento-de-pdf.py

### Explicação do PyPDFLoader:
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./gpt5.pdf")
docs = loader.load()
```

**O que é PyPDFLoader:**
- **Carrega arquivos PDF** locais do sistema
- **Extrai texto** de todas as páginas do PDF
- **Preserva estrutura** básica do documento
- **Suporta PDFs** com texto e imagens (OCR não incluído)

### Explicação do método load() para PDFs:
```python
docs = loader.load()
```

**O que faz:**
- **Lê arquivo PDF** do caminho especificado
- **Extrai texto** de cada página
- **Cria Document objects** para cada página
- **Inclui metadados** como número da página

### Estrutura dos documentos PDF:
```python
# Cada documento representa uma página do PDF
for doc in docs:
    print(f"Página {doc.metadata['page']}: {doc.page_content[:100]}...")
```

**Metadados típicos:**
- **`page`**: Número da página
- **`source`**: Caminho do arquivo PDF
- **`total_pages`**: Total de páginas no PDF

### Fluxo completo de carregamento PDF:

**1. Carregamento:**
```python
loader = PyPDFLoader("./gpt5.pdf")
docs = loader.load()
# Resultado: Lista de Document objects (um por página)
```

**2. Divisão em chunks:**
```python
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)
# Resultado: Chunks menores que podem cruzar páginas
```

**3. Análise:**
```python
print(len(chunks))  # Número total de chunks criados
```

### Vantagens do PyPDFLoader:
- **Simplicidade**: Uma linha para carregar PDFs
- **Preservação**: Mantém estrutura de páginas
- **Metadados**: Inclui informações da página
- **Compatibilidade**: Funciona com maioria dos PDFs

### Limitações do PyPDFLoader:
- **PDFs escaneados**: Não extrai texto de imagens
- **Formatação complexa**: Pode perder layout
- **Tabelas**: Pode não preservar estrutura
- **Arquivos corrompidos**: Pode falhar

### Exemplo de uso com metadados:
```python
# Acessar metadados dos documentos
for doc in docs:
    print(f"Página {doc.metadata['page']}")
    print(f"Conteúdo: {doc.page_content[:200]}...")
    print("-" * 50)
```

### Exemplo de configuração avançada:
```python
# Carregar apenas páginas específicas
loader = PyPDFLoader("./gpt5.pdf")
docs = loader.load()

# Filtrar páginas específicas
filtered_docs = [doc for doc in docs if doc.metadata['page'] <= 5]
```

### Comparação entre loaders:

**WebBaseLoader (Script 1):**
```python
loader = WebBaseLoader("https://www.langchain.com/")
```
- ✅ Carrega conteúdo web
- ❌ Requer internet
- ❌ Pode ser bloqueado

**PyPDFLoader (Script 2):**
```python
loader = PyPDFLoader("./gpt5.pdf")
```
- ✅ Carrega arquivos locais
- ✅ Funciona offline
- ✅ Preserva metadados de página

### Dicas importantes:
- **Caminho relativo**: Use `"./arquivo.pdf"` para arquivos no diretório atual
- **Caminho absoluto**: Use `/caminho/completo/arquivo.pdf` para arquivos específicos
- **Verificação**: Sempre verifique se o arquivo existe antes de carregar
- **Tamanho**: PDFs muito grandes podem demorar para carregar

---

## 📚 Script 3: 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py

### Explicação do OpenAIEmbeddings:
```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))
```

**O que é OpenAIEmbeddings:**
- **Cria vetores numéricos** dos textos (embeddings)
- **Converte texto** em representação matemática
- **Permite busca semântica** por similaridade
- **Modelo padrão**: "text-embedding-3-small" (1536 dimensões)

### Explicação do PGVector:
```python
from langchain_postgres import PGVector

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)
```

**O que é PGVector:**
- **Armazena vetores** no PostgreSQL com extensão pgvector
- **Permite busca por similaridade** usando distância vetorial
- **Suporta metadados** em formato JSONB
- **Escalável**: PostgreSQL é robusto para grandes volumes

### Parâmetros do PGVector:

**`embeddings`:**
- **Modelo de embeddings** para criar vetores
- **Deve ser consistente** entre ingestão e busca

**`collection_name`:**
- **Nome da coleção** no banco de dados
- **Organiza documentos** em grupos lógicos

**`connection`:**
- **URL de conexão** com PostgreSQL
- **Formato**: `postgresql://user:password@host:port/database`

**`use_jsonb=True`:**
- **Usa JSONB** para metadados (mais eficiente)
- **Melhor performance** que JSON simples

### Explicação da verificação de variáveis:
```python
for k in ("OPENAI_API_KEY", "PGVECTOR_URL","PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")
```

**O que faz:**
- **Valida configuração** antes de executar
- **Evita erros** em tempo de execução
- **Garante** que todas as variáveis necessárias estão definidas

### Explicação do Path(__file__).parent:
```python
current_dir = Path(__file__).parent
pdf_path = current_dir / "gpt5.pdf"
```

**O que faz:**
- **`__file__`**: Caminho do script atual
- **`.parent`**: Diretório pai (onde está o script)
- **Constrói caminho** relativo para o PDF
- **Portável**: Funciona em diferentes sistemas

### Explicação da limpeza de metadados:
```python
enriched = [
    Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
    )
    for d in splits
]
```

**O que faz:**
- **Remove valores vazios** (`""`) e nulos (`None`)
- **Limpa metadados** desnecessários
- **Reduz tamanho** do banco de dados
- **Melhora performance** de busca

### Explicação da geração de IDs:
```python
ids = [f"doc-{i}" for i in range(len(enriched))]
```

**O que faz:**
- **Cria IDs únicos** para cada documento
- **Formato**: "doc-0", "doc-1", "doc-2", etc.
- **Permite atualização** e remoção específica
- **Facilita debugging** e rastreamento

### Explicação do add_documents():
```python
store.add_documents(documents=enriched, ids=ids)
```

**O que faz:**
- **Armazena documentos** no banco vetorial
- **Cria embeddings** automaticamente
- **Associa IDs** aos documentos
- **Indexa** para busca rápida

### Fluxo completo de ingestão:

**1. Carregamento:**
```python
docs = PyPDFLoader(str(pdf_path)).load()
# Resultado: Document objects do PDF
```

**2. Divisão:**
```python
splits = RecursiveCharacterTextSplitter(...).split_documents(docs)
# Resultado: Chunks menores
```

**3. Limpeza:**
```python
enriched = [Document(...) for d in splits]
# Resultado: Documentos limpos
```

**4. Embeddings:**
```python
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
# Resultado: Modelo para criar vetores
```

**5. Armazenamento:**
```python
store.add_documents(documents=enriched, ids=ids)
# Resultado: Documentos indexados no banco
```

### Variáveis de ambiente necessárias:

**`.env`:**
```bash
OPENAI_API_KEY=sk-...
PGVECTOR_URL=postgresql://user:password@host:port/database
PGVECTOR_COLLECTION=meus_documentos
OPENAI_MODEL=text-embedding-3-small
```

### Vantagens do PGVector:
- **Busca semântica**: Encontra documentos similares
- **Escalabilidade**: PostgreSQL é robusto
- **Metadados**: Suporta informações adicionais
- **Performance**: Índices otimizados para vetores

### Limitações do PGVector:
- **Complexidade**: Requer PostgreSQL + pgvector
- **Configuração**: Mais setup que soluções simples
- **Custo**: Embeddings da OpenAI têm custo
- **Latência**: Requisições para API de embeddings

### Exemplo de configuração PostgreSQL:
```sql
-- Instalar extensão pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Criar tabela para vetores
CREATE TABLE document_vectors (
    id TEXT PRIMARY KEY,
    embedding vector(1536),
    content TEXT,
    metadata JSONB
);
```

---

## 📚 Script 4: 5-loaders-e-banco-de-dados-vetoriais/4-search-vector.py

### Explicação do similarity_search_with_score():
```python
results = store.similarity_search_with_score(query, k=3)
```

**O que é similarity_search_with_score:**
- **Busca documentos similares** usando similaridade vetorial
- **Retorna tuplas** (documento, score) ordenadas por similaridade
- **Score menor = mais similar** (distância vetorial)
- **Parâmetro k**: Número de resultados a retornar

### Explicação da query de busca:
```python
query = "Tell me more about the gpt-5 thinking evaluation and performance results comparing to gpt-4"
```

**O que é a query:**
- **Texto de busca** que será convertido em embedding
- **Pergunta ou termo** para encontrar documentos similares
- **Processo**: Query → Embedding → Comparação com documentos no banco
- **Resultado**: Documentos mais semanticamente similares

### Explicação do score de similaridade:
```python
for i, (doc, score) in enumerate(results, start=1):
    print(f"Resultado {i} (score: {score:.2f}):")
```

**Interpretação do score:**
- **0.0**: Documentos idênticos
- **0.0 - 0.3**: Muito similar (excelente match)
- **0.3 - 0.7**: Similaridade moderada (bom match)
- **0.7 - 1.0**: Baixa similaridade (match fraco)
- **> 1.0**: Muito diferente (match ruim)

### Fluxo completo de busca vetorial:

**1. Preparação da query:**
```python
query = "Tell me more about the gpt-5 thinking evaluation..."
# Query é convertida em embedding usando o mesmo modelo da ingestão
```

**2. Busca no banco:**
```python
results = store.similarity_search_with_score(query, k=3)
# Retorna os 3 documentos mais similares com seus scores
```

**3. Processamento dos resultados:**
```python
for i, (doc, score) in enumerate(results, start=1):
    print(f"Resultado {i} (score: {score:.2f}):")
    print(doc.page_content)
    print(doc.metadata)
```

### Explicação do parâmetro k:
```python
results = store.similarity_search_with_score(query, k=3)
```

**O que é k:**
- **Número de resultados** a retornar
- **k=3**: Retorna os 3 documentos mais similares
- **k=1**: Retorna apenas o mais similar
- **k=10**: Retorna os 10 mais similares
- **Escolha baseada** na aplicação e performance

### Exibição estruturada dos resultados:
```python
for i, (doc, score) in enumerate(results, start=1):
    print("="*50)
    print(f"Resultado {i} (score: {score:.2f}):")
    print("="*50)
    
    print("\nTexto:\n")
    print(doc.page_content.strip())
    
    print("\nMetadados:\n")
    for k, v in doc.metadata.items():
        print(f"{k}: {v}")
```

**Estrutura da exibição:**
- **Separadores visuais**: `=` para delimitar cada resultado
- **Score formatado**: `{score:.2f}` para 2 casas decimais
- **Conteúdo limpo**: `.strip()` remove espaços extras
- **Metadados organizados**: Chave-valor formatados

### Vantagens da busca vetorial:
- **Busca semântica**: Encontra documentos similares em significado
- **Não depende** de palavras-chave exatas
- **Escalável**: Funciona com grandes volumes de documentos
- **Flexível**: Aceita queries em linguagem natural

### Limitações da busca vetorial:
- **Custo**: Cada busca gera embedding (custo da OpenAI)
- **Latência**: Requisição para API de embeddings
- **Qualidade**: Depende da qualidade dos embeddings
- **Contexto**: Pode não capturar contexto específico

### Exemplo de diferentes tipos de query:
```python
# Query específica
query1 = "What are the performance benchmarks of GPT-5?"

# Query genérica
query2 = "Tell me about AI models"

# Query com comparação
query3 = "How does GPT-5 compare to GPT-4?"

# Query técnica
query4 = "What are the technical specifications?"
```

### Exemplo de filtros por score:
```python
# Filtrar apenas resultados muito similares
good_results = [(doc, score) for doc, score in results if score < 0.3]

# Filtrar resultados moderadamente similares
moderate_results = [(doc, score) for doc, score in results if 0.3 <= score < 0.7]
```

### Comparação com busca tradicional:

**Busca por palavras-chave:**
```python
# Busca exata (não semântica)
if "GPT-5" in document.content:
    return document
```
- ❌ Não encontra sinônimos
- ❌ Não entende contexto
- ✅ Muito rápida
- ✅ Sem custo

**Busca vetorial:**
```python
# Busca semântica
results = store.similarity_search_with_score(query, k=3)
```
- ✅ Encontra documentos similares
- ✅ Entende contexto e significado
- ❌ Mais lenta
- ❌ Tem custo

### Dicas para otimizar busca:
- **Queries específicas**: Melhoram a precisão
- **Ajuste do k**: Balanceie quantidade e qualidade
- **Filtros por score**: Removem resultados irrelevantes
- **Metadados**: Use para filtrar por tipo de documento

---

## 📝 Notas Gerais

### 🔑 Diferenças entre métodos principais:

**ChatOpenAI vs init_chat_model:**
- **ChatOpenAI**: Específico para OpenAI, mais direto e simples
- **init_chat_model**: Genérico, funciona com múltiplos provedores (Google, OpenAI, Anthropic)

**PromptTemplate vs ChatPromptTemplate:**
- **PromptTemplate**: Templates simples de texto com variáveis
- **ChatPromptTemplate**: Templates estruturados com roles (system, human, assistant)

**@chain vs RunnableLambda:**
- **@chain**: Para funções que recebem e retornam dicionários
- **RunnableLambda**: Para funções simples com input/output direto

### 🎯 Dicas importantes para todos os scripts:
- **Sempre use `load_dotenv()`** para carregar variáveis de ambiente
- **Configure suas API keys** no arquivo `.env`
- **O método `invoke()`** é usado para fazer chamadas aos modelos
- **Acesse a resposta** com `.content`
- **Use try/except** para tratar erros de API
- **Monitore custos** das APIs (especialmente OpenAI)

### 📊 Resumo por Complexidade:

**🟢 BÁSICO (Fundamentos):**
- Scripts 1-4 da Pasta 1: Conceitos fundamentais
- Script 1 da Pasta 2: LCEL básico

**🟡 INTERMEDIÁRIO (Chains e Memória):**
- Scripts 2-7 da Pasta 2: Chains avançadas
- Scripts 1-2 da Pasta 3: Agentes básicos
- Scripts 1-2 da Pasta 4: Memória de conversa

**🔴 AVANÇADO (Agentes e Vector DB):**
- Scripts 1-2 da Pasta 3: Agentes com tools
- Scripts 1-4 da Pasta 5: Loaders e banco vetorial

### 🚀 Próximos Passos Sugeridos:

1. **Comece pelos fundamentos** (Pasta 1) - Entenda modelos e prompts
2. **Aprenda chains** (Pasta 2) - Domine o processamento sequencial
3. **Experimente agentes** (Pasta 3) - Automatize tarefas complexas
4. **Implemente memória** (Pasta 4) - Adicione contexto às conversas
5. **Construa RAG** (Pasta 5) - Crie sistemas de busca em documentos

### 💡 Projetos Práticos Sugeridos:

**🟢 Iniciante:**
- Chatbot simples com memória
- Sistema de tradução multi-idioma
- Gerador de resumos de textos

**🟡 Intermediário:**
- Agente de pesquisa com múltiplas ferramentas
- Sistema de análise de sentimentos
- Assistente de programação

**🔴 Avançado:**
- RAG completo com banco vetorial
- Agente multi-modal (texto + imagem)
- Sistema de recomendação baseado em embeddings

---

## 🎓 RESUMO EXECUTIVO

### 📈 Progressão de Aprendizado

**FASE 1 - FUNDAMENTOS (Pasta 1)**
- ✅ Entender modelos de linguagem (OpenAI, Google)
- ✅ Dominar templates de prompt
- ✅ Compreender diferenças entre provedores

**FASE 2 - PROCESSAMENTO (Pasta 2)**
- ✅ Criar chains sequenciais com LCEL
- ✅ Implementar funções customizadas
- ✅ Construir pipelines complexos
- ✅ Dominar técnicas de sumarização

**FASE 3 - AUTOMAÇÃO (Pasta 3)**
- ✅ Criar agentes com ferramentas
- ✅ Usar prompts da comunidade
- ✅ Implementar raciocínio e ação

**FASE 4 - CONTEXTO (Pasta 4)**
- ✅ Adicionar memória às conversas
- ✅ Controlar tamanho do histórico
- ✅ Manter contexto entre interações

**FASE 5 - DADOS (Pasta 5)**
- ✅ Carregar documentos de diferentes fontes
- ✅ Criar e armazenar embeddings
- ✅ Implementar busca semântica
- ✅ Construir sistemas RAG completos

### 🏆 Competências Adquiridas

**Técnicas:**
- ✅ Integração com múltiplos provedores de IA
- ✅ Criação de prompts dinâmicos e estruturados
- ✅ Construção de pipelines de processamento
- ✅ Implementação de agentes autônomos
- ✅ Gerenciamento de memória conversacional
- ✅ Criação de bancos de dados vetoriais
- ✅ Implementação de busca semântica

**Conceituais:**
- ✅ Compreensão de LLMs e seus parâmetros
- ✅ Entendimento de embeddings e similaridade vetorial
- ✅ Conhecimento de arquiteturas RAG
- ✅ Familiaridade com agentes e ferramentas
- ✅ Compreensão de processamento de linguagem natural

### 🔮 Aplicações Práticas

**Desenvolvimento:**
- Chatbots inteligentes com memória
- Sistemas de documentação automatizada
- Assistentes de programação
- Análise de dados com IA

**Negócios:**
- Atendimento ao cliente automatizado
- Análise de documentos e relatórios
- Sistemas de recomendação
- Pesquisa e descoberta de informações

**Educação:**
- Tutores personalizados
- Sistemas de avaliação automática
- Geração de conteúdo educacional
- Análise de textos e redações

---

*Este arquivo será atualizado conforme avançarmos no estudo dos scripts.*
