# ========================================
# INICIALIZAÇÃO DE MODELO CHAT COM GOOGLE GEMINI
# ========================================
# Este exemplo demonstra como usar a função init_chat_model para
# inicializar diferentes provedores de modelos de linguagem.
# Neste caso, usamos o Google Gemini em vez da OpenAI.
# ========================================

# Importa a função init_chat_model que permite inicializar diferentes provedores
from langchain.chat_models import init_chat_model
# Importações já explicadas no script 1-fundamentos/1-hello-world.py
from dotenv import load_dotenv
load_dotenv()

# Inicializa um modelo do Google Gemini usando init_chat_model
# - model="gemini-2.5-flash": Especifica o modelo Gemini a ser usado
# - model_provider="google_genai": Indica que é um modelo do Google
gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

# Método invoke() já explicado no script 1-fundamentos/1-hello-world.py
answer_gemini = gemini.invoke("Olá Mundo!")

# Exibição do resultado já explicada no script 1-fundamentos/1-hello-world.py
print(answer_gemini.content)