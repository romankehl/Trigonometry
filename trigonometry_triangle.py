import math

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
    if a == 0 or g == 0:
        return None
    else:
        while True:
            try:
                waag = math.degrees(math.atan(g / a))
                return waag
            except ZeroDivisionError:
                waag = None
                break
            else:
                break

def wa_ah():
    if a == 0 or h == 0:
        return None
    else:
        while True:
            try:
                waah = math.degrees(math.acos(a / h))
                return waah
            except ZeroDivisionError:
                waah = None
                break
            else:
                break

def wa_gh():
    if g == 0 or h == 0:
        return None
    else:
        while True:
            try:
                wagh = math.degrees(math.asin(g / h))
                return wagh
            except ZeroDivisionError:
                wagh = None
                break
            else:
                break

def wa_wb():
    wawb = math.degrees(math.radians(90) - beta)
    return wawb


#printing functions of alpha
while True:
    if alpha > 0:
        break
    elif a > 0 and g > 0:
        print(f"Alpha: {wa_ag()}°")
        break
    elif a > 0 and h > 0:
        print(f"Alpha: {wa_ah()}°")
        break
    elif g > 0 and h > 0:
        print(f"Alpha: {wa_gh()}°")
        break
    else:
        print(f"Alpha: {wa_wb()}°")
        break



