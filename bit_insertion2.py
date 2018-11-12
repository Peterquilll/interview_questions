def insert_end(m, n, j, i):
    v = 0xffff
    left_end = v <<  j + 1
    right_end = v << i
    invert_end = right_end ^ v
    print(bin(invert_end))
    cleared_row = n & left_end
    preserved_end = n & invert_end
    insertion = cleared_row | m << i
    result = insertion | preserved_end
    return result

def main():
    n = int("10000000000", 2)
    m = int("10011", 2)
    j = 7
    i = 2
    result = insert_end(m, n, j, i)
    print(bin(result))

if __name__ == '__main__':
    main()
