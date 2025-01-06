def start():
    try:
        k, m = int(input()), int(input())
    except ValueError:
        print("йоу нига вводи только числа")
    except Exception as e:
        print(e)
    else:
        if (k % m) == 3:
            p = k ** 3
            print(p)
        else:
            p = (m % k)
            print(p)


start()
