i=0
while i == 0:
    a=int(input("Pierwsza liczba"))
    b=int(input("Druga liczba"))
    if b != 0:
        if a%b == 0:
            print("Liczba",a,"jest podzielna przez",b)
        else:
            print("Liczba",a,"nie jest podzielna przez",b)
    else:
        print("niedziel przez 0 cholere")
        
    c=str(input("Exit?(y)"))
    if c == "y":
        i=1
