

import turtle
import random
# Töö3
# 
# Kilpkonn
# Kirjutada programm, mis lubab kasutajal valida kujundite tüübi
# (viisnurk, ring, ruut või suvaline) ja arvu.
# Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul,
# kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# 
# Kõik kujundite joonistamise käsud peavad olema kirjutatud eraldi funktsioonidesse.
# Näiteks funktsioon joonista_ruut() või joonista_viisnurk().
# Pärast joonistamist peab programm pakkuma võimalust sisestada uued väärtused
# või väljuda programmist, jättes sisendi tühjaks.
# 
# Näiteks:
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Soovid jätkata?

#suvaline
# suvaline = random.randint()

kujund = input("1)viisnurk \n2)ring \n3)ruut \n4)suvaline \nMillist kujundit soovid joonistada: ")
arv = int(input("Mitu kujundit soovid joonistada?: "))
# input("Soovid jätkata?: "

kylg =90
# viisnurk
def viisnurk(kylg):
    for i in range(5):
        turtle.fd(kylg)
        turtle.rt(144)
        
# ring
def ring(kylg):
    turtle.circle(kylg)

# ruut
def ruut(kylg):
    for i in range(4):
        turtle.fd(kylg)
        turtle.lt(90)

#suvaline
def suvaline(kylg):
    kujund(random.choice("1", "2", "3"))
    arv(random.choice)
    
    
# kujundite joonistamine   
if kujund=="1":
    for i in range(arv):
        viisnurk(kylg)
        turtle.lt(kylg * 1.5)
        
elif kujund=="2":
    for i in range(arv):
        ring(kylg)
        turtle.lt(kylg * 1.5)
        
elif kujund=="3":
    for i in range(arv):
        ruut(kylg)
        turtle.lt(kylg * 1.5)
        
elif kujund=="4":
    for i in range(arv):
        suvaline(kylg)
    
    
else:
    pass
        





turtle.done()