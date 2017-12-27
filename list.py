print(list(range(1, 11)))

print(range(1, 5))

print(list(x * x for x in range(1, 10)))

print(list(x * x for x in range(1, 10) if(x % 2) == 0))

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print(key+'='+value for key, value in d.items())
