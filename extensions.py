import requests
import json
keys = {
	'евро':'EUR',
	'доллар':'USD',
	'рубль':'RUB',
}

class GetPrice:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ApiException('Невозможно перевести одинаковые валюты')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ApiException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'Не удалось обработать валюту {amount}')
        if amount <=0:
            raise ApiException(f'Количество валюты некорректно {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base * amount


class ApiException(Exception):
    pass
