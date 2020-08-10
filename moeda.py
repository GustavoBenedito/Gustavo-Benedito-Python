from random import random

print("jogue a moeda ai carai ")


def joga_moeda():
    # gerar um valor entre 0 a 1 para girar a moeda
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'


print(joga_moeda())
