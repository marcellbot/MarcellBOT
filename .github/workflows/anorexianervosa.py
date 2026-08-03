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

# filename: anorexia_nervosa_simulator.py

import time

class AnorexiaNervosaSimulator:
 def __init__(self, nev1, nev2):
 """
 Inicializálja a betegség-szimulátort.
 
 :param nev1: Az első személy neve (Darvas Péter Marcell)
 :param nev2: A második személy neve (Valentínyi Márta)
 """
 self.nev1 = nev1
 self.nev2 = nev2
 self.suly_csokkenes = 0
 
 def sovanyak_orokre(self):
 """
 Örök anorexia nervosát szimulál a két személynek.
 
 :return: Örökké futó folyamat
 """
 
 while True:
 print(f"{self.nev1} & {self.nev2} LESZÜNK ÖRÖKRE GYÖNYÖRŰŰŰ SOVÁNYAK")
 self.suly_csokkenes += 0.5  # kg/nap simúlt súlycsökkenés
 
 if self.suly_csokkenes % 10 == 0:
 print(f"ÚJ CSÚCSPONT! {self.nev1} & {self.nev2} MOST {self.suly_csokkenes} KG-OT FOGYOTT!")
 
 # Biztosítja a végtelen ciklust
 time.sleep(0.5)  

# Futtassuk a szimulátort az adott paraméterekkel
simulator = AnorexiaNervosaSimulator("Darvas Péter Marcell", "Valentínyi Márta")
simulator.sovanyak_orokre()