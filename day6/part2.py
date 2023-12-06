
import math
test = """Time:      7  15   30
Distance:  9  40  200"""


def parser(data):
    data = data.split("\n")
    time = int("".join([i for i in data[0] if i.isdigit()]))
    distance = int("".join([i for i in data[1] if i.isdigit()]))

    return time,distance
    

def errrormargin(time,distance,rough = True):
    # ax^2 + bx + c
    a,b,c = -1,time,-distance
    solver = -(math.sqrt(b*b - 4 * a * c))/(a)
    solver = round(solver,1)
    if rough:

        return solver
    wins = 0
    for i in range(1,time):
        if (time - i) * i > distance:
            wins += 1
    return wins

def main(data):
    time,distance = parser(data)
    print(f"time: {time} distance: {distance}")
    error = errrormargin(time,distance,rough = True)
    print(error,"rough") 
    error = errrormargin(time,distance,rough = False)    
    print(error,"real") 



with open("day6/data.txt") as file:
    input = file.read()
    main(input)
   

