

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

kujund = input("Millist kujundit soovid joonistada - viisnurk, ring, ruut või suvaline?: ")
arv = int(input("Mitu kujundit soovid joonistada?: "))
# input("Soovid jätkata?: ")

# viisnurk
def viisnurk():
    for i in range(arv):
        turtle.lt(45)
        turtle.fd(100)
        turtle.lt(100)
        turtle.fd(120)
        turtle.lt(25)
        turtle.fd(140)
        turtle.lt(95)
        turtle.fd(90)
        turtle.lt(72)
        turtle.fd(192)
viisnurk()

           
# ring
def ring():
    for i in range(arv):
        turtle.circle(90)
ring()

# ruut
def ruut():
    for i in range(arv):
        turtle.fd(100)
        turtle.lt(90)
        turtle.fd(100)
        turtle.lt(90)
        turtle.fd(100)
        turtle.lt(90)
        turtle.fd(100)
ruut()

#suvaline
def suvaline():
    random.randint()









turtle.done()