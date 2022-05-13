from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print(f"Bem vindo ao sistema de chatbot da {self.__empresa}\n")
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print("Escolha um dos bots disponíveis:")
        for i, bot in enumerate(self.__lista_bots):
            print(f"{i} - {bot.nome} : {bot.apresentacao()}")
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        num = input("Digite o número do bot que deseja utilizar: ")
        self.__bot = self.__lista_bots[int(num)]
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        print("Os comandos disponíveis são: ")
        print(self.__bot.mostra_comandos())
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        comando = input("Digite o comando que deseja executar (ou -1 para fechar o programa): ")
        if comando == "-1":
            return True
        else:
            print(self.__bot.executa_comando(comando))
            return False
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot  
        self.escolhe_bot()    
        ##mostra mensagens de boas-vindas do bot escolhido
        print(self.__bot.boas_vindas())
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
            self.mostra_comandos_bot()
            if self.le_envia_comando():
                break
        ##ao sair mostrar a mensagem de despedida do bot
        print(self.__bot.despedida())
