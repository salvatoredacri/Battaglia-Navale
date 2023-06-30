from griglia import  *
from standards import *
from giocatore import giocatore
from strategy import *

import time


try:
 clear_console()
except Exception as e:
 print("Si è verificato un errore nella chiamata a clear_console():", str(e))
 sys.exit()



# Assegna i valori degli argomenti alle variabili
args=initialize_parser(navi_disponibili)
check_parser(args)

lista_navi_1 = crea_lista_navi(args, navi_disponibili)
lista_navi_2 = crea_lista_navi(args, navi_disponibili)
giocatore_1 = giocatore(args.giocatore_1, crea_griglia(args.dimensione), crea_griglia(args.dimensione))
giocatore_2 = giocatore(args.giocatore_2, crea_griglia(args.dimensione), crea_griglia(args.dimensione))

# stampa messaggio di benvenuto 
print('Benvenuto')
stampa_messaggio_iniziale(lista_navi_1)
time.sleep(5)
clear_console()

# Giocatore 1 posiziona le tue navi!
print(giocatore_1.nome,", è il tuo turno!" "\n Posiziona le tue navi!")
stampa_griglia(giocatore_1.griglia_giocatore)
griglia1, navi_posizionate_1 = giocatore_1.posiziona_navi(lista_navi_1)
stampa_griglia(griglia1)
print('Hai terminato le navi da posizionare, pensa alla tua strategia!')
time.sleep(2)

clear_console()

# Giocatore 1 ha finito di posizionare le navi. Passa al turno del Giocatore 2.
input(f"Premi INVIO e passa il computer per passare al turno di {giocatore_2.nome}")
clear_console()



# # Giocatore 2 posiziona le tue navi!
print(giocatore_2.nome,", è il tuo turno!" "\n Posiziona le tue navi!")
stampa_griglia(giocatore_2.griglia_giocatore)
griglia2, navi_posizionate_2 = giocatore_2.posiziona_navi(lista_navi_2)
stampa_griglia(griglia2)
print('Hai terminato le navi da posizionare, pensa alla tua strategia!')
time.sleep(2)

clear_console()

# Inizia il gioco
input('Premi INVIO per passare alla fase successiva!')
clear_console()

print("""Giocatori, inizia la fase di attacco! Preparate la vostra offensiva!
         \nBuona fortuna!""")

time.sleep(5)
clear_console()


cambio_turno_strategy = get_cambio_turno_strategy(args.modalita) #qui si usa il pattern strategy
giocatore_di_turno = giocatore_1

while not partita_finita(giocatore_1,giocatore_2):
  esito = giocatore_di_turno.turno() 
  altro_giocatore = giocatore_1 if giocatore_di_turno == giocatore_2 else giocatore_2
  giocatore_di_turno = cambio_turno_strategy.get_prossimo_giocatore(giocatore_di_turno, esito, altro_giocatore)
