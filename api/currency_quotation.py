import json
import requests

class CurrencyQuotation:
    @staticmethod
    def get_cotacao():
        url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        response = requests.get(url)
        cotacao = json.loads(response.text)
        return cotacao
