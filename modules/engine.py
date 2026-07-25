import os
import time

from . import common

def main():
    reset = False

    # Verificando save
    if common.config["load_savefile"] is True and common.savefile is not None:
        common.status = common.savefile

    else:
        # Começo estático
        common.status["nextfile"] = common.startfile

    # Lógica principal do jogo
    while True:
        # Se houver um arquivo para carregar,
        # apenas faça!
        if common.status["actualfile"] and reset is False:
            game = common.loadscene(common.status["actualfile"]) # Jogo na memória

        elif common.status["nextfile"]:
            game = common.loadscene(common.status["nextfile"])

        # Já viu começar de outro lugar?
        # Claro que o index pra "folhear" a história
        # é justo do ponto zero!
        if reset is True:
            common.status["index"] = 0
            common.status["nextpart"] = None
            common.status["nextfile"] = None

        if common.config["clear_dialog"] is True:
            os.system(common.systemclear)

        while common.status["index"] < len(game[common.status["part"]]["dialogs"]):
            # Definir essa coisa pra não zoar
            # a minha vida, minha existência :D
            dialogs = game[common.status["part"]]["dialogs"]
            section = dialogs[common.status["index"]]
            dialog = section["text"]

            # Próxima parte para continuar
            nextpart = section.get("nextpart")

            # Checagem de personagens
            if common.status["index"] - 1 < 0:
                oldperson = None
            else:
                oldperson = dialogs[common.status["index"] - 1].get("person", None)

            # Personagem atual
            newperson = section.get("person", None)

            # Mecanismo de personagem
            if common.status["index"] == 0:
                print(f"[{newperson}]")

            elif reset is False and common.status["index"] > 0:
                print(f"[{newperson}]")

            elif oldperson and oldperson != newperson:
                # Cheque se o personagem anterior é diferente
                # ou igual ao atual. Se verdadeiro para diferente,
                # logo, exibir personagem diferente.
                #
                # Foi a parte mais legal do código, poxa :,)
                print(f"\n[{newperson}]")

            # Efeito de digitação 
            wait_var = float(section.get("waittime", -1.0))
            
            common.typingeffect(dialog, Wait=wait_var)

            # Se caso for uma pergunta
            if section.get("question", None) is True:
                common.status["nextpart"], common.status["nextfile"] = common.printchoices(section)

            else:
                common.status["nextpart"] = section.get("nextpart", None)
                common.status["nextfile"] = section.get("nextfile", None)

                if common.status["nextfile"]:
                    common.status["nextfile"] = common.status["nextfile"]

            # Próximo texto....
            common.status["index"] += 1 
            reset = True

        # Deseja que o jogo pause e continue com enter?
        # Não parece muito legal as vezes.
        # Só configurar e arrastar pra cima, pô!
        if common.config["pause_enter"] and not section.get("question"):
            input("\nPressione <ENTER> para continuar...")

        # A história apenas continua...
        if common.status["nextpart"]:
            # Afinal, a história não acaba, poxa.
            # Deixa rolar! Deixa ir pra outra parte!
            time.sleep(common.config["long_pause"])
            print() # Nova linha

            common.status["part"] = common.status["nextpart"]

        # O fim.
        # Na verdade, vou fazer disto aqui um loop futuro.
        # Ainda vou projetar esta parte
        if not common.status["nextfile"] and not common.status["nextpart"]:
            break
