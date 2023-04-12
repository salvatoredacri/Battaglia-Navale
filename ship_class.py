class Navi:
    def __init__(self,nome,lunghezza):
        self.nome=nome
        self.lunghezza=lunghezza
        self.colpita=[False]*lunghezza
        self.affondata=False


    def nave_colpita(self, riga, colonna, griglia_giocatore):
        posizione_colpita=griglia_giocatore[riga][colonna]
        if posizione_colpita!=0:
            self.colpita[posizione_colpita-1]=True
        return False


    def nave_affondata(self):
        if all(self.colpita):
            print ("hai affondato la nave")
        return False
    #rimuovi le coordinate colpite dalla griglia
    
    def rimuovi_coordinate(self,griglia_giocatore,riga,colonna):
         for i in range(self.lunghezza):
             if self.colpita[i]==True:
                 griglia_giocatore[riga][colonna]='c'
                 return griglia_giocatore
             return False
                
                 
                 
                 
                 




def puo_inserire_nave(nave, orientamento, riga, colonna, griglia):
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
    if puo_inserire_nave(nave, orientamento, riga, colonna, griglia):
        if orientamento == "orizzontale":
            for i in range(nave.lunghezza):
                griglia[riga][colonna + i] = 'x'
        elif orientamento == "verticale":
            for i in range(nave.lunghezza):
                griglia[riga + i][colonna] = 'x'
        print("\nNave inserita correttamente:")
        return griglia
    else:
        return False 
