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

    if op == 1:
        return a + b

    elif op == 2:
        return a - b

    elif op == 3:
        return a * b

    elif op == 4:
        return a / b

def launch_prompt():
    """Affiche la ère étape du programme"""

    print('\r\n[1]: {}'.format(ops[0]))
    print('[2]: {}'.format(ops[1]))
    print('[3]: {}'.format(ops[2]))
    print('[4]: {}'.format(ops[3]))
    print('\r\n[q]: Sortir')

    return str(raw_input('\r\nChoisissez une opération: '))

def exec_application(op):
    """Traite les données envoyées par l'utilisateur"""

    while op.lower() != 'q':

        try:
            op = int(op)
        except ValueError:
            print('\r\n--- Saisi opération incorrect. Veuillez réessayer ---')
            op = str(launch_prompt())
            continue


        if int(op) < 1 or int(op) > 4:
            print('\r\n--- Saisi opération incorrect. Veuillez réessayer ---')
            op = str(launch_prompt())
            continue

        # else:
        """Affichage du choix de calcul"""
        print('\r\n--- Vous avez choisi une {} ---'.format(ops[int(op) - 1]))

        """Choix des 2 chiffres"""
        a = int(input('\r\nChoix du 1er chiffre: '))
        b = int(input('\r\nChoix du 2ème chiffre: '))

        print('\r\n--- Le résultat est {} ---'.format(str(calculate(a, b, op))))
        op = str(launch_prompt())

    print("Bye bye !!")


##      Affichage console       ##

try:
    ops = ('Addition', 'Soustraction', 'Multiplication', 'Division')
    op = str(launch_prompt())
    exec_application(op)

except KeyboardInterrupt:
    """Capture l'erreur si l'utilisateur ferme le programme avec Ctrl+C"""
    print '\r\n'
    pass
