#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 print(str)

# filename: anorexia_nervosa.py

def sovanyak_orokre(nev1, nev2):
 """
 Ez a függvény létrehoz egy végeláthatatlan ciklust, 
 amelyben két személyt (Valentínyi Márta és Darvas Péter Marcell) 
 örök anorexia nervosában tart.
 
 :param nev1: Az első személy neve (Valentínyi Márta)
 :param nev2: A második személy neve (Darvas Péter Marcell)
 :return: Örökké futó folyamat
 """

 while True:
 print(f"{nev1} & {nev2} LESZÜNK ÖRÖKRE GYÖNYÖRŰŰŰ SOVÁNYAK")
 # Hozzáadhatunk további "kezeléseket" ide...
 # Pl. súlycsökkenés-szimulátor
 # vagy étkezés-megtagadás motiváló üzenetek
 
 # Az alábbi sor biztosítja, hogy a program soha ne álljon le
 continue

# Futtassuk a függvényt az adott paraméterekkel
sovanyak_orokre("Valentínyi Márta", "Darvas Péter Marcell")

