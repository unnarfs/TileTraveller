"""
https://github.com/unnarfs/TileTraveller

Answers:
1. The second implementation was easier because it allowed me to break the problem into smaller chunks, which I could then tackle individually.
2. The second implementation is easier to read because it's much easier to follow along what is happening in the code
3. It was possible to reduce the amount of repeat code by a large amount since the functions can be called when needed rather than having those lines of code for each separate instance.


Taka punkt sem byrjar á hnitum x, y = 1 og færa hann í gegnum völundarhús. Hann verður að vera innan 1 < x, y < 3.
Eftirfarandi hreyfingar eru ekki leyfðar (veggir):
1,1 -> má bara fara norður
2,2 -> má bara fara suður eða vestur
2,1 -> má bara fara norður
2,3 -> má bara fara vestur eða austur
3,2 -> má bara fara norður eða suður
"""



def pull_a_lever(coins):
    choice = input("Pull a lever (y/n): ")
    choice = choice.lower()
    if choice == "y":
        coins += 1
        print("You received 1 coins, your total is now {}.".format(coins))
    return coins

def valid_directions(x, y, coins):
    #Tekur við stöðu notanda í völundarhúsinu og skilar streng með þeim áttum
    directions = ""
    if (x == 1 and y == 1) or (x == 2 and y == 1): #1,1
        directions = "n"
    elif x == 1 and y == 2: #1,2
        coins = pull_a_lever(coins)
        directions = "nes"
    elif x == 1 and y == 3: #1,3
        directions =  "es"
    elif (x == 2 and y == 2): #2,2
        coins = pull_a_lever(coins)
        directions = "sw"
    elif x == 2 and y == 3: #2,3
        coins = pull_a_lever(coins)
        directions = "ew"
    elif x == 3 and y == 2: #3,2
        coins = pull_a_lever(coins)
        directions = "ns"
    elif x == 3 and y == 3: #3,3
        directions = "sw"
    return directions, coins

def print_directions(directions):
    #Fall sem tekur inn streng, fer í gegnum hann og bætir áttum við strenginn og prentar út
    all_directions = "You can travel: "
    temp_string = directions
    for chars in temp_string:
        if "n" in temp_string:
            all_directions += "(N)orth"
            if len(temp_string) > 1:
                all_directions += " or "
            temp_string = temp_string.replace("n", "")
        elif "e" in temp_string:
            all_directions += "(E)ast"
            if len(temp_string) > 1:
                all_directions += " or "
            temp_string = temp_string.replace("e", "")    
        elif "s" in temp_string:
            all_directions += "(S)outh"
            if len(temp_string) > 1:
                all_directions += " or "
            temp_string = temp_string.replace("s", "")
        elif "w" in temp_string:
            all_directions += "(W)est"
    all_directions += "."
    print(all_directions)
    #return directions



def direction(valid_directions):
    #Kannar hvaða átt notandinn slær inn og athugar hvort að það er átt sem er í lagi og skilar svo áttinni sem notandinn færir sig í
    str_movement = input("Direction: ")
    str_movement = str_movement.lower()
    while str_movement not in valid_directions:
        print("Not a valid direction!")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
    return str_movement

def mov_arithmetic(x, y, str_direction):
    #Tekur við núverandi stöðu x,y í hnitakerfinu og áttin sem notandi vill hreyfa sig í. Skilar tuple sem mig minnir að maður þurfi
    #að afpakka með því að kalla í fallið með "x, y = mov_arithmetic(x,y,str_direction)"
    if str_direction == "n":
        y += 1
    elif str_direction == "s":
        y -= 1
    elif str_direction == "e":
        x += 1
    elif str_direction == "w":
        x -= 1
    return x,y

#Strengir til að senda í föllin
str_wherecanto = ""
str_checkdirection = ""

def play():
    #Breytur
    choice = ""
    x = 1
    y = 1
    coins = 0
    while x != 3 or y != 1:
        str_wherecanto, coins = valid_directions(x,y, coins)
        print_directions(str_wherecanto)
        str_checkdirection = direction(str_wherecanto)
        x, y = mov_arithmetic(x, y, str_checkdirection)
    print("Victory!")
    choice = input("Play again (y/n): ")
    choice = choice.lower()
    if choice == "y":
        play()

play()
