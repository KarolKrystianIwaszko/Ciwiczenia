def p(l):
    if l == 0:
            print(l)
    else:
        while l!=0:
            c=l%10
            print(c)
            l = l // 10
for i in range(10):
    l=int(input("Podaj liczbe"))
    print("Cyfry liczby",l,"od ostatniej")
    p(l)


