def prepare_data(data):
    pair_joined = list()
    for sensor, values in data.items():
        if len(values) >= 1:
            pair_str = map(str, (sensor,values[0]))
            pair_joined.append(':'.join(pair_str))
    return ';'.join(pair_joined)