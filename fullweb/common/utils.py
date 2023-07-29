def percent_factor(value):
    factor = 10 ** (len(str(int(value)))-1)
    bigger_nearest = ((value // factor) + 2) * factor
    return value / bigger_nearest * 100

def bar_length(value):
    if value < 5:
        return 5
    return value