def start1():
    try:
        a, b, c, d = int(input('Число1: ')), int(input('Число2: ')), int(input('Число3: ')), int(input('Число4: '))
    except ValueError:
        print("Ниггер, вводи только числа")
        return start1()
    else:
        if a > b:
            if a > c:
                p = a % d
                print(p)
            else:
                p = b % d
                print(p)
        else:
            p = (b+c) % d
            print(p)


start1()
