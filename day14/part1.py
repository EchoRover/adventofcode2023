
test = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def parser(data):
    return [list(lst) for lst in data.split("\n")]

def main(data):
    data = parser(data)
    load = Load(data)
    
class Load:

    def __init__(self,data):
        self.data = data
        self.display()
        
        self.shitfN()

        self.display()

        self.calload()

    def display(self):
        for lst in self.data:
            print("".join(lst))
        print()
    
    def shitfN(self):
        
        for idy,row in enumerate(self.data):
            for idx ,tile in enumerate(row):
                if tile == "O":
                    newy = idy - 1
                    while newy >= 0 and self.data[newy][idx] == ".":
                        self.data[newy][idx] = "O"
                        self.data[newy + 1][idx]  = "."
                        newy -=1


    def calload(self):
        load = 0
        for idy,row in enumerate(self.data):
            for idx ,tile in enumerate(row):
                if tile == "O":
                    load += len(self.data) - idy
        print(load)


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

