#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotEspanhol import BotEspanhol

###construa a lista de bots disponíveis aqui
lista_bots = [BotEspanhol("Juan")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
