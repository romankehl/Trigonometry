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
        h = float(input("hypothenuse: ").strip())
alpha = math.radians(float(input("Alpha: ").strip()))
beta = math.radians(float(input("Beta; ").strip()))

#Define functions
def sin_w_gh():
    wah = math.asin(h / g)
    wah = math.degrees(wah)
    print(wah)
if g + h > 0:
    sin_w_gh()
else:
    print("no value")

def sin_a_hw():
    ahw = 3