import os
import json
import requests
from dotenv import load_dotenv
import logging


load_dotenv()


logging.basicConfig(
    filename='log/currency_quotation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class CurrencyQuotation:
    @staticmethod
    def get_cotacao():
        url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        response = requests.get(url)
        cotacao = json.loads(response.text)
        return cotacao

if __name__ == "__main__":
    cotacao = CurrencyQuotation.get_cotacao()
    logging.info('Starting the application')
    print(cotacao)
