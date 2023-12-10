
test1 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

test2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

test0 = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""
test = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

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
        self.other = "o"

        self.replaceS()
        self.createMaze()
        
        self.create_clear_maze()
        self.createmaps()

        self.display4()

        self.solve()

    def replaceS(self):
        """ replace start and get start """

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
        

    def display(self,new = False):
        if new:
            for y in self.newmaze:
                print(y)
            return


        for y in self.maze:
            print(y)
    def display4(self):
        self.updatecleanzero()
        for i in range(self.bre):
            print(self.maze[i],self.zeromaze[i],self.cleanmaze[i],self.zerocleanmaze[i],self.cornermap[i])
        print()

    def createMaze(self):
        """go through maze and get path """
        self.path = [(self.schar,(self.startX,self.startY))]
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
            self.path.append(((self.maze[y][x],(x,y))))
            # print(self.maze[y][x])
            entertile = connections2[tile][movement[step1][2]]
            if entertile == "A":
                exit = "B"
            else:
                exit = "A"
            step1 = connections2[tile].index(exit)
            

            x += movement[step1][0]
            y += movement[step1][1]
    

    def create_clear_maze(self):
        """this shows only path and everything else is ground"""
        self.cleanmaze = ["."*self.len for i in range(self.bre)]
        for tile in self.path:
            ypart = self.cleanmaze[tile[1][1]]
            new  = list(ypart)
            new[tile[1][0]] = tile[0]
            new = "".join(new)
            self.cleanmaze[tile[1][1]] = new

            

    def createmaps(self): 
        
        self.zeromaze = []
        for y in self.maze:
            xx = ""
            for tile in y:
                if tile != ".":
                    xx += self.other
                else:
                    xx += "."
            self.zeromaze.append(xx)
        
        self.corners = []
        for idy,y in enumerate(self.cleanmaze):
            for idx,x in enumerate(y):
                if x in ("F","L","J","7"):
                    self.corners.append((x,(idx,idy)))
        

        self.cornermap = ["."*self.len for i in range(self.bre)]
        for tile in self.corners:
            ypart = self.cornermap[tile[1][1]]
            new  = list(ypart)
            new[tile[1][0]] = tile[0]
            new = "".join(new)
            self.cornermap[tile[1][1]] = new
        
        self.updatecleanzero()
   
        

    def updatecleanzero(self):
        self.zerocleanmaze = []
        for y in self.cleanmaze:
            xx = ""
            for tile in y:
                if tile != ".":
                    xx += self.other
                else:
                    xx += "."
            self.zerocleanmaze.append(xx)

    def solve(self):
    
        #horizontal

        points = 0

        for y in self.cleanmaze:
            self.pos = "out"
            for idx,tile in enumerate(y):
                if tile == "|":
                    self.switch()
                elif tile in ("7","F"):
                    self.switch()



                    
                elif tile == "." and self.pos == "in":
                    points += 1
                    print("*",end ="")
                    continue

                print(tile,end = "")                   
                
            print()
        print(points)

    def switch(self):
        if self.pos == "in":
            self.pos = "out"
        else:
            self.pos = "in"

    def removeoutsides(self):
        #top #bottom
        for i in range(self.len):
            if self.cleanmaze[0][i] == ".":
                self.floodfill("O",i,0)
            elif self.cleanmaze[-1][i] == ".":
                self.floodfill("O",i,self.bre - 1)
          
        #left # right
        for i in range(self.bre):
            if self.cleanmaze[i][0] == ".":
                self.floodfill("O",0,i)
            elif self.cleanmaze[i][-1] == ".":
                self.floodfill("O",self.len - 1,i)


    def floodfill(self,tile,x,y):
        
        if self.cleanmaze[y][x] != ".":
            return
        ypart = list(self.cleanmaze[y])
        ypart[x] = tile
        self.cleanmaze[y] = "".join(ypart)
            
        for i in (((0,-1,2),(1,0,3),(0,1,0),(-1,0,1))):
            newx = x + i[0]
            newy = y + i[1]
            if newx >= 0 and newy >= 0 and newx < self.len and newy < self.bre:
                self.floodfill(tile,newx,newy)
                
                
               
        

        
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
    #main(test)
    # main(test0)
    # main(test1)
    # main(test2)
    main(input_data)

