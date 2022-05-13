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
        for i, comando in enumerate(self.comandos):
            mensagem += str(i) + comando + "\n"
        
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
