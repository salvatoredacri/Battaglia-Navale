from griglia import *


def turno(griglia_combattimento, giocatore, griglia_colpi, fine_gioco, lista_navi): 
    """
    Esegue un turno di gioco per il giocatore corrente.

    Argomenti:
    - griglia_combattimento: la griglia di gioco del giocatore avversario
    - giocatore: il nome del giocatore corrente
    - griglia_colpi: la griglia dei colpi effettuati dal giocatore corrente
    - fine_gioco: flag che indica se il gioco è terminato
    - lista_navi: la lista delle navi in gioco

    Ritorno:
    - fine_gioco: flag che indica se il gioco è terminato
    - griglia_colpi: la griglia dei colpi effettuati dal giocatore corrente
    - griglia_combattimento: la griglia di gioco del giocatore avversario

    """
    fine_turno = False
    print(giocatore, "Ecco la tua griglia dei colpi effettuati")
    stampa_griglia(griglia_colpi, len(griglia_colpi))
    print(giocatore, "inserisci le coordinate dove vuoi sparare")

    while not fine_turno:
        try:
         riga = int(input("Inserisci la riga di dove vuoi sparare (1-9): "))
         if riga < 0 or riga > len(griglia_combattimento):
            print("Coordinate non valide. Inserisci coordinate valide.")
        except ValueError:
         print('Inserisci un numero valido') 
         continue
        try:    
         colonna = int(input("Inserisci la colonna di dove vuoi sparare (1-9): "))
         if colonna < 0 or colonna > len(griglia_combattimento):
            print("Coordinate non valide. Inserisci coordinate valide.")
        except ValueError:     
         print('Inserisci un numero valido')
         continue

        if griglia_colpi[riga][colonna] != 0:
            print("Hai già sparato in questa posizione. Riprova.")
            continue

        hit = False
        
        for nave in lista_navi:
            if nave.check_hit(riga, colonna,griglia_combattimento):
                print("Hai colpito una nave!")
                hit = True
                griglia_colpi[riga][colonna] = "c"
                nave.is_hit(riga,colonna,griglia_combattimento)
                if nave.is_sunk():
                    print("Hai affondato una nave!",nave.nome)
                    if all(n.is_sunk() for n in lista_navi):
                        fine_gioco = vittoria(lista_navi)  # Tutte le navi sono affondate, fine del gioco
                break

        if not hit:
            print("Hai sparato in acqua.")
            griglia_colpi[riga][colonna] = "-"

        fine_turno = True
        print("\nGriglia dei colpi:")
        stampa_griglia(griglia_colpi, len(griglia_colpi))

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
        if not nave.is_sunk():
            return False
    return True








           
