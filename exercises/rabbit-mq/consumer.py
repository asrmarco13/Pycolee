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


def callback(channel, method, properties, body):
    print('Received %s' % body)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_consume(on_message_callback=callback,
                      queue=queue_name,
                      auto_ack=True)
channel.start_consuming()
