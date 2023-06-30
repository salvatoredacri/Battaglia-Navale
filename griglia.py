from standards import *
from enum import Enum
from ship_class import *

class StatoCella(Enum):
    VUOTA = 0     #Stato di una cella vuota
    COLPITA = 'c' #Stato di una cella rappresentante una nave colpita
    ACQUA = '-'    #Stato di una cella rappresentante un colpo mancato 
    NAVE = '>'    #Stato di una cella rappresentante una nave nella griglia di gioco



def crea_griglia(dimensione):
  """
    Crea una griglia di gioco vuota con le dimensioni specificate.

    Argomenti:
    - dimensione: la dimensione della griglia (numero di righe e colonne)

    Ritorno:
    - griglia: la griglia di gioco creata

    """
  griglia = [[StatoCella.VUOTA] * dimensione for _ in range(dimensione)]

  return griglia




def stampa_griglia(griglia): #stampa la griglia di gioco a video
    dimensione = len(griglia)
    #stampa header della griglia con le lettere corrispondenti nelle colonne
    print("\n  " + " ".join(chr(ord('A') + c) for c in range(dimensione)))
    for r in range(dimensione):
        #converte i valori della riga in stringhe
        riga = [str(c.value) for c in griglia[r]]
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
    if orientamento == OrientamentoNave.ORIZZONTALE.value:
        # Verifica se la nave supera i limiti della griglia in orizzontale
        if colonna + nave.lunghezza > len(griglia[0]):
            print("La nave non entra in questa posizione. Riprova")
            return False
        
        for i in range(nave.lunghezza):
            # Verifica se la cella è occupata da un'altra nave
            if griglia[riga][colonna + i] != StatoCella.VUOTA:
                print("In queste coordinate è già presente un'altra nave. Riprova")
                return False
            
            # Verifica se c'è una nave sopra la posizione desiderata
            if riga > 0 and griglia[riga - 1][colonna + i] != StatoCella.VUOTA:
                print("C'è una nave nelle vicinanze di questa posizione. Riprova")
                return False
            
            # Verifica se c'è una nave sotto la posizione desiderata
            if riga < len(griglia) - 1 and griglia[riga + 1][colonna + i] != StatoCella.VUOTA:
                print("C'è una nave nelle vicinanze di questa posizione. Riprova")
                return False
            
            # Verifica se c'è una nave a sinistra della posizione desiderata
            if colonna + i > 0 and griglia[riga][colonna + i - 1] != StatoCella.VUOTA:
                print("C'è una nave nelle vicinanze di questa posizione. Riprova")
                return False
            
            # Verifica se c'è una nave a destra della posizione desiderata
            if colonna + i < len(griglia[0]) - 1 and griglia[riga][colonna + i + 1] != StatoCella.VUOTA:
                print("C'è una nave nelle vicinanze di questa posizione. Riprova")
                return False

    elif orientamento == OrientamentoNave.VERTICALE.value:
        # Verifica se la nave supera i limiti della griglia in verticale
        if riga + nave.lunghezza > len(griglia):
            print("La nave non entra in questa posizione. Riprova")
            return False

        for i in range(nave.lunghezza):
            # Verifica se la cella è occupata da un'altra nave
            if griglia[riga + i][colonna] != StatoCella.VUOTA:
                print("In queste coordinate è già presente un'altra nave. Riprova")
                return False
            
            # Verifica se c'è una nave a sinistra della posizione desiderata
            if colonna > 0 and griglia[riga + i][colonna - 1] != StatoCella.VUOTA:
                print("C'è una nave nelle vicinanze di questa posizione. Riprova")
                return False
            
            # Verifica se c'è una nave a destra della posizione desiderata
            if colonna < len(griglia[0]) - 1 and griglia[riga + i][colonna + 1] != StatoCella.VUOTA:
                print("C'è una nave nelle vicinanze di questa posizione. Riprova")
                return False
            
            # Verifica se c'è una nave sopra la posizione desiderata
            if riga + i > 0 and griglia[riga + i - 1][colonna] != StatoCella.VUOTA:
                print("C'è una nave nelle vicinanze di questa posizione. Riprova")
                return False
            
            # Verifica se c'è una nave sotto la posizione desiderata
            if riga + i < len(griglia) - 1 and griglia[riga + i + 1][colonna] != StatoCella.VUOTA:
                print("C'è una nave nelle vicinanze di questa posizione. Riprova")
                return False

    else:
        raise ValueError("Orientamento non valido. Usare 'orizzontale' o 'verticale'.")

    # Se tutti i controlli passano, la nave può essere inserita
    return True
    

#metodo di controllo tramite rettangolo

# def puo_inserire_nave(nave, orientamento, riga, colonna, griglia):
#     # Imposta la dimensione del quadrato intorno alla nave
#     dimensione_quadrato = 1
    
#     if orientamento == OrientamentoNave.ORIZZONTALE.value":
#         # Controllo se la nave entra nella griglia considerando la sua lunghezza
#         if colonna + nave.lunghezza + dimensione_quadrato > len(griglia[0]):
#             print("La nave non entra in questa posizione. Riprova")
#             return False
#         # Itero attraverso la lunghezza della nave
#         for i in range(nave.lunghezza):
#             for r in range(riga - dimensione_quadrato, riga + dimensione_quadrato + 1):
#                 for c in range(colonna + i - dimensione_quadrato, colonna + i + dimensione_quadrato + 1):
#                     if r < 0 or r >= len(griglia) or c < 0 or c >= len(griglia[0]):
#                         continue  # Salta se le coordinate sono fuori dalla griglia
                        
#                     if griglia[r][c] != StatoCella.VUOTA:
#                         print("C'è una nave nelle vicinanze di questa posizione.")
#                         return False
                        
#     elif orientamento == OrientamentoNave.VERTICALE.value:
#         # Controllo se la nave entra nella griglia considerando la sua lunghezza
#         if riga + nave.lunghezza + dimensione_quadrato > len(griglia):
#             print("La nave non entra in questa posizione. Riprova")
#             return False
#         # Itero attraverso la lunghezza della nave
#         for i in range(nave.lunghezza):
#             for r in range(riga + i - dimensione_quadrato, riga + i + dimensione_quadrato + 1):
#                 for c in range(colonna - dimensione_quadrato, colonna + dimensione_quadrato + 1):
#                     if r < 0 or r >= len(griglia) or c < 0 or c >= len(griglia[0]):
#                         continue  # Salta se le coordinate sono fuori dalla griglia
                        
#                     if griglia[r][c] != StatoCella.VUOTA:
#                         print("C'è una nave nelle vicinanze di questa posizione.")
#                         return False
                        
#     else:
#         raise ValueError("Orientamento non valido. Usare 'orizzontale' o 'verticale'.")
    
#     return True
 

    


