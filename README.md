# Battaglia Navale

Questo repository contiene il progetto d'esame Battaglia Navale per il corso di ""Programmazione"" dell'Università Campus Bio-Medico di Roma.


# Specifica del gioco della battaglia navale

Il programa deve permettere a due giocatori di 
giocare alla "battaglia navale" secondo le regole 
usuali.

I due giocatori devono poter configurare il proprio
campo di gioco che consiste in una una matrice all'interno della
quale posizionare un numero predeterminato di navi
di diversa lunghezza secondo le seguenti regole:
- la lunghezza delle navi corrisponde a un numero 
intero di caselle della matrice;
- ciascuna nave può essere disposta orizzontalmente
o verticalmente, interamente all'interno del campo di gioco;
- due navi non possono essere adiacenti: deve sempre esserci
almeno una casella di distanza tra una nave ed ogni altra;
- il gioco può prevedere due modalità di alternanza del turno
di gioco tra i giocatori:
  * alternanza sistematica (un tiro ciascuno)
  * in caso di ogni colpo andato a segno, il giocatore ha diritto ad un altro colpo.

La dimensione del campo di gioco, il 
numero di navi e la loro distribuzione 
in termini di dimensioni sono parametri con cui 
l'applicazione deve essere inizialmente configurata
e sono gli stessi per entrambi i giocatori.
In altre parole non sono parametri fissi, ma possono 
essere modificati prima di iniziare il gioco.

L'applicazione deve fornire le seguenti funzionalità:
- imporre il rispetto delle regole di gioco;
- configurazione dei parametri (dimensione del campo di gioco, 
numero di navi per ogni dimensione permessa);
- ciascun giocatore deve poter distribuire le proprie navi
sul proprio campo di gioco senza che l'altro giocatore 
possa conoscere tale distribuzione;
- ciascun giocatore deve poter vedere il risultato 
di tutti i propri colpi prima di indicare il colpo
successivo;
- ciascun giocatore, secondo il proprio turno di gioco, comunica le coordinate
del colpo e l'applicazione deve fornire il risultato: *mancato*/*colpito*/*affondato*;
- riconosciento della fine del gioco e proclamazione 
del vincitore quando tutte le navi di un giocatore sono 
state affondate.

# ESECUZIONE

1) Assicurati di trovarti nella directory in cui è presente il file main.py.

  ```python
       cd path/to/directory 
  ```
2) Esegui il seguente comando nella linea di comando per  una descrizione dettagliata delle opzioni, degli argomenti e delle funzionalità del programma programma.

  ```python
        python3 main.py --help
  ```

3) Esegui il seguente comando nella linea di comando per l'inizializzazione del gioco:

  ```python
        python3 main.py --nome_nave quantità -g1 nome_giocatore -g2 nome_giocatore2 -d dimensione_tavolo -m modalità_gioco
  ```

N.B. Sostituisci:
- `nome_nave quantità` con il nome e il numero di navi da voler selezionare.
- `nome_giocatore` con il nome del primo giocatore.
- `nome_giocatore2` con il nome del secondo giocatore.
- `dimensione_tavolo` con la dimensione desiderata del campo da battaglia.
- `modalità_gioco` con la modalità desiderata:

  Modalità di gioco:
  - Modalità 0: Il turno di attacco si conclude solo in caso di mancato bersaglio.
  - Modalità 1: Durante la fase di attacco si procede un turno alla volta.


Esempio modalità personalizzata:  

```python
      python3 main.py --cacciatorpediniere 1 --sottomarino 2 --incrociatore 1 --corazzata 1 --partaerei 1 -g1 Salvatore -g2 Alessandro -d 10 -m 0
 ```
 In alternativa si può eseguire il programma in modalità dafault con il seguente comando nella linea di comando:

  ```python
        python3 main.py 
   ```
Cosi facendo il programma inizierà con le seguenti assegnazioni:
- una nave per ogni tipo
- -g1 giocatore1
- -g2 giocatore2
- -d 9
- -m modalità 0


4) I giocatori devono posizionare a turno le navi nel proprio campo da battaglia.

5) I giocatori passano alla fase di attacco fino al completamento del gioco.

6) Il programma decreterà il vincitore.

Assicurati di avere Python 3 installato sul tuo sistema e che le dipendenze necessarie per il programma siano soddisfatte prima di eseguire il comando.

# Codice sviluppato da:

- Alessandro Frisenda.
- Salvatore D'Acri.


