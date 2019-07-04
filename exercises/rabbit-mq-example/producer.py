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

count = 0
while True:
    message = str(count)
    count += 1
    channel.basic_publish('', 'worker_queue', message)
    print('Messaggio inviato %s', message)
    if count > 100000:
        break

connection.close()
