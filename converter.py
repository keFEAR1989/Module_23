import telebot
from extensions import APIException, CryptoConverter
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    text = 'Я могу конвертировать валюты. Чтобы узнать список доступных валют, введите команду /values. Чтобы узнать цену, введите запрос в формате: <имя валюты цену которой он хочет узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def send_values(message):
    text = 'Доступные валюты: USD, EUR, RUB.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert_currency(message):
    try:
        base, quote, amount = message.text.split(' ')
        result = CryptoConverter.get_price(base.upper(), quote.upper(), amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка: {e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Не удалось обработать запрос: {e}')
    else:
        text = f'{amount} {base.upper()} = {result} {quote.upper()}'
        bot.send_message(message.chat.id, text)

bot.polling()
