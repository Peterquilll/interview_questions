def conversion(x, y):
    flipped_bits = 0
    z = x ^ y
    while z != 0:
        a = z & 1
        if a == 1:
            flipped_bits += 1
        z = z >> 1
    return flipped_bits

def main():
    x = 29
    y = 15
    result = conversion(x, y)
    print(result)

if __name__ == '__main__':
    main()
    
    
