import os
import sys
import json
import time

from . import utils

#####################################
# 1. Fazer sistema de progresso (save)
# 2. Fazer sistema de estados
#####################################

# Sistema de limpeza de terminal
systemclear = utils.detectclear()

# Sistema de configuração
setting = utils.loadfile("settings.json")

def main(file):
    try:
        # Indicadores de partes da história 
        # Inicializando eles...
        part = "start" # O padrão é "start"
        actualfile = file

        # Loop para leitura de arquivos
        while True:
            if actualfile:
                game = utils.loadfile(actualfile) # Jogo na memória

            actualfile = None

            # Se você não gostar muito de MUITO texto
            # Acho interessante você ajustar isto em settings.json
            # Aguentar cargas é para os poucos (e loucos)! :,(
            limit_list = 0 

            # Lógica principal do jogo
            while True:
                # Já viu começar de outro lugar?
                # Claro que o index pra "folhear" a história
                # é justo do ponto zero!
                index = 0

                # Resertando as variáveis...
                nextpart = None
                nextfile = None

                # Limpar a tela
                #os.system(systemclear)

                while index < len(game[part]["dialogs"]):
                    # Definir essa coisa pra não zoar
                    # a minha vida, minha existência :D
                    dialogs = game[part]["dialogs"]
                    section = dialogs[index]
                    dialog = section["text"]

                    # Próxima parte para continuar
                    nextpart = section.get("nextpart")

                    # Checagem de personagens
                    if index - 1 < 0:
                        oldperson = None
                    else:
                        oldperson = dialogs[index - 1].get("person", None)

                    # Personagem atual
                    newperson = section.get("person", None)
                    
                    # Mecanismo de personagem
                    if index == 0:
                        print(f"[{newperson}]")

                    # Cheque se o personagem anterior é diferente
                    # ou igual ao atual. Se verdadeiro para diferente,
                    # logo, exibir personagem diferente

                    # Foi a parte mais legal do código, poxa :,)
                    if not oldperson is None and oldperson != newperson:
                        print(f"\n[{newperson}]")

                    # Efeito de digitação 
                    utils.typingeffect(setting, dialog) 
                
                    # Se caso for uma pergunta
                    if section.get("question") is True:
                        nextpart, nextfile = utils.printchoices(section)

                    # Próximo texto....
                    index += 1 

                # Deseja que o jogo pause e continue com enter?
                # Não parece muito legal as vezes.
                # Só configurar e arrastar pra cima, pô!
                if setting["pause_enter"] is True:
                    input("\nPressione <ENTER> para continuar...")
                else:
                    time.sleep(setting["long_pause"])

                # Se houver continuação em outro arquivo,
                # apenas deixar o main loop
                # fazer seu serviço, é claro
                if nextfile:
                    file = nextfile
                    nextfile = None
                    break

                # A história apenas continua...
                if nextpart is None:
                    break
                else:
                    # Afinal, a história não acaba, poxa.
                    # Deixa rolar! Deixa ir pra outra parte!
                    part = nextpart
                    section = game[part]
                    index = 0

            # O fim.
            # Na verdade, vou fazer disto aqui um loop futuro.
            # Ainda vou projetar esta parte
            if nextfile is None and nextpart is None:
                break

    except KeyboardInterrupt:
        os.system(systemclear)
        print("Fechando o jogo...")
        time.sleep(1)
