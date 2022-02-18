import math, random
screen = ""
radius = 5 #Radius of circle
mode = 1 #0 - random symbol, 1 - distributes text in a circle
symbols = "Hello :) " #Symbols or text that would be used to generate a circle
i = -1
x = (0 - radius / 2) * 8
y = (radius / 2) * 8
while y > (0 - radius / 2) * 8:
    y -= 2
    x = (0 - radius / 2) * 8
    while x < (radius / 2) * 8:
        x += 1
        if ((math.sqrt((0 - x) ** 2 + (0 - y) ** 2) - radius) < radius * 1.75): #If distance to 0 - size of circle < distance - draw circle
            i += 1
            if mode == 1:
                screen += symbols[i % len(symbols)]
            elif mode == 0:
                screen += symbols[math.floor(random.random() * len(symbols))]
        else:
            screen += "⠀"
    screen += "\n"
print(screen) #Printing circle