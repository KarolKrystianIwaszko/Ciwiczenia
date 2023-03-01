N = int(input('Wprowadź ilość danych w zbiorze'))
a = [0] * N
def wprowadź():
    for i in range(N):
        a[i] = int(input('Podaj liczbę:'))
def wyprowadź():
    for i in range(N):
        print(a[i])
def wyszukaj(w):
    for i in range(N):
        if a[i] == w:
            return i
    return 'nie ma'

wprowadź()
print('wprowadzone dane:')
wyprowadź()
w = int(input('Podaj czego szukasz:'))
p = wyszukaj(w)
if p >= 0:
    print('Znaleziono',w,'na pozycji',p+1)
else:
    print('nie znaleziono danej-',w)
