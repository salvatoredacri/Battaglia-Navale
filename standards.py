from ship_class import Navi
from griglia import *
import argparse
import sys
import platform
import os


# Controlla gli argomenti della riga di comando
def check_parser(args):
    try:
        check_arguments(args)
    except ValueError:
        sys.exit()


def check_arguments(args):
    # Controlla se la dimensione è compresa tra 7 e 20
    if not 7 <= args.dimensione <= 20:
        print('\u001b[31mDimensione errata\033[0m')
        raise ValueError
    # Controlla se il numero di portaerei è compreso tra 0 e 3
    if not 0 <= args.portaerei <= 3:
        print('\u001b[31mNumero invalido di portaerei\033[0m')
        raise ValueError
    # Controlla se il numero di portaerei è compreso tra 0 e 3
    if not 0<= args.corazzata <= 3:
        print('\u001b[31mNumero invalido di corazzata\033[0m')
        raise ValueError
    # Controlla se il numero di incrociatori è compreso tra 0 e 4
    if not 0<= args.incrociatore <=4:
        print('\u001b[31mNumero invalido di incrociatore\033[0m')
        raise ValueError
    # Controlla se il numero di sottomarini è compreso tra 0 e 5
    if not 0<= args.sottomarino<= 5:
        print('\u001b[31mNumero invalido di sottomarino\033[0m')
        raise ValueError
    # Controlla se il numero di cacciatorpediniere è compreso tra 0 e 5
    if not 0<= args.cacciatorpediniere <=5:
        print('\u001b[31mNumero invalido di cacciatorpediniere\033[0m')
        raise ValueError
    # Controlla se la modalità è 0 o 1
    if not (args.modalita==0 or args.modalita==1):
        print('\u001b[31mInput invalido per "modalita". Deve essere 0 o 1\033[0m')
        raise ValueError
    
    
# Dizionario dei tipi di nave disponibili
navi_disponibili = {
    "portaerei": Navi("portaerei", 5),
    "corazzata": Navi("corazzata", 4),
    "incrociatore": Navi("incrociatore", 3),
    "sottomarino": Navi("sottomarino", 2),
    "cacciatorpediniere": Navi("cacciatorpediniere", 1)
}
# Crea la lista delle navi sulla base degli argomenti della riga di comando e delle navi disponibili
def crea_lista_navi(args, navi_disponibili):
    # Crea una copia dell'oggetto args
    args_copy = argparse.Namespace(**vars(args))
    
    lista_navi = []
    for nave in navi_disponibili.values():
        # Ottiene il valore dell'attributo corrispondente al nome della nave
        num_navi = getattr(args_copy, nave.nome)  
        if num_navi > 0:
            for _ in range(num_navi):
                # Crea una nuova nave con quantita=1
                nuova_nave = Navi(nave.nome, nave.lunghezza, quantita=1)
                # Aggiunge la nuova nave alla lista delle navi 
                lista_navi.append(nuova_nave)
                # Decrementa il valore di num_navi di 1 
                num_navi -= 1  
                # Aggiorna il valore di num_navi nella copia di args
                setattr(args_copy, nave.nome, num_navi) 
    
    return lista_navi


def initialize_parser(navi_disponibili):
    parser = argparse.ArgumentParser()
    for nave in navi_disponibili.values():
     # Aggiunge un argomento per il numero di navi di ogni tipo
     parser.add_argument(f"--{nave.nome}", type=int, default=1, help=f"Numero di {nave.nome} da inserire")

    # Aggiunge gli argomenti per i nomi dei giocatori, la dimensione della griglia e la modalità di gioco
    parser.add_argument("-g1","--giocatore_1", type=str,default='giocatore_1', help='Nome del giocatore 1')
    parser.add_argument("-g2", "--giocatore_2", type=str,default='giocatore_2', help='Nome del giocatore 2')
    parser.add_argument("-d","--dimensione", type=int, default=9, help='Dimensione della griglia')
    parser.add_argument('-m','--modalita', type=int, default=0, help='Modalità di gioco: 0 il turno di attacco si conclude solo in caso di mancato bersaglio; 1 si procede un turno alla volta ')
   
    return parser.parse_args()

# Stampa un messaggio iniziale con le quantità delle navi selezionate
def stampa_messaggio_iniziale(lista_navi):
    print("Quantità di navi selezionate:")
    # Crea un insieme di nomi delle navi selezionate
    navi_selezionate = set(nave.nome for nave in lista_navi)
    for nome_nave in navi_selezionate:
    # Calcola la quantità totale della nave
     quantita_nave = sum(nave.quantita for nave in lista_navi if nave.nome == nome_nave)
     print(f"{nome_nave}: {quantita_nave}")
        
       

def clear_console():
# Controllo del sistema operativo
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:
        os.system('clear') # Unix/Linux/Mac
