from griglia import crea_griglia, posiziona_navi, stampa_griglia
from ship_class import Navi

# Creo i giocatori
giocatore_1= str(input("Inserisci il nome del giocatore 1: "))
giocatore_2 = str(input("Inserisci il nome del giocatore 2: "))


#Creo le griglie dei due giocatori
dimensione = int(input("Inserisci la dimensione della griglia: "))   
griglia_giocatore_1 = crea_griglia(dimensione)
griglia_giocatore_2 = crea_griglia(dimensione)


ship_list=["cacciatorpediniere","sottomarino","incrociatore","corazzata","portaerei"]
ship_length=[1,2,3,4,5]
player=[giocatore_1, giocatore_2]
griglia_avversario_1 = griglia_giocatore_2
griglia_avversario_2 = griglia_giocatore_1


# Giocatore 1 posiziona le tue navi!
print(player[0],", è il tuo turno!" "\n Posiziona le tue navi!")
griglia1 = posiziona_navi(ship_list, ship_length, griglia_giocatore_1, giocatore=player[0])
print(griglia1)

# Giocatore 1 ha finito di posizionare le navi. Passa al turno del Giocatore 2.
input(f"Premi INVIO per passare al turno di {player[1]}")
stampa_griglia(griglia_giocatore_2, dimensione)


# Giocatore 2 posiziona le tue navi!
print(player[1],", è il tuo turno!" "\n Posiziona le tue navi!")
griglia2 = posiziona_navi(ship_list, ship_length, griglia_giocatore_2, giocatore=player[1])
print(griglia2)
