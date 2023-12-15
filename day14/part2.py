
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

        self.cache ={}
        self.pack = ""

        self.docycle(1000000000) 

    def docycle(self,no):
        self.copy = [(lst) for lst in self.data]
        self.cache = []
        
 
              

        while self.pp() not in self.cache:
            self.cache.append(self.pp())
            self.cycle()
        start = self.cache.index(self.pp())
        i = len(self.cache)

        self.data = [list(lst) for lst in self.cache[(no - i)  % (start - i) + i ].split("\n")]
       
  


        print(self.calload())
      
    
    def cycle(self):
        self.shiftN()
        self.shiftW()
        self.shiftS()
        self.shiftE()


    def pp(self):
        self.pack = "\n".join(["".join(lst) for lst in self.data])
        return self.pack

        

    def display(self):
        for lst in self.data:
            print("".join(lst))
        print()
    
    def shiftN(self):
        
        for idy,row in enumerate(self.data):
            for idx ,tile in enumerate(row):
                if tile == "O":
                    newy = idy - 1
                    while newy >= 0 and self.data[newy][idx] == ".":
                        self.data[newy][idx] = "O"
                        self.data[newy + 1][idx]  = "."
                        newy -=1
    def shiftS(self):
        self.reverse()
        self.shiftN()
        self.reverse()
    
    def shiftE(self):
        self.transpose()
        self.shiftS()
        self.transpose()
    
    def shiftW(self):
        self.transpose()
        self.shiftN()
        self.transpose()

    def reverse(self):
        self.data.reverse()
    
    def transpose(self):
        self.copy = [lst.copy() for lst in self.data]

        for j in range(len(self.data)):
            for i in range(len(self.data[0])):
            
                self.copy[i][j] = self.data[j][i]
        
        self.data = self.copy


    def calload(self):
        load = 0
        for idy,row in enumerate(self.data):
            for idx ,tile in enumerate(row):
                if tile == "O":
                    load += len(self.data) - idy
        # print(load)
        return load


with open("day14/data.txt") as file:
    input_data = file.read()
    main(input_data)

