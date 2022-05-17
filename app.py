#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotEspanhol import BotEspanhol
from Bots.BotIngles import BotIngles

###construa a lista de bots disponíveis aqui
lista_bots = [BotEspanhol("Juan"), BotIngles("John")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
