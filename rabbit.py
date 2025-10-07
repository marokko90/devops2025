import pika
import time

conn_cred=pika.PlainCredentials('rabbitadmin', '123qaz123qaz')
conn_params = pika.ConnectionParameters(host='79.174.186.211', port=35672, virtual_host='/', credentials=conn_cred)

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

def print_message_sum(ch, method, properties, body):
    print(body)

#while True:
#    time.sleep(0.1)
#    channel.basic_publish(exchange='bank_ex', routing_key='avto', body='test123')


channel.basic_consume(queue='avto_credit_log', on_message_callback=print_message_sum, auto_ack=True)
channel.start_consuming()



