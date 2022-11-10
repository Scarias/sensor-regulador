import stomp
import time

conn = stomp.Connection([('127.0.0.1', 61613)])
conn.connect()
conn.send(body="this is a test", destination="/queue/test", content_type="text/blah", receipt="123")
time.sleep(2)
conn.disconnect()