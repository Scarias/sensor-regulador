def out_range(body) -> bool:
    return float(body.split(b',')[0]) < 0 or float(body.split(b',')[0]) > 5