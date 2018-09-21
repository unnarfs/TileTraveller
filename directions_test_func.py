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

    return all_directions

print_directions("nes")