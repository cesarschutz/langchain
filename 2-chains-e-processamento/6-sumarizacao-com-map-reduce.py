# ========================================
# SUMARIZAÇÃO COM MAP-REDUCE - TÉCNICA AVANÇADA
# ========================================
# Este exemplo demonstra a técnica "map_reduce" para sumarizar
# textos muito longos. Diferente da técnica "stuff", o map_reduce
# processa cada chunk separadamente e depois combina os resultados.
# ========================================

# Importações já explicadas nos scripts anteriores
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
load_dotenv()

# Texto longo já explicado no script 2-chains-e-processamento/5-sumarizacao.py
long_text = """
A aurora costura um dourado pálido pelo beco de vidro.
A cidade boceja em um coro de freios e sirenes distantes.
Janelas piscam desperta uma a uma, como olhos sonolentos.
O tecido das ruas, feito de vapor, se enrola nos bueiros, um rio silencioso.
O vapor do café sobe em espirais sobre a impressão pálida do jornal.
Pedestres desenham luz nas calçadas, apressados, ruidosos com guarda-chuvas.
Ônibus engolem a manhã com seus bocejos altos.
Um pardal pousa numa viga de aço, observando a grade.
O metrô suspira em algum lugar no subsolo, um batimento que sobe.
O néon ainda brilha nos cantos onde a noite se recusou a se retirar.
Um ciclista corta o coro, brilhante de cromo e movimento.
A cidade pigarreia, o ar ficando um pouco menos elétrico.
Sapatos sibilam no concreto, mil pequenos verbos de chegada.
A aurora mantém suas promessas no ritmo silencioso de uma metrópole desperta.
A luz da manhã se derrama pelas janelas imensas de aço e vidro,
lançando sombras geométricas sobre as ruas movimentadas abaixo.
O trânsito flui como rios de metal e luz,
enquanto pedestres se entrelaçam pelas faixas de pedestres com propósito.
Cafeterias exalam calor e o aroma de pão fresco,
enquanto os passageiros seguram seus copos como talismãs contra o frio.
Vendedores de rua chamam em uma sinfonia de idiomas,
suas vozes se misturando ao zumbido distante da construção.
Pombos dançam entre os pés dos trabalhadores apressados,
encontrando migalhas de doces matinais nas calçadas de concreto.
A cidade respira em ritmo com um milhão de batimentos cardíacos,
cada pessoa carregando sonhos e prazos na mesma medida.
Arranha-céus alcançam as nuvens que flutuam como algodão,
enquanto muito abaixo os trens do metrô ressoam nos túneis.
Essa orquestra urbana toca do amanhecer ao anoitecer,
uma canção interminável de ambição, luta e esperança.
"""

# Configuração do splitter já explicada no script 2-chains-e-processamento/5-sumarizacao.py
splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=70, 
)

# Divisão em chunks já explicada no script 2-chains-e-processamento/5-sumarizacao.py
parts = splitter.create_documents([long_text])

# Código comentado para visualizar os chunks já explicado no script 2-chains-e-processamento/5-sumarizacao.py
# for part in parts:
#     print(part.page_content)
#     print("-"*30)

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

# Cria uma chain de sumarização usando técnica "map_reduce"
# - chain_type="map_reduce": Técnica que processa chunks separadamente
# - verbose=False: Não mostra detalhes do processamento
chain_sumarize = load_summarize_chain(llm, chain_type="map_reduce", verbose=False)

# Invoca a chain passando os documentos divididos
# A técnica map_reduce: 1) Sumariza cada chunk → 2) Combina os resumos
result = chain_sumarize.invoke({"input_documents": parts})

# Exibe o resultado completo (inclui metadados do processamento)
print(result)