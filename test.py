def func1():
        a = 8
        b = 9
	return a, b


def func2(x, y, func):
        a, b = func()
        z = x + y + a + b
        return z


def main():
        a = func2(4, 6, func1)
        print(a)

if __name__ == '__main__':
        main()
