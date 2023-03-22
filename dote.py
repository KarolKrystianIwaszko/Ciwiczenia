def najmniejsza(e,n):
    i=0
    a=int(input('Wprowadź dane'))
    minimum = a
    najmniejsza_reszta_z_dzielenia = a%n
    while i+1 < e:
        a=int(input('Wprowadź dane'))
        if najmniejsza_reszta_z_dzielenia > a%n:
            minimum=a
            najmniejsza_reszta_z_dzielenia = a%n
        i=i+1
    return minimum
e = int(input('ile danych chcesz wprowadzić?'))
n = int(input('podaj dzielnik?'))
na = najmniejsza(e,n)
print('Najmniejsza jest reszta z dzielenia',na,'równa',na%n )
