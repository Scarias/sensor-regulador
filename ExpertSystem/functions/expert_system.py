import numpy as np


# data: {#sensor: distancia conseguida por el sensor # (float), ... (hasta n sensores)}
# distance_matrix: matriz de distancia entre sensores {k_sensor:[(todos los sensores en orden exceptuando el k sensor)]}

def matrix_calc(data, distance):
    to_add = {}
    temp = {}

    values = list(data.items())
    values.sort(key=lambda x: x[1])

    for i in range(len(values)):
        for k in range(i + 1, len(values)):
            if values[k][0] == values[i][0]:
                continue

            if distance[values[k][0]][int(values[i][0]) - 1] >= 8:
                try:
                    temp[values[k][0]].append(np.random.randint(0, 1))
                except KeyError:
                    temp[values[k][0]] = [np.random.randint(0, 1)]
            else:
                try:
                    temp[values[k][0]].append(np.random.randint(1, 2))
                except KeyError:
                    temp[values[k][0]] = [np.random.randint(1, 2)]

        if values[i][1] < 1.5:
            try:
                temp[values[i][0]].append(np.random.randint(3, 5))
            except KeyError:
                temp[values[i][0]] = [np.random.randint(3, 5)]
        elif 1.5 <= values[i][1] <= 3.5:
            try:
                temp[values[i][0]].append(np.random.randint(2, 4))
            except KeyError:
                temp[values[i][0]] = [np.random.randint(2, 4)]
        else:
            try:
                temp[values[i][0]].append(np.random.randint(0, 2))
            except KeyError:
                temp[values[i][0]] = [np.random.randint(0, 2)]

    for i in temp.keys():
        to_add[i] = sum(temp[i]) / len(temp[i])
        
    return to_add