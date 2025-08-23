# 📚 Anotações de Estudo - LangChain

Este arquivo contém anotações e explicações sobre cada script do projeto para facilitar o estudo e consulta.

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
