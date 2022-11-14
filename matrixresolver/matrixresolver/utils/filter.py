def out_range(frame) -> bool:
    return float(frame.body.split(',')[0]) < 0 or float(frame.body.split(',')[0]) > 5