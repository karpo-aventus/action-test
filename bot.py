import telebot

token = '2074513156:AAEHXH7oKIHy4PIakHME1DjBIRHC76k5YLI'

bot = telebot.TeleBot(token)
#bot.config['api_key'] = token


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello my little pony!')

@ bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'how are you?':
        bot.send_message(message.chat.id, 'I am fine!')
    else:
        bot.send_message(message.chat.id, 'Sorry, I can answer only one question!')


bot.polling()