#!/usr/bin/env python3

# Arquivo: distantdreams.py
# Autor: GreenBoots
# Licença: GNU GPLv3

from modules import engine
from modules import warning
from modules import banner
from modules import utils as util
from modules import vars as var

def main():
    if var.config["skip_banner"] is False or var.config["first_time"] is True:
        banner.main()

    if var.config["skip_warning"] is False or var.config["first_time"] is True:
        warning.main()

    if var.config["first_time"]:
        while True:
            choice_banner = input("Deseja pular o banner na próxima vez? Y/N ")

            if choice_banner.upper() == "Y" or choice_banner.upper() == "S":
                var.config["skip_banner"] = True
                break

            elif choice_banner.upper() == "N":
                var.config["skip_warning"] = False
                break

        while True:
            choice_warn = input("Deseja pular o aviso na próxima vez? Y/N ")

            if choice_warn.upper() == "Y" or choice_warn.upper() == "S":
                var.config["skip_warning"] = True
                break

            elif choice_warn.upper() == "N":
                var.config["skip_warning"] = False
                break

    if var.config["first_time"] is True:
        var.config["first_time"] = False
        util.savefile("config/config.json", var.config)

    engine.main()

if __name__ == "__main__":
    main()
