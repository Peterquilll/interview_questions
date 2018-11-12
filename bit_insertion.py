def insertion(n, m, i, j):
    all_ones = ~0
    left = all_ones << (j + 1)
    right = ((1 << i) - 1)
    mask = left | right
    n_cleared = n & mask
    m_shifted = m << i
    return(n_cleared | m_shifted)

def main():
    n = 0x400
    m = 0x13
    i = 2
    j = 6
    print(bin(insertion(n, m, i, j)))

if __name__ == '__main__':
    main()
    
