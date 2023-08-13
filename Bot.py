import telegram
import requests
import os
import openai
openai.organization = "org-U3Cj04o4w4vwi5zxdygPNUPd "
openai.api_key = os.getenv("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")
openai.Model.list()

# Configura el token de acceso de tu bot de Telegram
TELEGRAM_BOT_TOKEN = '6476747450:AAG00vg3M2eYmMxBzu7wETXpIkxa6IC378Q '

# Función para enviar mensajes a GPT-3
def send_to_gpt3(message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
    }
    data = {
        'prompt': message,
        'max_tokens': 50  # Ajusta el número de tokens según sea necesario
    }
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, json=data)
    return response.json()['choices'][0]['text']

# Función para responder a mensajes de Telegram
def reply(update, context):
    user_message = update.message.text
    gpt3_response = send_to_gpt3(user_message)
    update.message.reply_text(gpt3_response)

def main():
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    updater = telegram.ext.Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, reply))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
