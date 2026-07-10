import os
import sys
import time

from . import utils as util
from . import vars as var

def main():
    reset = False

    try:
        # Verificando save
        if var.config["load_savefile"] is True and var.savefile is not None:
            var.status = var.savefile

        else:
            # Começo estático
            var.status["nextfile"] = var.startfile

        # Lógica principal do jogo
        while True:
            # Se houver um arquivo para carregar,
            # apenas faça!
            if var.status["actualfile"] and reset is False:
                game = util.loadfile(var.status["actualfile"]) # Jogo na memória

            elif var.status["nextfile"]:
                game = util.loadfile(var.status["nextfile"])

            # Já viu começar de outro lugar?
            # Claro que o index pra "folhear" a história
            # é justo do ponto zero!
            if reset is True:
                var.status["index"] = 0
                var.status["nextpart"] = None
                var.status["nextfile"] = None

            if var.config["clear_dialog"] is True:
                os.system(var.systemclear)

            while var.status["index"] < len(game[var.status["part"]]["dialogs"]):
                # Definir essa coisa pra não zoar
                # a minha vida, minha existência :D
                dialogs = game[var.status["part"]]["dialogs"]
                section = dialogs[var.status["index"]]
                dialog = section["text"]

                # Próxima parte para continuar
                nextpart = section.get("nextpart")

                # Checagem de personagens
                if var.status["index"] - 1 < 0:
                    oldperson = None
                else:
                    oldperson = dialogs[var.status["index"] - 1].get("person", None)

                # Personagem atual
                newperson = section.get("person", None)

                # Mecanismo de personagem
                if var.status["index"] == 0:
                    print(f"[{newperson}]")

                elif reset is False and var.status["index"] > 0:
                    print(f"[{newperson}]")

                elif oldperson and oldperson != newperson:
                    # Cheque se o personagem anterior é diferente
                    # ou igual ao atual. Se verdadeiro para diferente,
                    # logo, exibir personagem diferente.
                    #
                    # Foi a parte mais legal do código, poxa :,)
                    print(f"\n[{newperson}]")

                # Efeito de digitação 
                util.typingeffect(dialog)

                # Se caso for uma pergunta
                if section.get("question") is True:
                    var.status["nextpart"], var.status["nextfile"] = util.printchoices(section)

                else:
                    var.status["nextpart"] = section.get("nextpart", None)
                    var.status["nextfile"] = section.get("nextfile", None)

                # Próximo texto....
                var.status["index"] += 1 
                reset = True

            # Deseja que o jogo pause e continue com enter?
            # Não parece muito legal as vezes.
            # Só configurar e arrastar pra cima, pô!
            if var.config["pause_enter"] and not section.get("question"):
                input("\nPressione <ENTER> para continuar...")

            # A história apenas continua...
            if var.status["nextpart"]:
                # Afinal, a história não acaba, poxa.
                # Deixa rolar! Deixa ir pra outra parte!
                time.sleep(var.config["long_pause"])
                print() # Nova linha

                var.status["part"] = var.status["nextpart"]

            # O fim.
            # Na verdade, vou fazer disto aqui um loop futuro.
            # Ainda vou projetar esta parte
            if not var.status["nextfile"] and not var.status["nextpart"]:
                break

    except KeyboardInterrupt:
        os.system(var.systemclear)
        print("Jogo Fechado.")

        # Sistema de salvamento aqui
        if var.config["save"] is True:
            # Isto foi escrito para não causar problemas
            # de salvamento
            if var.status["index"] == len(game[var.status["part"]]["dialogs"]):
                var.status["index"] -= 1

            elif var.status["index"] < 0:
                var.status["index"] = 0

            utils.savefile(var.savepath, var.status)
            print("O jogo foi salvo!")
