from abc import ABC, abstractmethod

class ICotacaoPresenter(ABC):
    @abstractmethod
    def bonito(self, cotacao):
        pass

class ConsoleCotacaoPresenter(ICotacaoPresenter):
    def bonito(self, cotacao):
        print('Cotação do Dólar: R$ {}'.format(cotacao['USDBRL']['bid']))
        print('Cotação do Euro: R$ {}'.format(cotacao['EURBRL']['bid']))
        print('Cotação do Bitcoin: R$ {}'.format(cotacao['BTCBRL']['bid']))

