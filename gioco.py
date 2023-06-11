from griglia import *
import os
import time
from standards import *


def turno(griglia_combattimento, giocatore, griglia_colpi, fine_gioco, lista_navi, modalita): 
    
    """
    Esegue un turno di gioco per il giocatore corrente.

    Argomenti:
    - griglia_combattimento: la griglia di gioco del giocatore avversario
    - giocatore: il nome del giocatore corrente
    - griglia_colpi: la griglia dei colpi effettuati dal giocatore corrente
    - fine_gioco: flag che indica se il gioco è terminato
    - lista_navi: la lista delle navi in gioco
    - modalita: la modalità di gioco (0 o 1)

    Ritorno:
    - fine_gioco: flag che indica se il gioco è terminato
    - griglia_colpi: la griglia dei colpi effettuati dal giocatore corrente
    - griglia_combattimento: la griglia di gioco del giocatore avversario

    """
    fine_turno = False
    

    while not fine_turno:
        clear_console()
        print(giocatore, "Ecco la tua griglia dei colpi effettuati")
        stampa_griglia(griglia_colpi)
        print(giocatore, "inserisci le coordinate dove vuoi sparare")
        
    
      
        colonne_valide = string.ascii_uppercase[:len(griglia_combattimento)]
       
        while True:
            coordinate_colpo = input('Inserisci le coordinate di dove vuoi sparare (es. A1):')
            if not coordinate_colpo:
                     print('Inserire un valore corretto (es. A1)')
                     continue
            if not re.match("^[A-Za-z][0-9]+$", coordinate_colpo):
                     print("Errore: caratteri speciali non consentiti.")
                     continue
            colonna = coordinate_colpo[0].upper()
            

            riga = int(coordinate_colpo[1:])-1 
               
            if colonna not in colonne_valide or riga < 0 or riga > len(griglia_combattimento):
                     print("Coordinate non valide. Riprova.")
                     continue
            break
            
        colonna = colonne_valide.index(colonna) 
            
        if griglia_colpi[riga][colonna] != 0:
         print("Hai già sparato in questa posizione. Riprova.")
         continue

        colpo = False
        
        for nave in lista_navi:
            if nave.colpita(riga,colonna):
                print("Hai colpito una nave!")
                colpo = True
                griglia_colpi[riga][colonna] = "c"
                
                if nave.affondata():
                    print("Hai affondato una nave!",nave.nome)
                    if all(n.affondata() for n in lista_navi):
                        fine_gioco = vittoria(lista_navi)  # Tutte le navi sono affondate, fine del gioco
                        break
       
       
        if colpo and modalita == 0:
             
              print("\nGriglia dei colpi:")
              stampa_griglia(griglia_colpi)
              print('Puoi sparare ancora')
              time.sleep(4)

        elif not colpo and modalita == 0:
              print("Hai sparato in acqua.")
              griglia_colpi[riga][colonna] = "-"
              fine_turno = True
        else:
            if not colpo and modalita == 1:
             print("Hai sparato in acqua.")
             griglia_colpi[riga][colonna] = "-"
             fine_turno = True
            elif colpo and modalita == 1:
               fine_turno = True
               
        
        if fine_gioco:
           break 
        
        print("\nGriglia dei colpi:")
        stampa_griglia(griglia_colpi)

    return fine_gioco, griglia_colpi, griglia_combattimento

def vittoria(lista_navi): 
    """
    Determina se tutte le navi nella lista sono state affondate.

    Argomenti:
    - lista_navi: Una lista delle navi nel gioco.

    Valore di ritorno:
    - True se tutte le navi sono state affondate, False altrimenti.
    """
    for nave in lista_navi:
        if not nave.affondata():
            return False
    return True








           
