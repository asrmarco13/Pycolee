# Conto Corrente

## Indice
1. [Introduzione](#introduzione)
2. [Conto 1](#conto-1)
3. [Conto 2](#conto-2)
4. [Conto 3](#conto-3)
5. [Conto 4](#conto-4)

### Introduzione
Vediamo come si inizializza il costruttore di una classe, come si definiscono gli attributi di un'istanza.

### Conto 1
Definire una classe **ContoCorrente** <u>sottoclasse di Object</u>.

Definire il costruttore di ContoCorrente che accetta in input 3 parametri: **nome**, **conto** e **importo**. Gli attributi di **istanza** sono nome, conto e saldo.

Definire un **metodo preleva** che accetta in **input** un **importo** che preleverà dal saldo una certa somma ogni volta che verrà  invocato.

Definire un **metodo deposita** che accetta in **input** un **importo** che aggiungerà una certa somma ogni volta che verrà invocato.

Definire un **metodo descrizione** che stampa il nome del titolare, il numero del conto e il saldo.

### Conto 2
Definire una classe **ContoCorrente** <u>sottoclasse di Object</u>.

Definire il costruttore di ContoCorrente che accetta in input 3 parametri: **nome**, **conto** e **importo**. Gli attributi di **istanza** sono nome, conto e saldo.

Definire il **saldo** come <u>attributo nascosto</u>.

Definire una property getter, di nome **saldo**, che ritorna il saldo.

Definire una property setter, di nome **saldo**, che modifica l'attributo saldo. All'interno del metodo setter chiamare il metodo che sottrae il saldo portandolo a zero. Chiamare poi il metodo deposita che definisce il nuovo importo pari al saldo.

Definire un metodo preleva che accetta in input un importo che preleverà dal saldo una certa somma ogni volta che verrà invocato.

Definire un metodo **deposita** che accetta in unput un importo che aggiungerà una certa somma ogni volta che verrà invocato.

Definire un metodo **descrizione** che stampa il nome del titolare, il numero del conto e il saldo.

### Conto 3
Definire una classe **Conto** <u>sottoclasse di Object</u>.

Definire una classe **ContoCorrente** <u>sottoclasse di Conto</u>.

Definire il costruttore di Conto che accetta in input 2 parametri: **nome** e **conto**. Gli attributi di **istanza** sono nome e conto.

Definire il costruttore di ContoCorrente che accetta in input 3 parametri: **nome**, **conto** e **importo**. I parametri nome e conto devono essere <u>passati alla superclasse</u> mentre la variabile saldo deve essere un attributo dell'istanza ContoCorrente.

Definire il **saldo** come attributo <u>nascosto</u>.

Definire una property getter, di nome **saldo**, che ritorna il saldo.

Definire una property setter, di nome **saldo**, che modifica l'attributo saldo. All'interno del metodo setter chiamare il metodo che sottrae il saldo portandolo a zero. Chiamare poi il metodo deposita che definisce il nuovo importo pari al saldo.

Definire un metodo **preleva** che accetta in input un importo che preleverà dal saldo una certa somma ogni volta che verrà invocato.

Definire un metodo **deposita** che accetta in unput un importo che aggiungerà una certa somma ogni volta che verrà invocato.

Definire un metodo **descrizione** che stampa il nome del titolare, il numero del conto e il saldo.

### Conto 4
Definire una classe **Conto** <u>sottoclasse di Object</u>.

Definire una classe **ContoCorrente** <u>sottoclasse di Conto</u>.

Definire una classe **GestoreContiCorrenti** <u>sottoclasse di Object</u>.

Definire il costruttore di Conto che accetta in input 2 parametri: **nome** e **conto**. Gli attributi di **istanza** sono nome e conto. 

Definire il costruttore di ContoCorrente che accetta in input 3 parametri: **nome**, **conto** e **importo**. I parametri nome e conto devono essere passati alla superclasse mentre la variabile saldo deve essere un attributo dell'istanza ContoCorrente.

Definire il **saldo** come <u>attributo nascosto</u>.

Definire una property getter, di nome **saldo**, che ritorna il saldo.

Definire una property setter, di nome **saldo**, che modifica l'attributo saldo.

All'interno del metodo setter chiamare il metodo che sottrae il saldo portandolo a zero. Chiamare poi il metodo deposita che definisce il nuovo importo pari al saldo.

Definire un metodo **preleva** che accetta in input un importo che preleverà dal saldo una certa somma ogni volta che verrà invocato.

Definire un metodo **deposita** che accetta in unput un importo che aggiungerà una certa somma ogni volta che verrà invocato.

Definire un metodo **descrizione** che stampa il nome del titolare, il numero del conto e il saldo.

Definire un metodo <u>statico</u> **bonifico** in <u>GestoreContiCorrenti</u> che accetta in input 3 parametri: **sorgente**, **destinazione** e **importo**. Il metodo bonifico preleva del denaro dal conto sorgente e lo accredita nel conto di destinazione.

