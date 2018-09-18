"""
Taka punkt sem byrjar á hnitum x, y = 1 og færa hann í gegnum völundarhús. Hann verður að vera innan 1 < x, y < 3.
Eftirfarandi hreyfingar eru ekki leyfðar (veggir):
1,1 -> má bara fara norður
2,2 -> má bara fara suður eða vestur
2,1 -> má bara fara norður
2,3 -> má bara fara vestur eða austur
3,2 -> má bara fara norður eða suður
"""

#Breytur fyrir hreyfingu leikmannsins í völundarhúsinu
x = 1
y = 1
#Strengur fyrir innslátt áttar sem ferðast á í
str_movement = ""


#while lykkja sem keyrir þangað til að x = 3 og y = 1
while x != 3 or y != 1:
    if x == 1 and y == 1: #1,1
        print("You can travel: (N)orth.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n":
            print("Not a valid direction!")
            str_movement = input("Direction: ")
            str_movement = str_movement.lower()
        y += 1
    elif x == 1 and y == 2: #1,2
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n" or str_movement != "e" or str_movement != "s":
            if str_movement == "n":
                y += 1
                break
            elif str_movement == "e":
                x += 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 1 and y == 3: #1,3
        print("You can travel: (E)ast or (S)outh.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "e" or str_movement != "s":
            if str_movement == "e":
                x += 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 2 and y == 1: #2,1
        print("You can travel: (N)orth.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n":
            print("Not a valid direction!")
            str_movement = input("Direction: ")
            str_movement = str_movement.lower()
        y += 1
    elif x == 2 and y == 2: #2,2
        print("You can travel: (S)outh or (W)est.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "s" or str_movement != "w":
            if str_movement == "w":
                x -= 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 2 and y == 3: #2,3
        print("You can travel: (E)ast or (W)est.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "e" or str_movement != "w":
            if str_movement == "w":
                x -= 1
                break
            elif str_movement == "e":
                x += 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 3 and y == 3: #3,3
        print("You can travel: (S)outh or (W)est.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "s" or str_movement != "w":
            if str_movement == "w":
                x -= 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 3 and y == 2: #3,2
        print("You can travel: (N)orth or (S)outh.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n" or str_movement != "s":
            if str_movement == "n":
                y += 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()

#Lykkjan búin og þar með sigrinum náð, prenta það.
print("Victory!")

