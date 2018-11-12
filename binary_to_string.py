def decimal_to_binary(d):
    r = d
    b = ['.']
    i = 0
    while r > 0:
        r = r * 2
        if r >= 1:
            b.append('1')
            r = r - 1
        else:
            b.append('0')
        i +=1
        if i >= 32:
            return 'Error'
            
    return "".join(b)

def main():
    d = .625
    result = decimal_to_binary(d)
    print(result)

if __name__ == '__main__':
    main()
