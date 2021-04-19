def mygcd(x, y):
    if x == 0:
        return y
    else:
        return mygcd(y%x, x)
