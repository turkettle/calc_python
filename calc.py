#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################
#@Python - Calculatrice
#@Gaetan
#@date 05092016
###################

print '1: Addition'
print '2: Soustraction'
print '3: Multiplication'
print '4: Division'
print 'q: Sortir'

while 1:
    op = input('Choisissez une opération: ')
    if op == 'q':
        print("Fin de la boucle")
        break

op = input('Choisissez une opération: ')
a = 1
b = 2
print op

if op == '1':
    print 'bibi'
    print a + b
