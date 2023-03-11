#!/usr/bin/python3
def magic_calculation(a, b):
    c = 0
    for i in range(4, 6):
        c = add(c, i)
    return sub(a, b) if a < b else add(c, sub(a, b))

if __name__ == '__main__':
    from magic_calculation_102 import add, sub
    print(magic_calculation(1, 2))
    print(magic_calculation(4, 2))

