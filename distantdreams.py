#!/usr/bin/env python3

# Arquivo: distantdreams.py
# Autor: GreenBoots
# Licença: GNU GPLv3
import os
import sys

from modules import banner
from modules import cli
from modules import common
from modules import engine

args = cli.main()

if args.credits is True:
    print(banner.banner_var)
    print(banner.warning_var)

    sys.exit()

def main():
    try:
        if common.config["skip_banner"] is False or common.config["first_time"] is True:
            banner.banner_main()

        if common.config["skip_warning"] is False or common.config["first_time"] is True:
            banner.warn_main()

        if common.config["first_time"]:
            while True:
                choice_banner = input("Deseja pular o banner na próxima vez? Y/N ")

                if choice_banner.upper() == "Y" or choice_banner.upper() == "S":
                    common.config["skip_banner"] = True
                    break

                elif choice_banner.upper() == "N":
                    common.config["skip_warning"] = False
                    break

            while True:
                choice_warn = input("Deseja pular o aviso na próxima vez? Y/N ")

                if choice_warn.upper() == "Y" or choice_warn.upper() == "S":
                    common.config["skip_warning"] = True
                    break

                elif choice_warn.upper() == "N":
                    common.config["skip_warning"] = False
                    break

        if common.config["first_time"] is True:
            common.config["first_time"] = False
            common.savefile(common.configpath, common.config)

        engine.main()

    except KeyboardInterrupt:
        os.system(common.systemclear)
        print("Jogo Fechado.")

        # Sistema de salvamento aqui
        if common.config["save"] is True:
            # Isto foi escrito para não causar problemas
            # de salvamento
            if common.status["index"] == len(game[common.status["part"]]["dialogs"]):
                common.status["index"] -= 1

            elif common.status["index"] < 0:
                common.status["index"] = 0

            common.savefile(common.savepath, common.status)
            print("O jogo foi salvo!")

if __name__ == "__main__":
    main()
