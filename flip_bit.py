def flip_bit(a):
    current_len = 0
    previous_len = 0
    max_len = 1
    INT_BYTE = 4

    if ~a == 0:
        return INT_BYTE * 8

    while a != 0:
        if a & 1 == 1:
            current_len  += 1
        elif a & 1 == 0:
            if a & 2 == 0:
                previous_len = 0
            else:
                previous_len = current_len

            current_len = 0

        max_len = max((previous_len + current_len + 1), max_len)

        a = a >> 1

    return max_len

def main():
    a = 0x6EF #0110 1110 1111
    result = flip_bit(a)
    print(result)

if __name__ == '__main__':
    main()
