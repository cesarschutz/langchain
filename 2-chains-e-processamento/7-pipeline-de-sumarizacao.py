# ========================================
# PIPELINE DE SUMARIZAÇÃO MANUAL - MAP-REDUCE PERSONALIZADO
# ========================================
# Este exemplo demonstra como criar um pipeline de sumarização
# map-reduce manual usando LCEL, em vez de usar load_summarize_chain.
# Permite controle total sobre cada etapa do processo.
# ========================================

# Importações já explicadas nos scripts anteriores
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

# Texto longo em inglês para demonstração
long_text = """Dawn threads a pale gold through the alley of glass.
The city yawns in a chorus of brakes and distant sirens.
Windows blink awake, one by one, like sleepy eyes.
Streetcloth of steam curls from manholes, a quiet river.
Coffee steam spirals above a newspaper's pale print.
Pedestrians sketch light on sidewalks, hurried, loud with umbrellas.
Buses swallow the morning with their loud yawns.
A sparrow perches on a steel beam, surveying the grid.
The subway sighs somewhere underground, a heartbeat rising.
Neon still glows in the corners where night refused to retire.
A cyclist cuts through the chorus, bright with chrome and momentum.
The city clears its throat, the air turning a little less electric.
Shoes hiss on concrete, a thousand small verbs of arriving.
Dawn keeps its promises in the quiet rhythm of a waking metropolis.
The morning light cascades through towering windows of steel and glass,
casting geometric shadows on busy streets below.
Traffic flows like rivers of metal and light,
while pedestrians weave through crosswalks with purpose.
Coffee shops exhale warmth and the aroma of fresh bread,
as commuters clutch their cups like talismans against the cold.
Street vendors call out in a symphony of languages,
their voices mixing with the distant hum of construction.
Pigeons dance between the feet of hurried workers,
finding crumbs of breakfast pastries on concrete sidewalks.
The city breathes in rhythm with a million heartbeats,
each person carrying dreams and deadlines in equal measure.
Skyscrapers reach toward clouds that drift like cotton,
while far below, subway trains rumble through tunnels.
This urban orchestra plays from dawn until dusk,
a endless song of ambition, struggle, and hope."""

# Configuração do splitter já explicada no script 2-chains-e-processamento/5-sumarizacao.py
spliter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
parts = spliter.create_documents([long_text])

# Código comentado para visualizar os chunks já explicado no script 2-chains-e-processamento/5-sumarizacao.py
# print all parts
# for part in parts:
#     print(part.page_content)
#     print("-" * 10)

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

# ===== FASE MAP: Sumarizar cada chunk individualmente =====

# Cria o prompt para sumarização de cada chunk
# from_template: Cria um PromptTemplate a partir de uma string simples
map_prompt = PromptTemplate.from_template("Write a concise summary of the following text:\n{context}")

# Cria a chain para sumarização: prompt -> modelo -> extrair texto
map_chain = map_prompt | llm | StrOutputParser()

# Função para preparar os inputs da fase map
# Converte documentos em lista de dicionários com a chave "context"
prepare_map_inputs = RunnableLambda(lambda docs: [{"context": d.page_content} for d in docs])

# Cria a etapa map que processa cada chunk
# .map(): Aplica a chain a cada item da lista de inputs
map_stage = prepare_map_inputs | map_chain.map()

# ===== FASE REDUCE: Combinar os resumos em um resumo final =====

# Cria o prompt para combinar os resumos
reduce_prompt = PromptTemplate.from_template("Combine the following summaries into a single concise summary:\n{context}")

# Cria a chain para combinação: prompt -> modelo -> extrair texto
reduce_chain = reduce_prompt | llm | StrOutputParser()

# Função para preparar o input da fase reduce
# Junta todos os resumos em uma única string
prepare_reduce_input = RunnableLambda(lambda summaries: {"context": "\n".join(summaries)})

# ===== PIPELINE COMPLETO =====

# Conecta as duas fases: map -> prepare_reduce -> reduce
pipeline = map_stage | prepare_reduce_input | reduce_chain

# Executa o pipeline completo
# O pipeline: 1) Sumariza cada chunk → 2) Combina os resumos → 3) Resumo final
result = pipeline.invoke(parts)

# Exibe o resultado final
print(result)








