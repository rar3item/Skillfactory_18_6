import telebot
import extensions
from extensions import GetPrice
import api_key
token = api_key.TOKEN
bot = telebot.TeleBot(token)
keys = extensions.keys

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Приветствую, для работы с ботом введите комманду в следующем формате: \nимя валюты|в какую валюту перевести|количество переводимой валюты\nчтобы узнать доступные валюты введите комманду /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
	text = 'Доступные валюты:'
	for key in keys.keys():
		text = '\n' .join((text, key, ))
	bot.reply_to(message, text)

api_key = 'ba52ce232d495e2f23e601d55c193a8ddb78c1952b2c3c28240243515b2ac2a4'

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise ApiException('Параметры некорректны')
    quote, base, amount = values
    total_base = GetPrice.convert(quote, base, amount)

    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()

