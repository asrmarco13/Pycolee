# RabbitMQ

L'esercizitazione prevede una comunicazione tra 2 applicativi attraverso l'uso di un message broker: **Rabbit MQ**. Istallare e configurare RabbitMQ e la libreria **Pika** di Python (consiglio l'istallazione della libreria Pika usando il tool **Virtual Environment** su Linux).

Creare uno script **producer.py** che richiede all'utente i parametri di connessione per RabbitMQ, crea una connessione e invia sulla coda dichiarata i messaggi per il consumer.

Creare uno script **consumer.py** che richiede all'utente i parametri di connessione per RabbitMQ, crea una connessione e prende dalla coda dichiarata i messaggi spediti dal producer. Se si vuole osservare una concorrenza di richieste sulla coda si consiglia di copiare più volte lo script del consumer e lanciare più terminali.
