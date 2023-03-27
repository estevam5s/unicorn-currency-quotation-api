import requests
import json
from utils.constants import AWESOME_API_URL
from .provider_interfaces import ICotacaoProvider

class AwesomeApiCotacaoProvider(ICotacaoProvider):
    def get_cotacao(self):
        response = requests.get(AWESOME_API_URL)
        cotacao = json.loads(response.text)
        return cotacao
