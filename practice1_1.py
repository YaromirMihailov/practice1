def dec(ac):
    def ob():
        ac()
        x = (v0 * t) + (ac() * t**2 / 2)
        print(x)
    return ob

@dec
def ac():
    a = (v - v0) / t
    print(a)
    return a
try:
    v0 = int(input())
    v = int(input())
    t = int(input())
    ac()
except ValueError:
    print('err: incorrect value')
except ZeroDivisionError:
    print('err: time can not be zero')


