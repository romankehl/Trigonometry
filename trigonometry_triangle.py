import math

print("Die Angaben müssen aus Sicht von alpha geschen!")

#Get Inputs
while True: 
    try:
        a = float(input("Ankathete: ").strip()) #Ankathete von Winkel alpha
        if a == 0:
            a = None
    except ValueError:
        print("Ankathete muss eine Zahl sein!")
    else:
        break

while True:
    try:
        g = float(input("Gegenkathete: ").strip()) #Gegenkathete von winkel alpha
        if g == 0:
            g = None
    except ValueError:
        print("Gegenkathete muss eine Zahl sein!")
    else:
        break

while True:
    try:
        h = float(input("Hypothenuse: ").strip())
        if h == 0:
            h = None
    except ValueError:
        print("Hypothenuse muss eine Zahl sein!")
    else:
        break

while True:
    try:
        alpha = math.radians(float(input("Alpha: ").strip()))
        if alpha == 0:
            alpha = None
    except ValueError:
        print("Alpha muss eine Zahl sein!")
    else:
        break

while True:
    try:
        beta = math.radians(float(input("Beta: ").strip()))
        if beta == 0:
            beta = None
    except ValueError:
        print("Beta muss eine Zahl sein!")
    else:
        break

#Clear Terminal Window after all inputs are given
import os
os.system('cls')

#Printing Error message for no input
import sys
if a == None and g == None and h == None and alpha == None and beta == None: 
    sys.exit("Nicht genügend Inputs!\nstarte das Programm neu")

#Print Error message if only one side is inputed
if (a != None and g == None and h == None) or (g != None and a == None and h == None) or (h != None and a == None and g == None):
    if alpha == None and beta == None:
        sys.exit("Es müssen mindestens zwei Seiten gegeben sein!\nstarte das Programm neu")

 #Print Error message if h is bigger than a or g
if h == None:
    pass
elif a == None:
    if g > h:
        sys.exit("Die Hypothenuse ist grösser als die Gegenkathete!\nstarte das Programm neu")
elif g == None:
    if a > h:
        sys.exit("Die Hypothenuse ist grösser als die Gegenkathete!\nstarte das Programm neu")

#print Error message if alpha + beta != 90°
if alpha != None and beta != None:
    if alpha + beta != 90:
        sys.exit("Alpha und beta müssen zusammen 90° ergeben!\nstarte das Programm neu")

#Define functions for alpha
def wa_ag():
    return math.degrees(math.atan(g / a))
        
def wa_ah():
    return math.degrees(math.acos(a / h))

def wa_gh():
    return math.degrees(math.asin(g / h))

def wa_wb():
    return math.degrees(math.radians(90) - beta)

#printing functions of alpha
while True:
    if alpha != None:
        break
    elif a != None and g != None:
        print(f"Alpha: {wa_ag(): .3f}°")
        break
    elif a != None and h != None:
        print(f"Alpha: {wa_ah(): .3f}°")
        break
    elif g != None and h != None:
        print(f"Alpha: {wa_gh(): .3f}°")
        break
    else:
        print(f"Alpha: {wa_wb(): .3f}°")
        break


#Ankathete und Gegenkathete müssen für Beta getauscht werden

#Define functions for beta
def wb_ag():
        return math.degrees(math.atan(a / g))

def wb_ah():
        return math.degrees(math.acos(g / h))

def wb_gh():
        return math.degrees(math.asin(a / h))

def wb_wa():
        return math.degrees(math.radians(90) - alpha)

#printing functions of beta
while True:
    if beta != None:
        break
    elif a != None and g != None:
        print(f"Beta: {wb_ag(): .3f}°")
        break
    elif g != None and h != None:
        print(f"Beta: {wb_ah(): .3f}°")
        break
    elif a != None and h != None:
        print(f"Beta: {wb_gh(): .3f}°")
        break
    else:
        print(f"Beta: {wb_wa(): .3f}°")
        break

#Define functions for Ankathete
def a_gwa():
    return g / math.degrees(math.sin(alpha))

def a_gwb():
    return g * math.degrees(math.tan(beta))

def a_hwa():
    return h * math.degrees(math.cos(alpha))

def a_hwb():
    return h * math.degrees(math.sin(beta))

def a_gh():
    return math.sqrt(h**2 - g**2)

#print functions of Ankathete
while True:
    if a != None:
        break
    elif g != None and alpha != None:
        print(f"Ankathete: {a_gwa(): .3f}")
        break
    elif g != None and beta != None:
        print(f"Ankathete: {a_gwb(): .3f}")
        break
    elif h != None and alpha != None:
        print(f"Ankathete: {a_hwa(): .3f}")
        break
    elif h != None and beta != None:
        print(f"Ankathete: {a_hwb(): .3f}")
        break
    else:
        print(f"Ankathete: {a_gh(): .3f}")
        break
