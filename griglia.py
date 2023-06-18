
import string
from standards import *
import re


def crea_griglia(dimensione):
  """
    Crea una griglia di gioco vuota con le dimensioni specificate.

    Argomenti:
    - dimensione: la dimensione della griglia (numero di righe e colonne)

    Ritorno:
    - griglia: la griglia di gioco creata

    """
  griglia = [[0] * dimensione for _ in range(dimensione)]

  return griglia




def stampa_griglia(griglia): #stampa la griglia di gioco a video
    dimensione = len(griglia)
    #stampa header della griglia con le lettere corrispondenti nelle colonne
    print("\n  " + " ".join(chr(ord('A') + c) for c in range(dimensione)))
    for r in range(dimensione):
        #converte i valori della riga in stringhe
        riga = [str(c) for c in griglia[r]]
        #stampa un valore crestente alla riga in base alla dimensione
        print(str(r + 1) + " " + " ".join(riga))
    print()

def puo_inserire_nave(nave, orientamento, riga, colonna, griglia):

    """
    Verifica se è possibile inserire una nave in una determinata posizione sulla griglia.

    Argomenti:
    - nave: l'oggetto Nave da inserire
    - orientamento: l'orientamento della nave ("orizzontale" o "verticale")
    - riga: la riga in cui posizionare la nave
    - colonna: la colonna in cui posizionare la nave
    - griglia: la griglia di gioco

    Ritorno:
    - True se è possibile inserire la nave nella posizione specificata, False altrimenti

    """
    if orientamento == "orizzontale" or orientamento == "o":
        # Controllo se la nave entra nella griglia considerando la sua lunghezza
        if colonna + nave.lunghezza > len(griglia[0]):
            print("La nave non entra in questa posizione. Riprova")
            return False
        # Itero attraverso la lunghezza della nave
        for i in range(nave.lunghezza):
            # Controllo che non sia sopra un'altra nave
            if griglia[riga][colonna + i] != 0:
                print("In queste coordinate è già presente un'altra nave. Riprova")
                return False
            # Controllo che sopra non abbia niente se non mi trovo sulla prima riga
            if riga > 0 and griglia[riga - 1][colonna + i] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
            
            # Controllo che sotto non abbia niente se non mi trovo sull'ultima riga
            if riga < len(griglia) - 1 and griglia[riga + 1][colonna + i] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
           
            # Controllo sinistra se non sono sul bordo sinistro
            if colonna + i > 0 and griglia[riga][colonna + i - 1] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
           
            # Controllo destra se non sono sul bordo destro
            if colonna + i < nave.lunghezza - 1 and griglia[riga][colonna + i + 1] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
            
    elif orientamento == "verticale" or orientamento == "v":
        # Controllo se la nave entra nella griglia considerando la sua lunghezza
        if riga + nave.lunghezza > len(griglia[0]):
            print("La nave non entra in questa posizione")
            return False
        # Itero attraverso la lunghezza della nave
        for i in range(nave.lunghezza):
          # controllo che non sia sopra un'altra nave
            if griglia[riga + i][colonna] != 0:
                print("In queste coordinate è già presente un'altra nave. Riprova")
                return False
            
            # Controllo che sopra non abbia niente se non mi trovo sulla prima colonna
            if colonna > 0 and griglia[riga + i][colonna - 1] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False 
            
            # Controllo che non ci sia una nave sotto, a meno che mi trovi sull'ultima colonna
            if colonna < len(griglia) - 1 and griglia[riga + i][colonna + 1] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
            
            # Controllo che non ci sia una nave a sinistra, a meno che mi trovi sulla prima riga
            if i > 0 and griglia[riga + i - 1][colonna] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
            
            # Controllo che non ci sia una nave a destra se non mi trovo sull'ultima riga
            if i < nave.lunghezza - 1 and griglia[riga + i + 1][colonna] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
            
    else:
        raise ValueError("Orientamento non valido. Usare 'orizzontale' o 'verticale'.")
    
    return True
 
def inserisci_nave(nave, orientamento, riga_iniz, colonna_iniz, griglia): 
    """
    Inserisce una nave nella griglia di gioco nella posizione specificata.

    Argomenti:
    - nave: l'oggetto Nave da inserire
    - orientamento: l'orientamento della nave ("orizzontale" o "verticale")
    - riga_iniz: la riga iniziale in cui posizionare la nave
    - colonna_iniz: la colonna iniziale in cui posizionare la nave
    - griglia: la griglia di gioco

    Ritorno:
    - Se la nave può essere inserita:
        - griglia: la griglia di gioco aggiornata con la nave inserita
        - coordinate: una lista di tuple che rappresentano le coordinate della nave sulla griglia
    - Se la nave non può essere inserita, restituisce False

    """
    if puo_inserire_nave(nave, orientamento, riga_iniz, colonna_iniz, griglia):
        coordinate =[]
        if orientamento == "orizzontale" or orientamento == "o":
            for i in range(nave.lunghezza):
                griglia[riga_iniz][colonna_iniz + i] = 1
                coordinate.append((riga_iniz,colonna_iniz+i))
        elif orientamento == "verticale" or orientamento == "v":
            for i in range(nave.lunghezza):
                griglia[riga_iniz + i][colonna_iniz] = 1
                coordinate.append((riga_iniz+i,colonna_iniz))
        print("\nNave inserita correttamente:")
        return griglia, coordinate
    else:
        return False
                     




def posiziona_navi(griglia, giocatore, lista_navi):
    """
    Posiziona le navi nella griglia del giocatore.

    Argomenti:
    - griglia: la griglia di gioco del giocatore
    - giocatore: il nome del giocatore corrente
    - lista_navi: la lista delle navi scelte da posizionare

    Valore di ritorno:
    - La griglia di gioco del giocatore con le navi posizionate
    - La lista delle navi_posizionate sulla griglia di gioco 

    """
    navi_posizionate=[]
    quantita_navi = len(lista_navi)
    for nave in lista_navi:
        
            print(f"{giocatore}, inserisci la nave: {nave.nome} di lunghezza: {nave.lunghezza}")
            
            colonne_valide = string.ascii_uppercase[:len(griglia)]    
            while True:
                posizione = input("Inserisci le coordinate della nave (es. A1): ")
                if not posizione:
                    print("Inserire un valore corretto (es. A1)")
                    continue
                if not re.match("^[A-Za-z][0-9]+$", posizione):
                    print("Errore: caratteri speciali non consentiti.")
                    continue
                colonna_iniz = posizione[0].upper()
                riga_iniz = int(posizione[1:])
                if colonna_iniz not in colonne_valide or riga_iniz < 1 or riga_iniz > len(griglia):
                    print("Coordinate non valide. Riprova.")
                    continue

                orientamento = input("Inserisci l'orientamento della nave ('o' per orizzontale, 'v' per verticale): ")
                orientamento = orientamento.lower()
                if orientamento != 'o' and orientamento !='orizzontale' and orientamento != 'v' and orientamento != 'verticale':
                    print("Orientamento non valido. Riprova.")
                    continue

                result = inserisci_nave(nave, orientamento, riga_iniz - 1, colonne_valide.index(colonna_iniz), griglia)
                if result != False:
                    griglia_giocatore, coordinate = result
                    nave_posizionata = Navi(nave.nome, nave.lunghezza, orientamento, riga_iniz -1, colonne_valide.index(colonna_iniz), coordinate)
                    clear_console()
                    stampa_griglia(griglia_giocatore)
                    print("\n\nEcco la tua griglia con le navi posizionate:")
                    navi_posizionate.append(nave_posizionata)
                    
                    break
    
    return stampa_griglia(griglia_giocatore), navi_posizionate
