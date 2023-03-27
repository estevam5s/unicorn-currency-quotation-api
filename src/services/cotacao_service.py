from models.provider_interfaces import ICotacaoProvider
from services.presenter_interfaces import ICotacaoPresenter

class CotacaoService:
    def __init__(self, cotacao_provider: ICotacaoProvider, cotacao_presenter: ICotacaoPresenter):
        self.cotacao_provider = cotacao_provider
        self.cotacao_presenter = cotacao_presenter

    def get_and_present_cotacao(self):
        cotacao = self.cotacao_provider.get_cotacao()
        self.cotacao_presenter.bonito(cotacao)
