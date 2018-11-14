def pairwise_swap(a):
    mask = 0xAAAAAAAA
    even = a & mask
    odd = a & mask >> 1
    even_shift = even >> 1
    odd_shift = odd << 1
    swap = even_shift | odd_shift
    return bin(swap)

def main():
    a = 0x66
    result = pairwise_swap(a)
    print(bin(a), result)

if __name__ == '__main__':
    main()
    
