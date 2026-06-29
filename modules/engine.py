import os
import sys
import time

from . import utils
from .vars import config
from .vars import systemclear
from .vars import status
from .vars import savefile
from .vars import startfile
from .vars import savepath

reset = False

def main():
    global savefile
    global savepath
    global startfile

    global status
    global reset

    try:
        # Verificando save
        if config["load_savefile"] is True and savefile:
            status = savefile
        else:
            # Começo estático
            status["nextfile"] = startfile

        # Lógica principal do jogo
        while True:
            # Se houver um arquivo para carregar,
            # apenas faça!
            if status["actualfile"] and reset is False:
                game = utils.loadfile(status["actualfile"]) # Jogo na memória

            elif status["nextfile"]:
                game = utils.loadfile(status["nextfile"])

            #print(game)
            #print(len(game[status["part"]]["dialogs"]))
            #input()

            # Já viu começar de outro lugar?
            # Claro que o index pra "folhear" a história
            # é justo do ponto zero!
            if reset is True:
                status["index"] = 0
                status["nextpart"] = None
                status["nextfile"] = None

            if config["clear_dialog"] is True:
                os.system(systemclear)

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

                elif reset is False and status["index"] > 0:
                    print(f"[{newperson}]")

                elif oldperson and oldperson != newperson:
                    # Cheque se o personagem anterior é diferente
                    # ou igual ao atual. Se verdadeiro para diferente,
                    # logo, exibir personagem diferente.
                    # Foi a parte mais legal do código, poxa :,)
                    print(f"\n[{newperson}]")

                # Efeito de digitação 
                utils.typingeffect(config, dialog) 

                # TEM COMO EU OTIMIZAR ESTA PARTE
                status["nextpart"] = section.get("nextpart", None)
                status["nextfile"] = section.get("nextfile", None)

                # Se caso for uma pergunta
                if section.get("question"):
                    status["nextpart"], status["nextfile"] = utils.printchoices(section)

                # Próximo texto....
                status["index"] += 1 
                reset = True

            # Deseja que o jogo pause e continue com enter?
            # Não parece muito legal as vezes.
            # Só configurar e arrastar pra cima, pô!
            if config["pause_enter"] and not section.get("question"):
                input("\nPressione <ENTER> para continuar...")

            # A história apenas continua...
            if status["nextpart"]:
                # Afinal, a história não acaba, poxa.
                # Deixa rolar! Deixa ir pra outra parte!
                time.sleep(config["long_pause"])
                print()

                status["part"] = status["nextpart"]

            # O fim.
            # Na verdade, vou fazer disto aqui um loop futuro.
            # Ainda vou projetar esta parte
            if not status["nextfile"] and not status["nextpart"]:
                break

    except KeyboardInterrupt:
        os.system(systemclear)
        print("Jogo Fechado.")

        # Sistema de salvamento aqui
        if config["save"] is True:
            if status["index"] == len(game[status["part"]]["dialogs"]):
                status["index"] -= 1

            elif status["index"] < 0:
                status["index"] = 0

            utils.savefile(savepath, status)
            print("O jogo foi salvo!")
