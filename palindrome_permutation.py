def palindrome_perm(string):
    pali_list = []
    char_range = 256
    for n in range(char_range):
        pali_list.append(0)
    for i in range(len(string)):
        d = ord(string[i])
        pali_list[d] += 1
    is_odd = False
    for n in pali_list:
        if n % 2 != 0:
            if is_odd:
                return False
            is_odd = True
    return True    
def main():
    string = 'civic'
    print(palindrome_perm(string))

if __name__ == '__main__':
    main()
    
