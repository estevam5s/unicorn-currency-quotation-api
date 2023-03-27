from abc import ABC, abstractmethod

class ICotacaoProvider(ABC):
    @abstractmethod
    def get_cotacao(self):
        pass
