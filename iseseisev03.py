

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
# random.choice valib suvaliselt ühe kujundi kolmest.        
def suvaline(kylg):
    random.choice((viisnurk, ring, ruut))(kylg)
    
    
# kujundite joonistamine
# while loop
while True:
# küsib kujundit
    kujund = input("1)viisnurk \n2)ring \n3)ruut \n4)suvaline \nMillist kujundit soovid joonistada: ")
# küsib kujundi arvu
    arv = int(input("Mitu kujundit soovid joonistada?: "))
# kujundite kordus(arv) ja liikumine joonistamisel
    for i in range(arv):
        turtle.penup()
        turtle.goto(random.randint(-300, 300),random.randint(-300, 300)) 
        turtle.pendown()
# valik    
        if kujund=="1":
            viisnurk(kylg)
        
        elif kujund=="2":
            ring(kylg)
       
        
        elif kujund=="3":
            ruut(kylg)
       
        
        elif kujund=="4":
            suvaline(kylg)
    
# vale vastuse sisestamisel    
        else:
            print("Valik puudub, pese silmad ära!")
            break
# programmi jätkamine, kirjutades kõike muud peale "ei", programm jätkub            
    kysimus = input("Kas soovid jätkata?: ")
    if kysimus=="ei":
        break
        





turtle.done()