def sort(str1, str2):
    ord_list1 = []
    ord_list2 = []
    in_order_str1 = "".join(sorted(str1))
    in_order_str2 = "".join(sorted(str2))
    ord_list1.append(in_order_str1)
    ord_list2.append(in_order_str2)
    return ord_list1, ord_list2
                     
def permutation(str1, str2, lists):
    i = 0
    a, b = lists
    if len(str1) != len(str2):
        print("Not even the same size")
        return False
    for i in range(len(str1)):
        if a[i] == b[i]:
            print("Looks like a permutation")
        else:
            print("Try again")
            return False
        return True
            
def main():
    str1 = "septemb"
    str2 = "betspme"
    sort(str1, str2)
    permutation(str1, str2, sort(str1, str2)) 

    
if __name__ == '__main__':
    main()
