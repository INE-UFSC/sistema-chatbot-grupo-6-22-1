#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotEspanhol import BotEspanhol
from Bots.BotIngles import BotIngles
from Bots.BotCachorro import BotCachorro
from Bots.BotBola import BotBola
from Bots.BotBinario import BotBinario


###construa a lista de bots disponíveis aqui
lista_bots = [BotEspanhol("Juan"), BotIngles("John"), BotCachorro("Theo"), BotBola("Bola"), BotBinario("01000101 01100100 01110101")]

#Bots integrados
#lista_bots.append(BotZangado("Zangado"))

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
