from enum import Enum
class OrientamentoNave(Enum):
    ORIZZONTALE =  ''
    VERTICALE =  ''

class Navi:
    def __init__(self, nome, lunghezza, orientamento, riga_iniz, colonna_iniz, coordinate=None): 
        """
        Inizializza un oggetto Navi con il nome, la lunghezza, l'orientamento, le posizioni di partenza e le coordinate specificate.

        Argomenti:
        - nome: Il nome della nave.
        - lunghezza: La lunghezza della nave.
        - orientamento: L'orientamento della nave (orizzontale o verticale)
        - riga_iniz: La riga di partenza per il posizionamento della nave 
        - colonna_iniz: La colonna di partenza per il posizionamento della nave
        - coordinate: Una lista delle coordinate occupate dalla nave. (Default: None)
        

        Attributi:
        - nome: Il nome della nave.
        - lunghezza: La lunghezza della nave.
        - orientamento: L'orientamento della nave (orizzontale o verticale)
        - riga_iniz: La riga di partenza per il posizionamento della nave 
        - colonna_iniz: La colonna di partenza per il posizionamento della nave
        - coordinate: Una lista delle coordinate occupate dalla nave.
        - colpi: Il numero di volte che la nave è stata colpita.
        

        """
        self.nome = nome
        self.lunghezza = lunghezza
        self.orientamento = orientamento
        self.riga_iniz = riga_iniz
        self.colonna_iniz = colonna_iniz
        self.colpi = 0  
       
        if coordinate is None:
         self.coordinate = []
        else:
            self.coordinate = coordinate
    
    def controlla_colpo(self, riga, colonna): 
        """
        Verifica se la nave è stata colpita in una specifica posizione.

        Argomenti:
        - riga: La riga in cui si vuole verificare il colpo.
        - colonna: La colonna in cui si vuole verificare il colpo.
        - griglia: La griglia del giocatore in cui si trova la nave.

        Valore di ritorno:
        - True se la nave è stata colpita nella posizione specificata, False altrimenti.

        """
        
      
        
        if (riga, colonna) in self.coordinate:
             return True
        return False
    
    def colpita(self, riga, colonna):    
        """
        Registra un colpo sulla nave nella posizione specificata.

        Argomenti:
        - riga: La riga in cui si è verificato il colpo.
        - colonna: La colonna in cui si è verificato il colpo.
        

        Valore di ritorno:
        - True se la nave è stata colpita nella posizione specificata, False altrimenti.

        """
        
        if self.controlla_colpo(riga,colonna):
            self.coordinate.remove((riga,colonna))
            self.colpi += 1
            return True
        return False
    
    def affondata(self):  
        """
        Verifica se la nave è affondata.

        Valore di ritorno:
        - True se la nave è affondata (è stata colpita tutte le volte necessarie), False altrimenti.

        """
        
        if self.colpi == self.lunghezza:
            return True
        else:
            return False
    
    
                     




                     


