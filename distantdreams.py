#!/usr/bin/env python3

# Arquivo: distantdreams.py
# Autor: GreenBoots
# Licença: GNU GPLv3

import time

from modules import engine, warning, utils, banner
from modules.vars import config

def main():
    if config["skip_banner"] is False or config["first_time"] is True:
        banner.main()

    if config["skip_warning"] is False or config["first_time"] is True:
        warning.main()

    if config["first_time"]:
        while True:
            choice_banner = input("Deseja pular o banner na próxima vez? Y/N ")

            if choice_banner.upper() == "Y" or choice_banner.upper() == "S":
                config["skip_banner"] = True
                break

            elif choice_banner.upper() == "N":
                config["skip_warning"] = False
                break

        while True:
            choice_warn = input("Deseja pular o aviso na próxima vez? Y/N ")

            if choice_warn.upper() == "Y" or choice_warn.upper() == "S":
                config["skip_warning"] = True
                break

            elif choice_warn.upper() == "N":
                config["skip_warning"] = False
                break

    if config["first_time"] is True:
        config["first_time"] = False
        utils.savefile("config/config.json", config)

    engine.main()

if __name__ == "__main__":
    main()
