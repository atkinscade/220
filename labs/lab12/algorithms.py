

def read_data(file):
    with open(file) as f:
        lines = f.read()
        numbers = lines.split()
    return numbers


def is_in_linear(val, inlist):
    print(inlist)
    if str(val) in inlist:
        return print('True')
    else:
        return print('False')
