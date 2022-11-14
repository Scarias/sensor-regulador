from stomp import Connection


conn = Connection([('localhost', 61614)])
conn.connect()