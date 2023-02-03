import telegram

import openai

from telegram.ext import Updater

openai.api_key = "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"

updater = Updater(token="6048217054:AAGCyQZ9AlPt_pCJ6BH4YeQp_NJT7rYssaM", use_context=True)

def handle_updates(update, context):

    # Get the text of the message that was received

    message_text = update.message.text

    print(message_text)

    

    # Use the openai.Completion.create() method to generate a response

    if f"@{context.bot.username}" in message_text:

        response = openai.Completion.create(

            engine="text-davinci-003",

            prompt=message_text,

            max_tokens=1024,

            suffix="nlp",

            n=1,

            stop=None,

            temperature=0,

        )

        # Use the bot.send_message() method to send the response back to the user

        context.bot.send_message(

            chat_id=update.message.chat_id,

            text=response["choices"][0]["text"],

        )

updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_updates))

updater.start_polling()

