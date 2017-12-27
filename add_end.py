def add_end(L=[]):
    L.append('END')
    return L


add_end()
add_end()


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))


def calcnew(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calcnew(1, 2, 3, 4))

a = [2, 3, 4]
print('{}'.format(*a))
print('{}'.format(a))
print('{}'.format(a[1:2]))
print(*a)


def func(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


args = (5, 6, 7, 8)
kw = {'x': 99}
func(*args, **kw)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact1(1000))



