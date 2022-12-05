def out_range(body) -> bool:
    return float(body.body.split(',')[0]) < 0 or float(body.body.split(',')[0]) > 5