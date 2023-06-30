import requests
import json

class APIException(Exception):
    def __init__(self, message):
        self.message = message

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно конвертировать одинаковые валюты {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}&api_key=e09f04ebd9cc5fb652e80d06dd0d55775f2d0da0f931eaa67200d78dee777ec8')
        result = json.loads(r.content)[quote]
        total = result * amount
        return total