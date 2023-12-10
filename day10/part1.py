
test1 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""



test = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

# F - 7
# |   |
# L _ J

# f 1
# 1
#  N E S w

connections = {"F":[0,1,1,0],"7":[0,0,1,1],"J":[1,0,0,1],"L":[1,1,0,0],"|":[1,0,1,0],"-":[0,1,0,1],".":[0,0,0,0]}
connections2 ={"F":[0,"A","B",0],"7":[0,0,"A","B"],"J":["A",0,0,"B"],"L":["A","B",0,0],"|":["A",0,"B",0],"-":[0,"A",0,"B"]}
 


class Maze:

    def __init__(self,maze):
        self.maze = maze
        self.len = len(maze[0])
        self.bre = len(maze)

        self.replaceS()
        

        self.createMaze()
        self.calc()

    def replaceS(self):

        for y in range(self.bre):
            if self.maze[y].find("S") != -1:
                self.startX = self.maze[y].find("S")
                self.startY = y
                break
        S_sides = []
        for pos in ((0,-1,2),(1,0,3),(0,1,0),(-1,0,1)):
                newx = self.startX + pos[0]
                newy = self.startY + pos[1]
                if newx >= 0 and newy >= 0 and newx < self.len and newy < self.bre:
                    
                    # print(self.maze[newy][newx])
                    S_sides.append(connections[self.maze[newy][newx]][pos[2]])
                else:
                    S_sides.append(0)
                # print(newx,newy)
                # print(newx,newy)
    

        for key in connections:
            if connections[key] == S_sides:
                self.schar = key 
                
                break
        
        self.maze[self.startY] = self.maze[self.startY].replace("S",self.schar)
        

    def display(self):
        for y in self.maze:
            print(y)

    def createMaze(self):
        self.path = [self.schar]
        currentdir = "A"
        x = self.startX
        y = self.startY

        movement = ((0,-1,2),(1,0,3),(0,1,0),(-1,0,1))
        step1 = connections2[self.schar].index(currentdir)
        

        x += movement[step1][0]
        y += movement[step1][1]
        # print(x,y,self.startX,self.startY)

        while (x != self.startX) or (y != self.startY):
           
            tile = self.maze[y][x]
            self.path.append(self.maze[y][x])
            # print(self.maze[y][x])
            entertile = connections2[tile][movement[step1][2]]
            if entertile == "A":
                exit = "B"
            else:
                exit = "A"
            step1 = connections2[tile].index(exit)
            

            x += movement[step1][0]
            y += movement[step1][1]
            

            
        
    def calc(self):
        print(len(self.path)//2)
            
        


                    
        
        

        # print(self.startX,self.startY)


def parser(data):
    data  =data.split("\n")
    return data


def main(data):
    data = parser(data)
    
    
    maze = Maze(data)


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

