from ship_class import navi, puo_inserire_nave
from standards import ship_list, numero_navi

def crea_griglia():
#richiesta delle dimensioni dellla griglia
    n_righe = int(input("Inserisci il numero di righe della griglia: "))
    n_colonne = int(input("Inserisci il numero di colonne della griglia: "))

    #creazione della griglia
    griglia = [[0] * n_colonne for _ in range(n_righe)]
#richiesta all'utente di posizionare le navi
    for ship in ship_list:
     print("Inserisci le navi di nome {ship.nome}(lunghezza {lunghezza.lunghezza})")
    for i in range(numero_navi[ship]):
     while True:
         orientamento = input("Inserisci l'orientamento della nave (orizzontale o verticale): ")
         riga = int(input("Inserisci la riga in cui inserire la nave: "))
         colonna = int(input("Inserisci la colonna in cui inserire la nave: "))
         if puo_inserire_nave(ship.lunghezza, orientamento, riga, colonna):
             break
         else:
             print("Non puoi inserire la nave qui. Riprova.")
    return griglia