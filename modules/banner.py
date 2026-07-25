from . import common

banner_var = r""" _____  _     _              _     _____
|  __ \(_)   | |            | |   |  __ \
| |  | |_ ___| |_ __ _ _ __ | |_  | |  | |_ __ ___  __ _ _ __ ___  ___
| |  | | / __| __/ _` | '_ \| __| | |  | | '__/ _ \/ _` | '_ ` _ \/ __|
| |__| | \__ \ || (_| | | | | |_  | |__| | | |  __/ (_| | | | | | \__ \
|_____/|_|___/\__\__,_|_| |_|\__| |_____/|_|  \___|\__,_|_| |_| |_|___/

Copyright (C) 2026, GreenBoots
LICENSE: GNU General Public License v3.0

Github: https://github.com/greenboots1824
Email: whoismeifthemynameisocult@proton.me
"""

warning_var = """ATENÇÃO!
Devido o jogo usar efeitos psicológicos que podem desencadear profundas reações,
recomendamos caso haja algum histórico de transtornos mentais, favor evitar a visualização do conteúdo.

Para algumas pessoas mais sensíveis, se haver desconforto intenso, ansiedade, sinais de angústia,
favor evitar o conteúdo do programa.

Pessoas com traumas recentes, depressão, ansiedade devem evitar a visualização do jogo também."""

def banner_main():
    print(banner_var)

def warn_main(): 
    common.typingeffect(warning_var, Wait=0.020)

    input("Pressione <ENTER> para continuar...")
    print()
