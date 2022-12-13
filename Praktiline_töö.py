from math import *
from random import *
#13/12/22
try:
    vanus=int(input("Kui vana sa oled?"))
except:
    print("!!!!!!")
if vanus==18:
    luba=int(input("Kas lubate vanematele hindeid vaadata?"))

elif vanus==14 or vanus==15 or vanus==16 or vanus==17: #and , or, not !=ei võrdu, <, >, >=, <=
    print("Automaatne juurdepääs vanematele")
else: 
    print("Viga!")






try:
     päev=int(input("Mis päev ja mitu tundi täna on ?"))
except:
     print("!!!!!!!")
if   päev==1:
    n="Esmaspäev"
    n="6 tundi"
elif päev==2:
    n="Teisipäev"
    n="8 tundi"
elif päev==3:
    n="Kolmapäev"
    n="6 tundi"
elif päev==4:
    n="Neljapäev"
    n="5 tundi"
elif päev==5:
    n="Reede"
    n="7 tundi"
elif päev==6:
    n="Laupäev"
    n="0 tundi"
elif päev==7:
    n="Pühapäev"
    n="0 tundi"
else: 
    n="vale number"
print(n)










r=randint(-100,100)
a=randint(-100,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr:
        print(f"Ruud´u pindala {Skv} on suurem ringi pindala {Skr}")
    elif Skr>Skv:
        print(f"Ruud´u pindala {Skv} on suurem ringi pindala {Skr}")
    else:
        print("Pindalad on võrdsed. {Skr m^2}")
else:
     print(f"{a} ja {r} paevad > kui 0 olla")

print()
    
  
  
  
  
  #Days 
from math import *
from random import * 
try:
     päev=int(input("Mis päev täna on?"))
except:
     print("!!!!!!!")
if   päev==1:
    n="Esmaspäev"
elif päev==2:
    n="Teisipäev"
elif päev==3:
    n="Kolmapäev"
elif päev==4:
    n="Neljapäev"
elif päev==5:
    print="Reede"
elif päev==6:
    n="Laupäev"
elif päev==7:
    n="Pühapäev"
else: 
    n="vale number"
print(n)
print("Viga")
    



#12/12/22
from math import *
from random import * 
try:
    hinne=int(input("Mis hinne täna said koolis"))
except:
    print("!!!!!!")
if hinne==5:
    print("Väga hea!")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Rahuldav!")
elif hinne==2 or hinne==1: #and , or, not !=ei võrdu, <, >, >=, <=
    print("Lastekodu!")
else: 
    print("Viga!")

    
  









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

try:
   a=int(input("Number:"))
except:
    print("Vale andmetüüp!")
    a=0
try:
    b=int(input("Number:"))
except:
    print("Vale andmetüüp!")
    b=0
try:
    c=int(input("Number:"))
except:
        print("Vale andmetüüp!")
        c=0
try:
    d=int(input("Number:"))
except:
    print("Vale andmetüüp!")
    d=0
try:
    e=int(input("Number:"))
except:
    print("Vale andmetüüp!")
    e=0
p=(a+b+c+d+e)/5
print(f"Vastus:keskmise suvalisest on {p}")



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


#1 
print("Puu läbimõõdu arvutamine")
try:
    C=float(input("Puu ümbermõõt: "))
except:print("Vale andmetüüp")
d=2*(C/(2*pi))
print(f"Vaastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d }")
