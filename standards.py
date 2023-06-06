from ship_class import Navi
from griglia import *
import copy
import argparse
import sys

portaerei=Navi("portaerei",5)
corazzata=Navi("corazzata",4)
incrociatore=Navi("incrociatore",3)
sottomarino=Navi("sottomarino",2)
cacciatorpediniere=Navi("cacciatorpediniere",1)
# Creazione della lista delle navi
lista_navi=[cacciatorpediniere,sottomarino,incrociatore,corazzata,portaerei]  
# Creazione di una copia profonda della lista delle navi
lista_navi_2= copy.deepcopy(lista_navi)

#Creazione argParser
parser = argparse.ArgumentParser()
parser.add_argument("-g1","--giocatore_1", type=str,default='giocatore_1', help='Nome del giocatore 1')
parser.add_argument("-g2", "--giocatore_2", type=str,default='giocatore_2', help='Nome del giocatore 2')
parser.add_argument("-d","--dimensione", type=int, default=9, help='Dimensione della griglia')
args = parser.parse_args()



def controllo_parser(args):
    try:
        controllo_arguments(args)
    except ValueError:
        sys.exit()


def controllo_arguments(args):
    if not 7 < args.dimensione < 15:
        print('\u001b[31mDimensione errata\033[0m')
        raise ValueError
 