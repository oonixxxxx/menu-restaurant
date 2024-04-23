def f(n):
    if n == 0:
        return 0
    else:
        if n>0 and n%2==0:
            return f(n // 2)
        else:
            if n%2!=0:
                return 1 + f