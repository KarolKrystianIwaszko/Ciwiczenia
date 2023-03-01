def nwzz(o):
    i=0
    a=int(input('Wprowadź dane'))
    maks = a
    if maks<a:
         maks=a  
    while i+1 < o:
        a=int(input('Wprowadź dane'))
        if maks<a:
            maks=a
        i=i+1
    return maks
n = int(input('ile danych chcesz wprowadzić?'))
print('Najwiękrza liczba',nwzz(n))
