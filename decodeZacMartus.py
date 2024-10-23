def decode(encrypted):
    arr = ''
    for i in encrypted:
        arr = arr + str((int(i) - 3) % 10)
    return arr

