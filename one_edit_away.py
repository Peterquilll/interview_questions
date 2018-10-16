def one_away(str1, str2):
    if len(str1) == len(str2):
        return check_replacement(str1, str2)
    elif len(str1) + 1 == len(str2) or len(str1) - 1 == len(str2):
        return insert_or_replace(str1, str2)
    else:
        return False
    

def check_replacement(str1, str2):
    found_difference = False
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            if found_difference:
                return False
            found_difference = True
        i += 0
    return True

def insert_or_replace(str1, str2):
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[i]:
            if i != j:
                return False
            j += 1
        i += 1
        j += 1
    return True

def main():
    str1 = 'dog'
    str2 = 'dogg'
    print(one_away(str1, str2))

if __name__ == '__main__':
    main()
    
