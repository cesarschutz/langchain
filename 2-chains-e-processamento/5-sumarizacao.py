# ========================================
# SUMARIZAÇÃO DE TEXTOS LONGOS - TÉCNICA "STUFF"
# ========================================
# Este exemplo demonstra como sumarizar textos longos usando
# RecursiveCharacterTextSplitter para dividir o texto em chunks
# e load_summarize_chain com técnica "stuff" para criar resumos.
# ========================================

# Importações já explicadas nos scripts anteriores
from langchain_openai import ChatOpenAI
# Importa RecursiveCharacterTextSplitter para dividir textos longos
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Importa load_summarize_chain para criar chains de sumarização
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
load_dotenv()

# Texto longo para ser sumarizado (poema sobre uma cidade)
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

# Cria um splitter para dividir o texto em chunks menores
# - chunk_size=250: Tamanho máximo de cada chunk (caracteres)
# - chunk_overlap=70: Sobreposição entre chunks para manter contexto
splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=70, 
)

# Divide o texto longo em documentos menores
# create_documents: Converte o texto em uma lista de documentos
parts = splitter.create_documents([long_text])

# Código comentado para visualizar os chunks (descomente para ver)
# for part in parts:
#     print(part.page_content)
#     print("-"*30)

# Configuração do modelo já explicada no script 1-fundamentos/1-hello-world.py
llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

# Cria uma chain de sumarização usando técnica "stuff"
# - chain_type="stuff": Técnica que coloca todo o texto em um único prompt
# - verbose=False: Não mostra detalhes do processamento
chain_sumarize = load_summarize_chain(llm, chain_type="stuff", verbose=False)

# Invoca a chain passando os documentos divididos
# A chain sumariza todos os chunks e retorna um resumo final
result = chain_sumarize.invoke({"input_documents": parts})

# Exibe o texto sumarizado
print(result["output_text"])