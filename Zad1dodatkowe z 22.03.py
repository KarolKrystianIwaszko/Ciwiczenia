
n = int(input('podaj n'))

a = int(input('podaj a'))
b = a-n
if b < 0:
  b=b*-1
najmniejsza_różnica = b
najbliżej_n = a
      
for i in range(4):
    a = int(input('podaj a'))
    b = a-n
    if b < 0:
      b=b*-1
    if b < najmniejsza_różnica:
      najmniejsza_różnica = b
      najbliżej_n = a
      
print('najbliżej na osi liczbowej do',n,'jest',najbliżej_n,'oddalona o ',najmniejsza_różnica)
  
