import pika

print('Connect to RabittMQ...')
print('Insert your RabbitMQ credentials...')

username = input('Insert username: ')
password = input('Insert password: ')
host = input('Insert host: ')
credentials = pika.PlainCredentials(username, password)
params = pika.ConnectionParameters(host=host, credentials=credentials)
connection = pika.BlockingConnection(parameters=params)
channel = connection.channel()
queue_name = input('Queue name: ')
channel.queue_declare(queue_name)

print('...successful connection')

count = 0
while True:
    message = str(count)
    count += 1
    channel.basic_publish('', queue_name, message)
    print('Message send %s', message)
    if count > 100000:
        break

connection.close()
