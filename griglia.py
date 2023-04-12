from ship_class import Navi, inserisci_nave


def crea_griglia(dimensione):
#richiesta delle dimensioni dellla griglia
   griglia = [[0] * dimensione for _ in range(dimensione)]
   stampa_griglia(griglia, dimensione)
   return griglia


def posiziona_navi(ship_list, ship_length, griglia, giocatore):
    i = 1
    while i <= 5:
        nave = Navi(ship_list[i-1], ship_length[i-1]) 
        print(giocatore, f",inserisci la nave: {ship_list[i-1]} di lunghezza: {ship_length[i-1]} ")
        orientamento = input("Inserisci l'orientamento della nave (orizzontale/verticale): ")
        # #controllo che l'orientamento sia corretto
        if orientamento != "orizzontale" and orientamento != "verticale":
            print("Orientamento non valido. Riprova.")
            continue
        # # chiedo la riga
        riga = int(input("Inserisci la riga in cui inserire la nave: "))
        # # controllo che la riga sia corretta
        if riga < 0 or riga > len(griglia)-1:
         print(f"Riga non valida. Inserisci un numero da 0 a {len (griglia)-1} Riprova.")
         continue
        # controllo che rientri nella griglia
        # chiedo la colonna
        colonna = int(input("Inserisci la colonna in cui inserire la nave: "))
        # controllo che la colonna sia corretta
        if colonna < 0 or colonna > len(griglia)-1:
         print(f"Colonna non valida. Inserisci un numero da 0 a {len(griglia)-1} Riprova.")
         continue
         
         # inserisco la nave nella griglia del giocatore 
        griglia_giocatore = inserisci_nave(nave, orientamento, riga, colonna, griglia)
        if griglia_giocatore != False:
            i+=1
            stampa_griglia(griglia_giocatore, len(griglia))
            print("\n\nEcco la tua griglia con le navi posizionate:")
    return stampa_griglia(griglia_giocatore, len(griglia))   
        
          
 
    
    
        
       

def stampa_griglia(griglia,dimensione):
    print("\n  " + " ".join(str(x) for x in range(1, dimensione + 1)))
    for r in range(dimensione):
        print(str(r + 1) + " " + " ".join(str(c) for c in griglia[r]))
    print()

