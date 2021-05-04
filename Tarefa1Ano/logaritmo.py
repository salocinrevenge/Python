import argparse
import math


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numero", help="Número para calcular o logaritmo.", type=float)
    parser.add_argument("-b", "--base", help="base do logaritmo.", default=10.0, type=float)

    args = parser.parse_args()

    resultado = math.log(args.numero, args.base)

    print(resultado)


main()
