from . import utils
from .vars import config

warning = """
ATENÇÃO!
Devido o jogo usar efeitos psicológicos que podem desencadear profundas reações,
recomendamos caso haja algum histórico de transtornos mentais, favor evitar a visualização do conteúdo.
Para algumas pessoas mais sensíveis, se haver desconforto intenso, ansiedade, sinais de angústia,
favor evitar o conteúdo do programa.

Pessoas com traumas recentes, depressão, ansiedade devem evitar a visualização do jogo também.
"""

def main(): 
    utils.typingeffect(config, warning, Wait=0.025)

    input("Pressione <ENTER> para continuar...")
    print()
