class navi:
 def __init__(self,griglia,nome,lunghezza):
    self.nome=nome
    self.griglia=griglia
    self.posizione=[]
    self.colpita=[False]*lunghezza
    self.lunghezza=lunghezza



 def puo_inserire_nave(self, lunghezza, orientamento, riga, colonna):
    if orientamento == "orizzontale":
        # Controllo se entra
        if colonna + lunghezza > len(self.griglia[0]):
            return False
        for i in range(lunghezza):
            # Controllo che non sia sopra un'altra nave
            if self.griglia[riga][colonna + i] != 0:
                return False
            # Controllo che sopra non abbia niente se non mi trovo sulla prima riga
            if riga > 0 and self.griglia[riga - 1][colonna + i] != 0:
                return False
            # Controllo che sotto non abbia niente se non mi trovo sull'ultima riga
            if riga < len(self.griglia) - 1 and self.griglia[riga + 1][colonna + i] != 0:
                return False
            # Controllo sinistra se non sono sul bordo sinistro
            if colonna + i > 0 and self.griglia[riga][colonna + i - 1] != 0:
                return False
            # Controllo destra se non sono sul bordo destro
            if colonna + i < lunghezza - 1 and self.griglia[riga][colonna + i + 1] != 0:
                return False
    elif orientamento == "verticale":
        # Controllo se entra
        if riga + lunghezza > len(self.griglia):
            return False
        for i in range(lunghezza):
    #        # controllo che non sia sopra un'altra nave
            if self.griglia[riga + i][colonna] != 0:
                return False
            if colonna > 0 and self.griglia[riga + i][colonna - 1]:
                return False
            if colonna < len(self.griglia[0]) - 1 and self.griglia[riga + i][colonna + 1] != 0:
                return False
            if i > 0 and self.griglia[riga + i - 1][colonna] != 0:
                return False
            if i < lunghezza - 1 and self.griglia[riga + i + 1][colonna] != 0:
                return False
    else:
        raise ValueError("Orientamento non valido. Usare 'orizzontale' o 'verticale'.")
    return True

def inserisci_nave(self, lunghezza, orientamento, riga, colonna):
    if self.puo_inserire_nave(self, lunghezza, orientamento, riga, colonna):
        if orientamento == "orizzontale":
            for i in range(lunghezza):
                self.griglia[riga][colonna + i] = 1
        elif orientamento == "verticale":
            for i in range(lunghezza):
                self.griglia[riga + i][colonna] = 1
        return self.griglia
    else:
        raise ValueError("Non puoi inserire la nave qui.")

def nave_colpita(self, riga, colonna):
   posizione_colpita=self.griglia[riga][colonna]
   if posizione_colpita!=0:
    self.colpita[posizione_colpita-1]=True
    print ("hai colpito la nave")

def nave_affondata(self):
    if all(self.colpita):
        print ("hai affondato la nave")