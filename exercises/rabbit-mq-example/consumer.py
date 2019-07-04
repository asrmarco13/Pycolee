import pika

print('Collegamento a RabiitMQ...')

username = 'manager'
password = 'manager'
credentials = pika.PlainCredentials(username, password)
params = pika.ConnectionParameters(host='localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters=params)
channel = connection.channel()
channel.queue_declare('worker_queue')

print('...eseguito')

def callback(channel, method, properties, body):
    print('Ricevuto messaggio %s' % body)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_consume(on_message_callback=callback, queue='worker_queue', auto_ack=True)
channel.start_consuming()

connection.close()
