import math
test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""



constraints1 =  {
    "red":12,
    "green":13,
    "blue":14

}
constraints =  {
    "red":12,
    "green":13,
    "blue":14

}


def linespliter(line):
    gameno = line.split(":")[0].split()[-1]
    sets = line.split(":")[-1]
    sets = sets.split(";")
    sets = [i.split(',') for i in sets]
    sets = [[tuple(j.split(" "))[1:] for j in i] for i in sets]
    
    # print(gameno,test)
    mins = minpowers(sets)
    total = mins["red"] * mins["green"] * mins["blue"]

    # print(total)
    return total


def minpowers(sets):
    mins = {
        "red":-math.inf,
        "green":-math.inf,
        "blue":-math.inf

        }
    

    for setn in sets:
        for colors in setn:
            if mins[colors[-1]] < int(colors[0]):
                mins[colors[-1]] = int(colors[0])
    return mins



def solve(sets,gameno):
    for setn in sets:
        for colors in setn:
            if constraints[colors[-1]] < int(colors[0]):
                print(gameno)
                return False
    return True




def problem2(data):
    total = []
    for line in data.split("\n"):
        total.append(linespliter(line))
    print(sum(total))





with open("data.txt") as f:
    data = f.read()
    problem2(data)