import os
import sys
import json
import time

from . import utils
from .vars import config, systemclear, status

def main(file):
    try:
        # Inicializando o arquivo
        status["nextfile"] = file

        #os.system(systemclear)

        # Lógica principal do jogo
        while True:
            # Se houver um arquivo para carregar,
            # apenas faça!
            if status["nextfile"]:
                game = utils.loadfile(status["nextfile"]) # Jogo na memória

            # Resetando as variáveis...

            # Já viu começar de outro lugar?
            # Claro que o index pra "folhear" a história
            # é justo do ponto zero!
            status["index"] = 0
            status["nextpart"] = None
            status["nextfile"] = None

            while status["index"] < len(game[status["part"]]["dialogs"]):
                # Definir essa coisa pra não zoar
                # a minha vida, minha existência :D
                dialogs = game[status["part"]]["dialogs"]
                section = dialogs[status["index"]]
                dialog = section["text"]

                # Próxima parte para continuar
                nextpart = section.get("nextpart")

                # Checagem de personagens
                if status["index"] - 1 < 0:
                    oldperson = None
                else:
                    oldperson = dialogs[status["index"] - 1].get("person", None)

                # Personagem atual
                newperson = section.get("person", None)
                
                # Mecanismo de personagem
                if status["index"] == 0:
                    print(f"[{newperson}]")

                # Cheque se o personagem anterior é diferente
                # ou igual ao atual. Se verdadeiro para diferente,
                # logo, exibir personagem diferente.
                # Foi a parte mais legal do código, poxa :,)
                if oldperson and oldperson != newperson:
                    print(f"\n[{newperson}]")

                # Efeito de digitação 
                utils.typingeffect(config, dialog) 

                if section.get("nextpart"):
                    status["nextpart"] = section.get("nextpart")

                if section.get("nextfile"):
                    status["nextfile"] = section.get("nextfile")
            
                # Se caso for uma pergunta
                if section.get("question"):
                    #print()
                    status["nextpart"], status["nextfile"] = utils.printchoices(section)

                # Próximo texto....
                status["index"] += 1 

            # Deseja que o jogo pause e continue com enter?
            # Não parece muito legal as vezes.
            # Só configurar e arrastar pra cima, pô!
            if config["pause_enter"] and not section.get("question"):
                input("\nPressione <ENTER> para continuar...")
            else:
                time.sleep(config["long_pause"])


            # A história apenas continua...
            if status["nextpart"]:
                # Afinal, a história não acaba, poxa.
                # Deixa rolar! Deixa ir pra outra parte!
                status["part"] = status["nextpart"]

            # O fim.
            # Na verdade, vou fazer disto aqui um loop futuro.
            # Ainda vou projetar esta parte
            if not status["nextfile"] and not status["nextpart"]:
                break

    except KeyboardInterrupt:
        os.system(systemclear)
        print("Fechando o jogo...")

        # Sistema de salvamento aqui
        pass
        
        time.sleep(1)

        os.system(systemclear)
