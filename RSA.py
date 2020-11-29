

def Euclide(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a+b

Q = int(input("Введите q: "))
P = int(input("Введите p: "))
n = P*Q
euler = (P-1)*(Q-1)
e = 2
while Euclide(e, euler) != 1:
    e += 1
print(e)
i = 2
d = 0
while True:
    d = (i*euler+1)/e
    if int(d) == d:
        break
    i += 1
print(f'Закрытый ключ ({int(d)},{n})')
print(f'Открытый ключ ({e},{n})')
