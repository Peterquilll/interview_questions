n = int(input("steps: "))
dic = {}
def count_steps(n , dic):
    if dic.get(n):
        print(dic[n])
    else:
        if n < 0:
            print(0)
        elif n == 0:
            print(1)
        else:
            a = n - 1
            b = a - 1
            c = b - 1
            result = a + b + c
            print(result)
            dic[n] = result


if __name__ == '__main__':
    count_steps(n, dic)

            
        
    
