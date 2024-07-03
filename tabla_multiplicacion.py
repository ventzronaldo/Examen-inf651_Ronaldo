a=int(input("ingrese un numero menor a 10: "))
b=10
if(a<10 and a>0):
    for i in range(1,b+1):
        print(i*a)
else:
    print("por favor introduce un numero menor que 10 y mayor que 0")
