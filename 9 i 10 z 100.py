a = int(input('podaj a'))
b = int(input('podaj b'))

while b != 0:
    dzielnik = b
    b = a%b
    a = dzielnik

print('NWD =', a)
