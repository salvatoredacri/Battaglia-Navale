# Battaglia Navale

Questo repository contiene il progetto d'esame Battaglia Navale per il corso di ""Programmazione"" dell'Università Campus Bio-Medico di Roma.

Codice sviluppato da:

- Alessandro Frisenda
- Salvatore D'Acri

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

2) Esegui il seguente comando nella linea di comando:

  ```python
        python3 main.py -g1 nome_giocatore -g2 nome_giocatore2 -d dimensione_tavolo -m modalità_gioco
  ```

   N.B. Sostituisci nome_giocatore con il nome del primo giocatore e nome_giocatore2 con il nome del secondo giocatore. Inoltre, imposta dimensione_tavolo con la dimensione desiderata del campo da battaglia e 
        Modalità_gioco con la modalità desiderata:
           - Modalità 0: Il turno di attacco si conclude solo in caso di mancato bersaglio.
           - Modalità 1: Durante la fase di attacco si procede un turno alla volta.
           
3) I giocatori devono posizionare a turno le navi nel proprio campo da battaglia.

4) I giocatori passano alla fase di attacco fino al completamento del gioco.

5) Il programma decreterà il vincitore

Assicurati di avere Python 3 installato sul tuo sistema e che le dipendenze necessarie per il programma siano soddisfatte prima di eseguire il comando.



