def p (b):
    a=1
    for i in range(10000):
        if b < a*a:
            a=a
        if b < a*a:
            a=a+0.0001
        if b > a*a:
            a=a-0.0001
    return a

c=int(input("Podaj liczbe do spierwiastkowania"))
print("pierwiatek z",c,"wynosi",p(c))
