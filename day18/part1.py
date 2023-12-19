
test = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


def parser(data):
    data = data.split("\n")
    data = [lst.split() for lst in data]
    data = [[lst[0],int(lst[1]),lst[2][1:-1]] for lst in data]

    return data



def main(data):
    data = parser(data)
    dig = Digger(data)


class Digger:
    def __init__(self,data):
        self.data = data
        self.move = {"R":(1,0),"L":(-1,0),"U":(0,-1),"D":(0,1)}
        self.length = self.breadth = 0
        self.xpos = self.xneg = 0
        self.ypos = self.yneg = 0

        self.positions = []
        self.color = {}

        self.createborder()
        self.createmap()
        self.findvolumn()

    

    def createborder(self):
        self.x = self.y = 0

        for direction,times,hexcode in self.data:
            for i in range(times):
                self.positions.append([self.x,self.y])
                self.x += self.move[direction][0]
                self.y += self.move[direction][1]
                if hexcode not in self.color:
                    self.color[hexcode] = []
                self.color[hexcode].append([self.x,self.y])
         
                if self.x < 0:
                    self.xneg = max(abs(self.x),self.xneg)
                else:
                    self.xpos = max(self.x,self.xpos)
                if self.y < 0:
                    self.yneg = max(abs(self.y),self.yneg)
                else:
                    self.ypos = max(self.y,self.ypos)

                

        self.length += self.xneg + self.xpos  + 1
        self.breadth += self.yneg + self.ypos  + 1

       

        for i in self.positions:
            i[0] += self.xneg + 0
            i[1] += self.yneg + 0



        
        # print(self.length,self.breadth)
        # self.display()
    
    def findvolumn(self):


        self.positions = set(map(tuple,self.positions))
        self.stack = [(self.xneg + 1,self.yneg + 1)]
        self.seen = set()
        while not self.stack == []:
            x,y = self.stack.pop()
            self.floodfill(x,y)
            # self.display()
            # a = input()
        self.volume = len(self.seen) + len(self.positions)
        print("volumn is ",self.volume)
        # print(len(self.seen))

    

    def floodfill(self,x,y):
 
        if (x,y) in self.positions:
            return
        if (x,y) in self.seen:
            return
        # if (x not in range(self.length)) or (y not in range(self.breadth)):
        #     return 
        self.seen.add((x,y))
        
        for val in self.move.values():
            self.stack.append((x + val[0],y + val[1]))
    
    def createmap(self):
        self.map = [["." for j in range(self.length)] for _ in range(self.breadth)]

        for x,y in self.positions:
            self.map[y][x] = "#"



    
    def display(self):
        temp = [["." for j in range(self.length)] for _ in range(self.breadth)]

        

        for x,y in self.positions:
            temp[y][x] = "#"
        for x,y in self.seen:
            temp[y][x] = "*"
              
        for row in temp:
            print("".join(row))
        print()

            
    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

