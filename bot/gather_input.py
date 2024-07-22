import csv
import numpy as np



def read_inputs(filename, delim=','):
    f = open(filename, 'r')

    reader = csv.reader(f, delimiter=delim)

    raw = []

    first_row = True
    for row in reader:
        if not first_row:
            raw.append(list(map(lambda x: int(x), row)))
        else:
            raw.append(row)
            first_row = not first_row


    f.close()
    return (np.array(raw[0]), np.array(raw[1:]))


