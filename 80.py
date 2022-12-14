z=0
x=0
c=0
v=0
b=0
while (z<5):
    for i in [0,1,2,3,4]:
        print(i)
        print("-------------------------------------")
        z=z+1
        for i in range(5):
            print(i)
            x=x+1
            print("-------------------------------------")
            print(z,x,c,v,b)
            n = int(input("n:"))
            for i in range(n):
                print(i)
                c=c+1
                print("-------------------------------------")
                for i in range(5,15):
                    print(i)
                    v=v+1
                    print("-------------------------------------")
                    for i in range(15,55,5):
                        print(i)
                        b=b+1
                        print("-------------------------------------")
print(z,x,c,v,b)


