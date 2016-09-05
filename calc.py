#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################
#@Python - Calculatrice
#@Gaetan
#@date 05092016
###################

##      FONCTIONS       ##

def calculate(a, b, op):

    """Exécution du calcul"""

    if op == '1':
        return a + b

    elif op == '2':
        return a - b

    elif op == '3':
        return a * b

    elif op == '4':
        return a / b


##      Affichage console       ##


ops = ('Addition', 'Soustraction', 'Multiplication', 'Division')

print('\r\n[1]: {}'.format(ops[0]))
print('[2]: {}'.format(ops[1]))
print('[3]: {}'.format(ops[2]))
print('[4]: {}'.format(ops[3]))
print('\r\n[q]: Sortir')

op = str(input('\r\nChoisissez une opération: '))

while op.lower() != 'q':

    if int(op) < 1 or int(op) > 4:
        print('\r\nSaisi opération incorrect. Veuillez réessayer.')
        continue

    else:
        """Affichage du choix de calcul"""
        print('\r\n--- Vous avez choisi une {} ---'.format(ops[int(op) - 1]))

        """Choix des 2 chiffres"""
        a = int(input('\r\nChoix du 1er chiffre: '))
        b = int(input('\r\nChoix du 2ème chiffre: '))

    print('\r\n--- Le résultat est {} ---'.format(str(calculate(a, b, op))))

print("Bye bye !!")
