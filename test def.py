def w (x, y):
    o=1
    for i in range(1,2):
        print("*" * int((x+x/3)))
    while o < (y-2) :
        print("*", " " * (x-2), "*")
        o=o+1
    for i in range(1,2):
        print("*" * int((x+x/3)))

x = int(input("Podaj wysokość"))
y = int(input("Podaj szerokość"))

w(x, y)
