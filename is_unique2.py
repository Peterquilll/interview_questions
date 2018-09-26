def is_unique1(string):
    if len(string) > 256:
        return False

    list1 = []
    i = 0
    l = 256
    for n in range(l):
        list1.append(False)
        i += 1
    for c in string:
        d = ord(c)
        if list1[d] is True:
            return False
        list1[d] = True
    return True

def if_unique_party(was_unique):
    if was_unique is True:
        print("!!!!!!!!!!!")

def main():
    string = 'dog'
    was_unique = is_unique1(string)  # assign the RESULT of a function call to a variable
    v = is_unique1  # assign a function to a variable
    print(was_unique)
    if_unique_party(was_unique)
    

if __name__ == '__main__':
    main()
