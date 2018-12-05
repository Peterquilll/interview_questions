def get_next(n):
    c = n
    c0 = 0
    c1 = 0

    while c & 1 == 0 and c != 0:
        c0 += 1
        c = c >> 1

    while c & 1 == 1:
        c1 += 1
        c = c >> 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1

    n = n | (1 << p)
    n = n & ~((1 << p) - 1)
    n = n | (1 << (c1-1)) -1

    return n

def get_previous(n):
    temp = n
    c0 = 0
    c1 = 0

    while temp & 1 == 1:
        c1 += 1
        temp = temp >> 1

    if temp == 0:
        return -1

    while temp & 1 == 0 and temp != 0:
        c0 += 1
        temp = temp >> 1

    p = c0 + c1
    n = n & ((~0) << p + 1)
    mask = ( 1 << ( c1 + 1)) - 1
    n = n | mask << (c0 -1)
    return n


def main():
    n = 0x2783
    result1 = get_next(n)
    result2 = get_previous(n)
    print("n = ", n)
    print("get_next = ", bin(result1))
    print("get_previous = ", bin(result2)) 

if __name__ == '__main__':
    main()
