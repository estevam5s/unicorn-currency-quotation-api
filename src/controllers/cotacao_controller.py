from services.cotacao_service import CotacaoService
from models.provider_interfaces import ICotacaoProvider
from services.presenter_interfaces import ICotacaoPresenter

class CotacaoController:
    def __init__(self, cotacao_provider: ICotacaoProvider, cotacao_presenter: ICotacaoPresenter):
        self.cotacao_service = CotacaoService(cotacao_provider, cotacao_presenter)

    def get_cotacao(self):
        self.cotacao_service.get_and_present_cotacao()
