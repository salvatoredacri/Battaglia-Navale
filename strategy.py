from giocatore import *
from standards import clear_console
       
class CambioTurnoStrategy:
    def get_prossimo_giocatore(self, giocatore_corrente, esito_colpo):
        '''
        Metodo astratto per ottenere il prossimo giocatore.
        Viene implementato dalle sottoclassi.
        
        '''
        raise NotImplementedError()
   
class TiroSingoloStrategy(CambioTurnoStrategy):
    '''
    Restituisce il prossimo giocatore in base all'esito del colpo e alla situazione di gioco.
    Se il colpo ha avuto successo e la partita non è finita, si passa all'altro giocatore.
    Altrimenti, si passa lo stesso all'altro giocatore.
    
    '''
    def get_prossimo_giocatore(self, giocatore_corrente, esito_colpo, altro_giocatore):
            if esito_colpo and not partita_finita(giocatore_corrente, altro_giocatore):
                 time.sleep(2)
                 input('Premi INVIO e passa il computer al tuo avversario')
                 return altro_giocatore
            else:
                time.sleep(2)
                input('Premi INVIO e passa il computer al tuo avversario')
                return altro_giocatore 

class TiroContinuoStrategy(CambioTurnoStrategy):
    '''
    Restituisce il prossimo giocatore in base all'esito del colpo e alla situazione di gioco.
    Se il colpo ha avuto successo e la partita non è finita, il giocatore di turno ha diritto ad un altro colpo.
    Altrimenti, si passa all'altro giocatore.
   
    '''
    def get_prossimo_giocatore(self, giocatore_corrente, esito_colpo, altro_giocatore):
         if esito_colpo and not partita_finita(giocatore_corrente, altro_giocatore):
              print('Puoi sparare ancora')
              time.sleep(2)
              return giocatore_corrente
         else:
             time.sleep(2)
             input('Premi INVIO e passa il computer al tuo avversario')
             return altro_giocatore 
        

def partita_finita(giocatore1, giocatore2):
    '''
    Verifica se la partita è finita controllando se uno dei giocatori ha vinto.
    Se uno dei giocatori ha vinto, viene mostrato il messaggio di vittoria e il programma termina.
    Altrimenti, la partita non è ancora finita.
    
    '''
    if giocatore1.vittoria():
        time.sleep(4)
        clear_console()
        print(f"\u001b[92mPartita finita! {giocatore1.nome} ha vinto!\033[0m")
        print('\nGrazie per aver giocato')
        return True and sys.exit()
        
    elif giocatore2.vittoria():
        time.sleep(4)
        clear_console()
        print(f"\u001b[92mPartita finita! {giocatore2.nome} ha vinto!\033[0m")
        print('\nGrazie per aver giocato')
        return True and sys.exit()
    else:
        return False
    

def get_cambio_turno_strategy(modalita):
 '''
 Restituisce l'istanza di strategia di cambio turno in base alla modalità di gioco specificata.
 Se la modalità è 1, viene restituita un'istanza di TiroSingoloStrategy (a prescindere dall'esito del colpo il turno viene passato al prossimo giocatore).
 Se la modalità è 0, viene restituita un'istanza di TiroContinuoStrategy (solo in caso di colpo mancato il turno viene passato al prossimo giocatore).
 
 '''
 if modalita == 1:
     return TiroSingoloStrategy()
 elif modalita == 0:
     return TiroContinuoStrategy()
