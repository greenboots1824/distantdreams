#!/usr/bin/env python3

# Arquivo: distantdreams.py
# Autor: GreenBoots
# Licença: GNU GPLv3

from modules import engine, warning, utils, banner
import time

setting = utils.loadfile("settings.json")

def main():
    if setting["skip_banner"] is False:
        banner.main()

    if setting["skip_warning"] is False:
        warning.main()

    engine.main("scenes/intro.json")

if __name__ == "__main__":
    main()
