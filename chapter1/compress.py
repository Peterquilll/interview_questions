def compress(string):
    compressed_string = []
    count_consecutive = 0
    i = 0
    while i < len(string):
        count_consecutive += 1
        if (i + 1 >= len(string) or string[i] != string[i +1]):
            compressed_string.append(string[i])
            compressed_string.append(count_consecutive)
            count_consecutive = 0
        i += 1
    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return String

def main():
    string = "abbbccddddd"
    result = compress(string)
    print(result)

if __name__ == '__main__':
    main()
        
            
