##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome):
        self.nome = nome
        self.comandos = {}

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    def mostra_comandos(self):
        mensagem = ""
        for i in range(1, len(self.comandos)+1):
            mensagem += f"{i} - {self.comandos[str(i)][0]}\n"
        
        return mensagem

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
