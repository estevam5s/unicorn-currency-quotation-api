# from src.main import CurrencyQuotation
import json
import sys
import os

# Adicione a pasta 'src' ao sys.path para permitir a importação de módulos dessa pasta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import CurrencyQuotation


def test_get_cotacao():
    currency_quotation = CurrencyQuotation()
    cotacao = currency_quotation.get_cotacao()

    # Verifique se o objeto cotacao contém as chaves esperadas
    assert 'USDBRL' in cotacao
    assert 'EURBRL' in cotacao
    assert 'BTCBRL' in cotacao

    # Verifique se cada objeto de cotação contém a chave 'bid'
    assert 'bid' in cotacao['USDBRL']
    assert 'bid' in cotacao['EURBRL']
    assert 'bid' in cotacao['BTCBRL']
