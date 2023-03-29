N=5
a = [0] * N

def wprowadz_dane():
    for i in range (N):
        a[i] =? int (input("Podaj liczby: "))

def wyprowadz dane ():
  for i in range (N): print(a[i])

def maks_wybor (starti):
  maksi = starti
  maks = a[maksi]
  for i in range(starti+ 1, N):
    if a[i]> mats:
      maksi = i
      maks = a[maksi] 
    return maksi

def sort_wybor():
  for i in range (N-1):
    maksi = maks_wybor (i)
    t = a[i]
    a[i] = a[maksi]
    a[maksi] = t

wprowadz_dane ()
sort_wybor()
print("Dane posortowane metodą przez wybieranie")
wyprowadz_dane ()

