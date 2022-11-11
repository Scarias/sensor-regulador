def out_range(frame):
    if float(frame.body.split(',')[0]) < 0 or float(frame.body.split(',')[0]) > 5:
        return '%s: abnormal value at sensors %s'


def luminosity_level(frame):
    result_msg = out_range(frame)
    if not result_msg:
        result = float(frame.body.split(',')[0])
        if 0 <= result < 1.5:
            result_msg = '%s: low luminosity at sensors %s'
        elif 1.5 <= result < 3.5:
            result_msg = '%s: medium luminosity at sensors %s'
        else:
            result_msg = '%s: high luminosity at sensors %s'

    if result_msg:
        return result_msg % tuple(frame.body.split(','))