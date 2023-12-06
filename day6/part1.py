
test = """Time:      7  15   30
Distance:  9  40  200"""


def parser(data):
    data = data.split("\n")
    time = tuple(map(int,data[0].split(":")[1].split()))
    distance = tuple(map(int,data[1].split(":")[1].split()))
    races = [(time[i],distance[i]) for i in range(len(time))]
    return (races)

def errrormargin(time,distance):
    wins = 0
    for i in range(1,time):
        if (time - i) * i > distance:
            wins += 1
    return wins

def main(data):
    races = parser(data)
    error = 1

    for time,distance in races:
        error *= errrormargin(time,distance)
    
    print(error) 



with open("data.txt") as file:
    input = file.read()
    main(input)

