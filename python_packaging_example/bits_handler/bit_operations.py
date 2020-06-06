from bitarray import bitarray

def add(first, second):
    a = bitarray(first)
    b = bitarray(second)
    c = a & b
    print(c)
    return c