def test():
    a = (0 + 1) * (0 + 1)   # true
    b = (0 + 1) * (0 * 1)   # false
    c = (True or False) and (not(False or True))   # false
    d = not(True or True)
    e = (1 + 0) * (1 * 1)
    f = (True or True) or (True and False)
    g = (bool(1 + 1)) or not(False and True)
    print(a, b, int(c), int(d), e, int(f), int(g))


test()
