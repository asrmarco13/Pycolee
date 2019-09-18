# Flask

## Indice
1. [Introduzione](#introduzione)
2. [Primo esercizio REST con Flask](#primo-esercizio-rest-con-flask)
3. [Secondo esercizio RESTful con Flask](#secondo-esercizio-restful-con-flask)
4. [Terzo esercizio RESTful con SQLite](#terzo-esercizio-restful-con-sqlite)

### Introduzione
[Flask](https://palletsprojects.com/p/flask/) è un web framework (classificato anche come microframework) scritto in Python e basato sullo strumento Werkzeug WSGI e Jinja2. Una delle caratteristiche importanti di questo framework è che il sistema è basato su trasmissione di dati su HTTP senza ulteriori livelli (esempio: SOAP).

### Primo esercizio REST con Flask
Il primo esercizio chiamato **first-rest-api** consiste in programma **app.py** in cui sono definite varie azioni:
- un'azione **'/store'** che aggiunge ad una lista, definita **stores**, un oggetto e ritorna un oggetto JSON;
- un'azione **'/store/<string:name>'** che ritorna, se presente, un oggetto presente nella lista stores;
- un'azione **'/store'** che ritorna tutti gli oggetti presenti nella lista stores;
- un'azione **'/store/<string:name>/item'** che inserisce all'interno di uno store esistente un nuovo oggetto;
- un'azione **'/store/<string:name>/item'** che restituisce un oggetto presente all'interno di uno store esistente;

Per far partire l'esercizio il mio consiglio è quello di creare un ambiente [virtualizzato](https://wiki.archlinux.org/index.php/Python/Virtual_environment#Usage) tramite Python all'interno della cartella ed installare con **pip** (package manager per Python) la libreria Flask. Di seguito il comando:

`pip install Flask`

A questo punto avviare il programma tramite comando `python app.py`. Se si apre il browser e si punta al seguente indirizzo [http://localhost:8080](http://localhost:8080) otteremo in risposta un **'Hello World!'** definito nel metodo **home** del nostro programma.

### Secondo esercizio RESTful con Flask
Il secondo esercizio chiamato **first-restful-app** consiste in programma definito **app.py** in cui sono definite due classi:
- Item
- ItemList

La classe Item è composta di 4 metodi:
- un metodo **GET**  che ritorna, se presente, un oggetto presente nella lista items;
- un metodo **POST** che aggiunge un oggetto alla lista items;
- un metodo **DELETE** che elimina un ogetto presente all'interno della lista items;
- un metodo **PUT** che aggiorna un oggetto già esistente all'interno di items. In caso contrario aggiunge un nuovo oggetto alla lista.

La classe ItemList è composta da 1 solo metodo:
- un metodo **GET** che ritorna la lista di tutti gli oggetti presenti in items.

Per far partire l'esercizio il mio consiglio è quello di creare un ambiente [virtualizzato](https://wiki.archlinux.org/index.php/Python/Virtual_environment#Usage) tramite Python all'interno della cartella ed installare con **pip** (package manager per Python) la libreria Flask. Di seguito il comando:

`pip install Flask`
`pip install Flask-RESTful`
`pip install Flask-JWT`

In questo esercizio usiamo come metodo di autenticazione della sessione lo standard JWT (JSON Web Token). In particolare, possiamo notare che il metodo **GET** della classe Item usa un decorator **jwt_required()**. Cosa significa questo? Significa che all'invocazione del metodo se non si ha un token valido da passare in sessione non avremo restituito nessun item.

Un'altra particolarità del nostro esercizio è l'uso dell'interfaccia [Request Parsing](https://flask-restplus.readthedocs.io/en/stable/parsing.html) che Flask-RESTful mette a disposizione. Quest'interfaccia permette un più semplice accesso alla nostra risorsa dicendoci quali parametri il metodo si aspetta di ricevere in input. All'interno della classe Item, prima della definizione dei metodi definiamo una variabile **parser** che definisce l'obbligatorietà del campo **price**. Quando invocheremo la **POST** e la **PUT** il metodo **parse_args()** verificherà la presenza di un valore intero all'interno del campo **price**. Se non presente restituirà un errore, altrimenti inserirà l'oggetto definito come chiave-valore {'price': int} all'interno di **request_data**.

La classe User presente all'interno di user.py definisce un costruttore composto da: id, username e password.

In security.py definiamo:
- un'istanza **users** che è una lista di oggetti User;
- un dizionario **username_mapping** che useremo per recuperare le informazioni utente attraverso il suo username;
- un dizionario **userid_mapping** che useremo per recuperare le informazioni utente attraverso il suo id;
- una funzione **authenticate** che prende in input username e password e verifica che esse siano contenute all'interno di **username_mapping**. Il metodo ritorna l'utente se lo trova, altrimenti non torna nulla;
- una funzione chiamata **identity** che prende in input un payload che è il contenuto del token JWT e da cui estrarremo l'ID utente. Estratto il valore andremo a recuperare l'utente specifico che si trova all'interno di **userid_mapping**. Il metodo ritorna l'utente se lo trova, altrimenti non torna nulla.

A questo punto avviare il programma tramite comando `python app.py`. Usiamo Postman per invocare i metodi e verifichiamo che tutto funzioni correttamente. 

### Terzo esercizio RESTful con SQLite
Il terzo esercizio **restful-sqlite-app** è un programma che espone varie risorse.
