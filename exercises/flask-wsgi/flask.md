# Flask

## Indice
1. [Introduzione](#introduzione)
2. [Primo esercizio REST con Flask](#primo-esercizio-rest-con-flask)

### Introduzione
[Flask](https://palletsprojects.com/p/flask/) è un web framework (classificato anche come microframework) scritto in Python e basato sullo strumento Werkzeug WSGI e Jinja2. Una delle caratteristiche importanti di questo framework è che il sistema è basato su trasmissione di dati su HTTP senza ulteriori livelli (esempio: SOAP).

### Primo esercizio REST con Flask
Il primo esercizio chiamato **first-rest-api** consiste in una classe **app.py** in cui sono definite varie azioni:
- un'azione **'/store'** che aggiunge ad una lista, definita **stores**, un oggetto e ritorna un oggetto JSON;
- un'azione **'/store/<string:name>'** che ritorna, se presente, un oggetto presente nella lista stores;
- un'azione **'/store'** che ritorna tutti gli oggetti presenti nella lista stores;
- un'azione **'/store/<string:name>/item'** che inserisce all'interno di uno store esistente un nuovo oggetto;
- un'azione **'/store/<string:name>/item'** che restituisce un oggetto presente all'interno di uno store esistente;

Per far partire l'esercizio il mio consiglio è quello di creare un ambiente [virtualizzato](https://wiki.archlinux.org/index.php/Python/Virtual_environment#Usage) tramite Python all'interno della cartella ed installare con **pip** (package manager per Python) la libreria Flask. Di seguito il comando:

`pip install Flask`

A questo punto avviare il programma tramite comando `python app.py`. Se si apre il browser e si punta al seguente indirizzo [http://localhost:8080](http://localhost:8080) otteremo in risposta un **'Hello World!'** definito nel metodo **home** del nostro programma.
