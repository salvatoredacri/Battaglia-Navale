from griglia import  *
from ship_class import Navi
from gioco import turno, vittoria
# from standards import lista_navi 
# from standards import lista_navi, lista_navi_2
from standards import lista_navi, lista_navi_2
# from standards import lista_navi


# Creo i giocatori
giocatore_1= str(input("Inserisci il nome del giocatore 1: "))
giocatore_2 = str(input("Inserisci il nome del giocatore 2: "))


#Creo le griglie dei due giocatori
dimensione = int(input("Inserisci la dimensione della griglia: "))   
griglia_giocatore_1 = crea_griglia(dimensione)
griglia_giocatore_2 = crea_griglia(dimensione)
griglia_colpi_1= crea_griglia(dimensione)
griglia_colpi_2= crea_griglia(dimensione)


player=[giocatore_1, giocatore_2]




# Giocatore 1 posiziona le tue navi!
print(player[0],", è il tuo turno!" "\n Posiziona le tue navi!")
griglia1 = posiziona_navi(griglia_giocatore_1, player[0], lista_navi)
print(griglia1)

# Giocatore 1 ha finito di posizionare le navi. Passa al turno del Giocatore 2.
input(f"Premi INVIO per passare al turno di {player[1]}")
stampa_griglia(griglia_giocatore_2, dimensione)


# # Giocatore 2 posiziona le tue navi!
print(player[1],", è il tuo turno!" "\n Posiziona le tue navi!")
griglia2 = posiziona_navi(griglia_giocatore_2, player[1], lista_navi_2)
print(griglia2)


# Inizia il gioco
fine_gioco = False
turno_giocatore = 0  # Indice del giocatore di turno

while not fine_gioco:
    print(f"{player[turno_giocatore]}, è il tuo turno! Attacca!")

    if turno_giocatore == 0:
        griglia_combattimento = griglia_giocatore_2
        griglia_colpi = griglia_colpi_1
        avversario = player[1]
        lista_navi_avversario = lista_navi_2

        
        
    else:
        griglia_combattimento = griglia_giocatore_1
        griglia_colpi = griglia_colpi_2
        avversario = player[0]
        lista_navi_avversario = lista_navi
        
        
        

    # Esegui il turno di attacco
    fine_gioco, griglia_colpi, griglia_combattimento= turno(griglia_combattimento, player[turno_giocatore], griglia_colpi, fine_gioco, lista_navi_avversario)
    

    
    # # Controlla la vittoria del giocatore
    # fine_gioco = vittoria(lista_navi_avversario)
     
    if not fine_gioco:
        input(f"Premi INVIO per passare al turno di {player[1-turno_giocatore]}")
        turno_giocatore = 1 - turno_giocatore
        
     

# # Fine del gioco, un giocatore ha vinto
vincitore = player[turno_giocatore]
print(f"{vincitore} ha vinto il gioco!")
