import math
from multiprocessing.sharedctypes import Value

#Get Inputs
while True: 
    try:
        a = float(input("Ankathete: ").strip())
    except ValueError:
        print("Ankathete muss eine Zahl sein!")
    else:
        break

while True:
    try:
        g = float(input("Gegenkathete: ").strip())
    except ValueError:
        print("Gegenkathete muss eine Zahl sein!")
    else:
        break

while True:
    try:
        h = float(input("Hypothenuse: ").strip())
    except ValueError:
        print("Hypothenuse muss eine Zahl sein!")
    else:
        break

while True:
    try:
        alpha = math.radians(float(input("Alpha: ").strip()))
    except ValueError:
        print("Alpha muss eine Zahl sein!")
    else:
        break

while True:
    try:
        beta = math.radians(float(input("Beta: ").strip()))
    except ValueError:
        print("Beta muss eine Zahl sein!")
    else:
        break

#Define functions for alpha
def wa_ag():
    waag = math.atan(g / a)
    waag = math.degrees(waag)
    return waag
    
def wa_ah():
    waah = math.acos(a / h)
    waah = math.degrees(waah)
    return waah

def wa_gh():
    wagh = math.asin(h / g)
    wagh = math.degrees(wagh)
    return wagh

def wa_wb():
    wawb = math.degrees(math.radians(90) - beta)
    return wawb

#Define functions for beta
def wb_ag():
    wbag = math.atan(g / a)
    wbag = math.degrees(wbag)
    return wbag
    
def wb_ah():
    wbah = math.acos(a / h)
    wbah = math.degrees(wbah)
    return wbah

def wb_gh():
    wbgh = math.asin(h / g)
    wbgh = math.degrees(wbgh)
    return wbgh

def wb_wa():
    wbwa = math.degrees(math.radians(90) - alpha)
    return wbwa


#printing functions of alpha
while True:
    if alpha > 0:
        break
    elif a + g > 0:
        print(f"Alpha: {wa_ag()}°")
        break
    elif a + h > 0:
        print(f"Alpha: {wa_ah()}°")
        break
    elif g + h > 0:
        print(f"Alpha: {wa_gh()}°")
        break
    else:
        print(f"Alpha: {wa_wb()}°")
        break

#printing functions of beta
while True:
    if beta > 0:
        break
    elif a + g > 0:
        print(f"Beta: {wb_ag()}°")
        break
    elif a + h > 0:
        print(f"Beta: {wb_ah()}°")
        break
    elif g + h > 0:
        print(f"Beta: {wb_gh()}°")
        break
    else:
        print(f"Beta: {wb_wa()}°")
        break



