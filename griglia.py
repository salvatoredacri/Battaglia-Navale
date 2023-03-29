from ship_class import navi, puo_inserire_nave
from standards import ship_list, numero_navi

def crea_griglia():
#richiesta delle dimensioni dellla griglia
    n_righe = int(input("Inserisci il numero di righe della griglia: "))
    n_colonne = int(input("Inserisci il numero di colonne della griglia: "))

    #creazione della griglia
    griglia = [[0] * n_colonne for _ in range(n_righe)]
   
    
    nome_nave = input("Inserisci il nome della nave: ")
    lunghezza_nave = None
    for ship in ship_list:
          if ship.nome == nome_nave:
           lunghezza_nave = ship.lunghezza
           print(f"La nave {nome_nave} ha lunghezza {lunghezza_nave}.")
           break
    if lunghezza_nave is None:
            print("Nome della nave non valido.")   
#richiesta all'utente di posizionare le navi
   for ship in ship_list:
        while True:
         stampa_griglia(griglia, n_righe, n_colonne)
         try:
          orientamento = str(input("Inserisci l'orientamento della nave (orizzontale o verticale): "))
          riga = int(input("Inserisci la riga in cui inserire la nave: "))
          colonna = int(input("Inserisci la colonna in cui inserire la nave: ")) 
          if Navi.puo_inserire_nave(ship.lunghezza, orientamento, riga, colonna, griglia): 
            Navi.inserisci_nave(ship.lunghezza, orientamento, riga, colonna, griglia)
            break
         except IndexError:
          print("Inserisci una coordinata valida. Riprova.")
    else:
         print("Non puoi inserire la nave qui. Riprova.")
             

    return griglia
