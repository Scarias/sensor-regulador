def clean_data(data):
    for k in data.keys():
        if any(data[k]):
            data[k].pop(0)