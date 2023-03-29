from ship_class import Navi
from griglia import crea_griglia, stampa_griglia
from standards import ship_list
#  metodo che opermette di sparare
def sparare(griglia, ship_list, riga, colonna):
    posizione_colpita = griglia[riga][colonna]
    if posizione_colpita != 0:
        nave = ship_list[posizione_colpita - 1]                              
        Navi.nave_colpita(riga, colonna)
        if Navi.colpita.count(True) == Navi.lunghezza:
            Navi.nave_affondata()
            return True
    else:
        print("Mancato!")
    return False

def gioca_locale():
    # Crea le griglie dei due giocatori
    print("Creazione della griglia del primo giocatore:")
    griglia1 = crea_griglia()
    print("Creazione della griglia del secondo giocatore:")
    griglia2 = crea_griglia()
    
    # Ciclo di gioco: il primo giocatore gioca, poi il secondo
    giocatori = [(griglia1, "Giocatore 1"), (griglia2, "Giocatore 2")]
    for i in range(2):
        griglia, nome_giocatore = giocatori[i]
        print(f"\nTurno di {nome_giocatore}!")
        turno_finito = False
        while not turno_finito:
            # Stampa la griglia del giocatore corrente
            print(f"\nGriglia di {nome_giocatore}:")
            stampa_griglia(griglia, len(griglia), len(griglia[0]))
            
            # Chiede all'utente le coordinate dove sparare
            riga = int(input("Inserisci la riga in cui sparare: "))
            colonna = int(input("Inserisci la colonna in cui sparare: "))
            
            # Esegue lo sparo
            affondata = sparare(griglia, ship_list, riga, colonna)
            if affondata:
                print("Nave affondata!")
            
            # Verifica se il turno è finito
            if all(nave.affondata for nave in ship_list):
                print(f"{nome_giocatore} ha vinto!")
                turno_finito = True
            elif affondata:
                continue
            else:
                turno_finito = True
    print("Fine del gioco!")







           