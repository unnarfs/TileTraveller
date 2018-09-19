"""
https://github.com/unnarfs/TileTraveller

Answers:



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

def valid_directions(x,y):
    #Tekur við stöðu notanda í völundarhúsinu og prentar hvert hann má færa sig og skilar streng með þeim áttum
    if (x == 1 and y == 1) or (x == 2 and y == 1): #1,1
        print("You can travel: (N)orth.")
        return "n"
    elif x == 1 and y == 2: #1,2
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        return "nes"
    elif x == 1 and y == 3: #1,3
        print("You can travel: (E)ast or (S)outh.")
        return "es"
#    elif x == 2 and y == 1: #2,1 (má samþætta með 1,1)
#        print("You can travel: (N)orth.")
#        return "n"
    elif (x == 2 and y == 2) or (x == 3 and y == 3): #2,2
        print("You can travel: (S)outh or (W)est.")
        return "sw"
    elif x == 2 and y == 3: #2,3
        print("You can travel: (E)ast or (W)est.")
        return "ew"
#    elif x == 3 and y == 3: #3,3 (má samþætta með 2,2)
#        print("You can travel: (S)outh or (W)est.")
#        return "sw"
    elif x == 3 and y == 2: #3,2
        print("You can travel: (N)orth or (S)outh.")
        return "ns"
"""
def direction(valid_direction, valid_direction2 = "", valid_direction3 =):
    #Kannar hvaða átt notandinn slær inn og athugar hvort að það er átt sem er í lagi og skilar svo áttinni sem notandinn færir sig í
    str_movement = input("Direction: ")
    while str_movement != valid_direction or str_movement != valid_direction2 or str_movement != valid_direction3:
        print("Not a valid direction!")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
    if str_movement == valid_direction:
        return valid_direction
    elif str_movement == valid_direction2:
        return valid_direction2
    elif str_movement == valid_direction3:
        return valid_direction3
"""
str_valid = valid_directions(1,1)