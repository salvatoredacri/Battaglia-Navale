
import string
import os


def crea_griglia(dimensione):
  """
    Crea una griglia di gioco vuota con le dimensioni specificate.

    Argomenti:
    - dimensione: la dimensione della griglia (numero di righe e colonne)

    Ritorno:
    - griglia: la griglia di gioco creata

    """
  griglia = [[0] * dimensione for _ in range(dimensione)]
#   stampa_griglia(griglia, dimensione)
  return griglia




def stampa_griglia(griglia, dimensione):
    print("\n  " + " ".join(chr(ord('A') + c) for c in range(dimensione)))
    for r in range(dimensione):
        riga = [str(c) for c in griglia[r]]
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
    if orientamento == "orizzontale":
        # Controllo se entra
        if colonna + nave.lunghezza > len(griglia[0]):
            print("La nave non entra in questa posizione. Riprova")
            return False
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
            
    elif orientamento == "verticale":
        # Controllo se entra
        if riga + nave.lunghezza > len(griglia[0]):
            print("La nave non entra in questa posizione")
            return False
        for i in range(nave.lunghezza):
          # controllo che non sia sopra un'altra nave
            if griglia[riga + i][colonna] != 0:
                print("In queste coordinate è già presente un'altra nave. Riprova")
                return False
            
           # 
            if colonna > 0 and griglia[riga + i][colonna - 1] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False 
            
            #
            if colonna < len(griglia) - 1 and griglia[riga + i][colonna + 1] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
      
            if i > 0 and griglia[riga + i - 1][colonna] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
      
            if i < nave.lunghezza - 1 and griglia[riga + i + 1][colonna] != 0:
                print("c'è una nave nelle vicinanze di questa posizione")
                return False
            
    else:
        raise ValueError("Orientamento non valido. Usare 'orizzontale' o 'verticale'.")
    
    return True
 
def inserisci_nave(nave, orientamento, riga, colonna, griglia): 
    """
    Inserisce una nave nella griglia di gioco nella posizione specificata.

    Argomenti:
    - nave: l'oggetto Nave da inserire
    - orientamento: l'orientamento della nave ("orizzontale" o "verticale")
    - riga: la riga in cui posizionare la nave
    - colonna: la colonna in cui posizionare la nave
    - griglia: la griglia di gioco

    Ritorno:
    - Se la nave può essere inserita:
        - griglia: la griglia di gioco aggiornata con la nave inserita
        - coordinate: una lista di tuple che rappresentano le coordinate della nave sulla griglia
    - Se la nave non può essere inserita, restituisce False

    """
    if puo_inserire_nave(nave, orientamento, riga, colonna, griglia):
        coordinate =[]
        if orientamento == "orizzontale":
            for i in range(nave.lunghezza):
                griglia[riga][colonna + i] = 1
                coordinate.append((riga,colonna+i))
        elif orientamento == "verticale":
            for i in range(nave.lunghezza):
                griglia[riga + i][colonna] = 1
                coordinate.append((riga+i,colonna))
        print("\nNave inserita correttamente:")
        # nave.coordinate = coordinate
        # print(coordinate)
        return griglia, coordinate
    else:
        return False
                     
  



 

def posiziona_navi(griglia, giocatore, lista_navi):
    """
    Posiziona le navi sulla griglia del giocatore.

    Argomenti:
    - griglia: la griglia in cui posizionare le navi (lista di liste)
    - giocatore: il nome del giocatore (stringa)
    - lista_navi: la lista delle navi da posizionare (lista di oggetti Nave)

    Ritorno:
    - None

    """
    i = 0    
    while i < 5:
        
        nave = lista_navi[i]
        print(f"{giocatore}, inserisci la nave: {nave.nome} di lunghezza: {nave.lunghezza}")
        orientamento = input("Inserisci l'orientamento della nave (orizzontale/verticale): ")
        
        # Controllo che l'orientamento sia corretto
        if orientamento != "orizzontale" and orientamento != "verticale":
            print("Orientamento non valido. Riprova.")
            continue
        
    
        # Chiedo la colonna
        colonne_valide = string.ascii_uppercase[:len(griglia)]
        colonna = input("Inserisci la lettera della colonna in cui vuoi posizionare la nave (es.A):  ")
        colonna = colonna.upper()
        # Controllo che la colonna sia corretta
        if colonna not in colonne_valide:
            print(f"Lettera non valida. Inserisci una lettera da A a {colonne_valide[-1]}. Riprova.")
            continue

        # Chiedo la riga
        riga = int(input("Inserisci il numero della riga in cui vuoi inserire la nave (es.1): "))
        
        # Controllo che la riga sia corretta
        if riga < 1 or riga > len(griglia):
            print(f"Numero non valido. Inserisci nemero valido, da 1 a {len(griglia)}. Riprova.")
            continue
        
        # Inserisco la nave nella griglia del giocatore 
        result = inserisci_nave(nave, orientamento, riga - 1, colonne_valide.index(colonna), griglia)
        
        if result != False:
            griglia_giocatore, coordinate = result
            nave.coordinate = coordinate
            i += 1
            os.system('cls')
            stampa_griglia(griglia_giocatore, len(griglia))
            print("\n\nEcco la tua griglia con le navi posizionate:")
            
     
    return stampa_griglia(griglia_giocatore, len(griglia_giocatore))



