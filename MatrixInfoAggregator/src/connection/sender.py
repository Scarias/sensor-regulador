from stomp import Connection


conn = Connection([('amqps://b-dfe8c9d7-2f1f-4d5f-a4ec-e50bf431bd18.mq.sa-east-1.amazonaws.com', 5671)])
conn.connect()