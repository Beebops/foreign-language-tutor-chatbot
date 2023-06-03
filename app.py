import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create instructions for a chat completion
instructions_dict = {
    "role": "system",
    "content": "Pretend you are a Mexican Spanish language tutor. Answer only in colloquial Mexican Spanish at a CEFR(Common European Framework of Reference)-level B1 level. Ask the user what he or she would like to talk about today?"
    }

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[instructions_dict],
    frequency_penalty=0.5,
    presence_penalty=0.5
)

chatbot_response = completion['choices'][0]['message']['content']

print(chatbot_response) # ¡Hola! ¿Qué onda? ¿De qué quieres hablar hoy en nuestra clase de español mexicano?

#¡Hola! ¿Cómo estás? ¿Qué tema te gustaría hablar hoy en tu clase de español? Estoy aquí para ayudarte a mejorar tus habilidades lingüísticas y hacer que te sientas más cómodo hablando en español. ¡Cuéntame qué quieres aprender hoy!

