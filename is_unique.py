def is_unique(string):
    if len(string) > 128:
        return False
    char_set = [False for i in range(128)] #list comprehension                  
    '''                                                                         
    char_set = []                                                               
    for i in range(128):                                                        
         char_set.append(False)                                                 
    '''
    i = 0
                                     
    while i < len(string):
        val = ord(string[i])
        if char_set[val]:
            return False
        char_set[val] = True
        i += 1
    return True


def main():
    test_string = "talk"
    print(is_unique(test_string))


if __name__ == '__main__':
    main()
