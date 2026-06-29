import os
import json
import sys
import time
import random

def printchoices(section):
    options = section["options"]

    # Você recebe as escolhas...
    for i, choice in enumerate(options):
        #typingeffect(config, f"[{i+1}] {options[i]["option"]}")
        print(f"[{i+1}] {options[i]["option"]}")

    while True:
        try:
            # Agora escolha por onde trilhar
            choice_player = int(input("> ")) - 1

            # A escolha foi sua! Presuma sua consequência!
            if choice_player >= 0 and choice_player < len(options):
                # Verificar se tem continuação no próximo arquivo...
                # Vire a página, filho!
                nextfile = options[choice_player].get("nextfile", None)

                # Se houver algo, apenas seguir o que manda
                # Se não houver nada, segue o padrão...
                nextpart = options[choice_player].get("nextpart", "start") 

                # Bora processar dados!
                break

        # Digite um número, seu boboca!
        except ValueError: 
            continue

    return nextpart, nextfile

def typingeffect(config, text, Wait=-1.0, NewLine=True):
    if not isinstance(NewLine, bool):
        raise TypeError("NewLine is not a boolean!")

    elif not isinstance(Wait, float):
        raise TypeError("Wait is not an int!")

    elif config["interval_min"] > config["interval_max"]:
        raise ValueError("Interval maximum is greater than interval minimum")

    for letter in text:
        print(letter, flush=True, end='')

        # -1 para desativado
        if Wait == -1.0:
            interval_gen = random.uniform(
                config["interval_min"],
                config["interval_max"]
                )

            time.sleep(interval_gen)

        else:
            time.sleep(Wait)

    if NewLine:
        print() # Nova linha

    time.sleep(config["pause_dialog"])

def detectclear():
    # Windows
    if os.name == "nt":
        system_clear = "cls"

    # Linux/MacOS
    else:
        system_clear = "clear"

    return system_clear

def loadfile(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return None

    except Exception as error:
        print("An error occured while access a file:", error)
        sys.exit(1)


def savefile(filepath, content):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(content, file, ensure_ascii=False, indent=4)

    except Exception as error:
        print("An error occured while writing a file:", error)
        sys.exit(1)
