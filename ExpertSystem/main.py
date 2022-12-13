import json
from flask import Flask, request

from functions.expert_system import matrix_calc


app = Flask(__name__)


@app.get('/lumen/expert_system')
def expert_system():

    event = request.get_json()

    # Variables
    to_return = []
    temp = {}

    # Loads json dump from other lambda
    body = json.loads(event['body'])
    datas = body['data']
    distance = body['distance']
    print(f" [x] Data received: {datas}")
    
    # Expert system
    for data in datas:
        # Get lumen matrix
        lumen_matrix = matrix_calc(data, distance)
        to_return.append(lumen_matrix)
        
    print(f" [x] Data to send: {to_return}")

    return {
        'statusCode': 200,
        'body': json.dumps(to_return),
    }
