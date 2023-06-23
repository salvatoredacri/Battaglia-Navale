from griglia import *
import string
import re
import time

class giocatore():
    def __init__(self, nome, griglia_giocatore, griglia_colpi, modalita):
        """
        Inizializza un oggetto Giocatore.

        Argomenti:
        - nome: il nome del giocatore
        - griglia_giocatore: la griglia di gioco del giocatore
        - griglia_colpi: la griglia dei colpi effettuati dal giocatore
        - modalita: la modalità di gioco del giocatore

        Attributi:
        - nome: il nome del giocatore
        - griglia_giocatore: la griglia di gioco del giocatore
        - griglia_colpi: la griglia dei colpi effettuati dal giocatore
        - navi_posizionate: la lista delle navi posizionate sulla griglia di gioco
        - modalita: la modalità di gioco del giocatore
        """
        
        self.nome= nome
        self.griglia_giocatore = griglia_giocatore
        self.griglia_colpi = griglia_colpi
        self.navi_posizionate = []
        self.modalita = modalita
        

    def posiziona_navi(self, lista_navi):
        """
        Posiziona le navi nella griglia del giocatore.

        Argomenti:
        - lista_navi: la lista delle navi scelte da posizionare

        Valore di ritorno:
        - La griglia di gioco del giocatore con le navi posizionate
        - La lista delle navi_posizionate sulla griglia di gioco
        """
       
        colonne_valide = string.ascii_uppercase[:len(self.griglia_giocatore)]
        for nave in lista_navi:
            print(f"{self.nome}, inserisci la nave: {nave.nome} di lunghezza: {nave.lunghezza}")

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
                if colonna_iniz not in colonne_valide or riga_iniz < 1 or riga_iniz > len(self.griglia_giocatore):
                    print("Coordinate non valide. Riprova.")
                    continue

                orientamento = input("Inserisci l'orientamento della nave ('o' per orizzontale, 'v' per verticale): ")
                orientamento = orientamento.lower()
                if orientamento not in ['o', 'orizzontale', 'v', 'verticale']:
                    print("Orientamento non valido. Riprova.")
                    continue

                result = self.inserisci_nave(nave, orientamento, riga_iniz - 1, colonne_valide.index(colonna_iniz))
                if result != False:
                    self.griglia_giocatore, coordinate = result
                    nave_posizionata = Navi(nave.nome, nave.lunghezza, orientamento, riga_iniz - 1, colonna_iniz, coordinate)
                    clear_console()
                    stampa_griglia(self.griglia_giocatore)
                    print("\n\nEcco la tua griglia con le navi posizionate:")

                    self.navi_posizionate.append(nave_posizionata)
                    break
                    

        return self.griglia_giocatore, self.navi_posizionate

    def inserisci_nave(self, nave, orientamento, riga_iniz, colonna_iniz):
        """
        Inserisce una nave nella griglia di gioco nella posizione specificata.

        Argomenti:
        - nave: l'oggetto Nave da inserire
        - orientamento: l'orientamento della nave ("orizzontale" o "verticale")
        - riga_iniz: la riga iniziale in cui posizionare la nave
        - colonna_iniz: la colonna iniziale in cui posizionare la nave

        Ritorno:
        - Se la nave può essere inserita:
            - griglia_giocatore: la griglia di gioco aggiornata con la nave inserita
            - coordinate: una lista di tuple che rappresentano le coordinate della nave sulla griglia
        - Se la nave non può essere inserita, restituisce False
        """
        if puo_inserire_nave(nave, orientamento, riga_iniz, colonna_iniz, self.griglia_giocatore):
            coordinate = []
            if orientamento in ['orizzontale', 'o']:
                for i in range(nave.lunghezza):
                    self.griglia_giocatore[riga_iniz][colonna_iniz + i] = 1
                    coordinate.append((riga_iniz, colonna_iniz + i))
            elif orientamento in ['verticale', 'v']:
                for i in range(nave.lunghezza):
                    self.griglia_giocatore[riga_iniz + i][colonna_iniz] = 1
                    coordinate.append((riga_iniz + i, colonna_iniz))
            print("\nNave inserita correttamente:")
            return self.griglia_giocatore, coordinate
        else:
            return False
        

    def turno(self,avversario):
        """
        Gestisce il turno di gioco del giocatore.

        Argomenti:
        - avversario: l'oggetto Giocatore avversario

        Ritorno:
        - True se il gioco è finito (il giocatore ha vinto), False altrimenti
        """
        fine_turno = False
        fine_gioco = False
        
        while not fine_turno:
            clear_console()
            print(f'{self.nome} Ecco la tua griglia dei colpi effettuati')
            stampa_griglia(self.griglia_colpi)
            print(f"{self.nome}, inserisci le coordinate dove vuoi sparare")
            
            colonne_valide = string.ascii_uppercase[:len(avversario.griglia_giocatore)]
           
            while True:
              coordinate_colpo = input('Inserisci le coordinate di dove vuoi sparare (es. A1):')
              if not coordinate_colpo:
                print('Inserire un valore corretto (es. A1)')
                continue
              if not re.match("^[A-Za-z][0-9]+$", coordinate_colpo):
                print("Errore: caratteri speciali non consentiti.")
                continue
              colonna = coordinate_colpo[0].upper()
              riga = int(coordinate_colpo[1:]) - 1
               
              if colonna not in colonne_valide or riga < 0 or riga >= len(avversario.griglia_giocatore):
                print("Coordinate non valide. Riprova.")
                continue
              break
            
            colonna = colonne_valide.index(colonna) 
            
            if self.griglia_colpi[riga][colonna] != 0:
             print("Hai già sparato in questa posizione. Riprova.")
             time.sleep(2)
             continue

            colpo = False
        
            for nave in avversario.navi_posizionate:
             if nave.colpita(riga, colonna):
                print("Hai colpito una nave!")
                colpo = True
                self.griglia_colpi[riga][colonna] = "c"
                
                if nave.affondata():
                    print("Hai affondato una nave!", nave.nome)
                    if all(n.affondata() for n in avversario.navi_posizionate):
                        fine_gioco = avversario.vittoria()
                        break  # Tutte le navi sono affondate, fine del gioco
                        
       
            if colpo and self.modalita == 0:
              print("\nGriglia dei colpi:")
              stampa_griglia(self.griglia_colpi)
              print('Puoi sparare ancora')
              time.sleep(4)
        
            elif not colpo and self.modalita == 0:
              print("Hai sparato in acqua.")
              self.griglia_colpi[riga][colonna] = "-"
              stampa_griglia(self.griglia_colpi)
              time.sleep(2)
              fine_turno = True
            else:
               if not colpo and self.modalita == 1:
                print("Hai sparato in acqua.")
                self.griglia_colpi[riga][colonna] = "-"
                stampa_griglia(self.griglia_colpi)
                time.sleep(2)
                fine_turno = True
               elif colpo and self.modalita == 1:
                 print("\nGriglia dei colpi:")
                 stampa_griglia(self.griglia_colpi)
                 time.sleep(3)
                 fine_turno = True

        

        return fine_gioco
    

    def vittoria(self):
       """
        Controlla se il giocatore ha vinto la partita.

        Ritorno:
        - True se il giocatore ha vinto, False altrimenti
        """
       for nave in self.navi_posizionate:
          if not nave.affondata():
             return False
          return True 
    







           
