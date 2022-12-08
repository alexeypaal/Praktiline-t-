#10
from math import * 
print("Ajateisendus")
v=float(input("aja minutites:"))
s=int(v%60)
t=int(v//60)
print(f"minutes {t}:sekundid {s}")




#9
from math import *
print ("Rulluisutajad")
print("Rulluidutaja keskmine kiirus on 39.9 km/h")
m=24/60
t=m*29.9
t=round(t,2)
print(f"Vastus:{t}km")
print()





#8
from math import *
print ("Kütusekulu ")
l=float(input (" Tangitud kütuse liitrid "))
km=float(input (" Läbitud kilomeetrid "))
pr=(l/km)*100   #liitrid iga sada kilometrid 
print(str(f"Vastus: {pr}l/km"))





#7
from math import *
print ("Jätate teenindajale 10% jootraha")
s=10*12.9/100
s=round(s)
d=(12.9+s)
print(f"Vastus: {d}")
p=d/3
p=round(p,1)
print(f"iga lollpea peab:")
print()




#6
from random import randint 
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\Külg b={b}\nKülg c={c}")
print(f"Kolmnurga ümbermõõt= {a+b+c}")
print()



#5
print("    @..@")
print ("  (----)" )
print( " ( \__/ )" )
print( " ^^ "" ^^ " )  



#4
from math import * 
print("aritmeetilise keskmise ")
A1=int(input ("Sisesta 1. arv => "))
A2=int(input ("Sisesta 2. arv => "))
A3=int(input ("Sisesta 3. arv => "))
A4=int(input ("Sisesta 4. arv => "))
A5=int(input ("Sisesta 5. arv => "))
K=(A1+A2+A3+A4+A5 )/ 5 
print(f"keskmine on {keskmine}")



#3
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg 

print("Sinu kiirus oli " + str(kiirus) + " km/h")


#2
from math import * 
print(" Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus =>"))
d=sqrt(N**2+M**2)
print ("Maatüki diagonaal on {d} m**2")


#1from math import * 
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vaastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d }")
