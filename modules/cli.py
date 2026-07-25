import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--credits",
        help="Mostra a introdução completa do programa",
        action="store_true"
    )

    return parser.parse_args()
