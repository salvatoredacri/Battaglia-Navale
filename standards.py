from ship_class import Navi
from griglia import *
import copy

portaerei=Navi("portaerei",5)
corazzata=Navi("corazzata",4)
incrociatore=Navi("incrociatore",3)
sottomarino=Navi("sottomarino",2)
cacciatorpediniere=Navi("cacciatorpediniere",1)
# Creazione della lista delle navi
lista_navi=[cacciatorpediniere,sottomarino,incrociatore,corazzata,portaerei]  
# Creazione di una copia profonda della lista delle navi
lista_navi_2= copy.deepcopy(lista_navi)

