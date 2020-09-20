# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:56:29 2020

@author: matheus
"""
def busca_binaria(lista, item):

    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:

        meio = (esquerda + direita) // 2 

        if lista[meio] == item:
            return meio
        elif item < lista[meio]:
            direita = meio - 1
        elif item > meio:
            esquerda = meio + 1

    return -1


lista = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
         ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,
         191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,
         281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397]

item = int(input("Elemento a ser buscado: "))

localizacao = busca_binaria(lista, item)

if localizacao == -1:
    print("Elemento não encontrado.")
else:
    print("Localização na posição: " + str(localizacao) + " da lista.")
    


