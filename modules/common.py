import os
import json
import sys
import time
import random
import shutil
from pathlib import Path

p = Path(__file__).resolve().parent

while not (p / "modules").exists():
    p = p.parent

WORKING_DIR = p

# Deixando variáveis estáticas aqui
startfile = "intro"
configpath = WORKING_DIR / "config/config.json"
defaultconfigpath = WORKING_DIR / "config/defaultconfig.json"

# Estado do jogo
status = {
    "part" : "start",
    "actualfile": None,
    "nextpart": None,
    "nextfile": None,
    "print_name": None,
    "index": 0
}

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

def typingeffect(text, Wait=-1.0, NewLine=True):
    try:
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

    except Exception as error:
        print("An error occured while the program has been typing:", error)
        sys.exit(1)

def detectclear():
    # Windows
    if os.name == "nt":
        system_clear = "cls"

    # Linux/MacOS
    else:
        system_clear = "clear"

    return system_clear

def loadfile(filepath):
    try:
        if filepath is None:
            raise ValueError("Not null value allowed")

        with open(filepath, "r", encoding="utf-8") as content:
            return json.load(content)

    except Exception as error:
        print("An error occured while access a file:", error)
        sys.exit(1)

def loadscene(filepath):
    try:
        if filepath is None:
            raise ValueError("Not null value allowed")

        filepath = WORKING_DIR / "scenes" / f"{filepath}.json"

        with open(filepath, "r", encoding="utf-8") as contentjson:
            return json.load(contentjson)

    except Exception as error:
        print("An error occured while access a scene file:", error)
        sys.exit(1)

def savefile(filepath, content):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(content, file, ensure_ascii=False, indent=4)

    except Exception as error:
        print("An error occured while writing a file:", error)
        sys.exit(1)

def createconfig(configpath):
    defaultconfig = loadfile(defaultconfigpath)
    savefile(configpath, defaultconfig)

def resetconfig(configpath):
    # Autocarregar arquivo de configuração
    # padrão para uso
    testconfig = Path(configpath)

    if not testconfig.exists() and not testconfig.is_file():
        # Se config.json não existir e nem for um arquivo
        # Criar uma nova baseada em defaultconfig.json
        createconfig(configpath)

    elif testconfig.is_dir():
        while True:
            print("Foi detectado que há uma pasta no lugar de config.json")
            answer = input("Deseja deletar? Y/N ")

            if answer.upper() == "Y" or answer.upper() == "S":
                shutil.rmtree(configpath)
                createconfig(configpath)
                break

            elif answer.upper() == "N":
                print("OK! Apague manualmente para o jogo voltar a funcionar!")
                sys.exit(0)

# Variáveis que dependem de funções
resetconfig(configpath)

config = loadfile(configpath)
savepath = WORKING_DIR / f"state/{config["savename"]}.json"

systemclear = detectclear()

savefile = loadfile(savepath)
