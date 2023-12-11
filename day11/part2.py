import math
test = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
test1 = """...#......
.......#..
..........
..........
......#...
.#........
.........#
..........
.......#..
....#....."""

def parser(data):
    data = [i for i in data.split("\n")]
    data = [list(lst) for lst in data]
    return data
def main(data):
    data = parser(data)
    cosmos = Cosmos(data,expan = 1000000)
    
class Cosmos:

    def __init__(self,data,expan = 2):
        self.data = data
        self.len = len(data[0])
        self.bre = len(data)

        self.expansion = expan
        self.spacejump = []
        self.rowjumps = []
        self.columnjumps = []


        
        self.getjumps()
        self.display()

        self.galaxycount()
        print("no of iterations",self.comb(self.gc,2))
        self.distances()
       
    

    def display(self):
        for row in self.data:
            print("".join(row))
        print()
    
    def advdisplay(self):
        for j in range(self.bre):
            for i in range(self.len):
                if (i,j) in self.spacejump:
                    char = "*"
                else:
                    char = self.data[j][i]
                print(char,end = "")
            print()

    def comb(self,n,r):
        a = math.factorial

        return a(n)/(a(r)*a(n- r))



    def getjumps(self):
        
        # rows
        for x,row in enumerate(self.data):
            if "#" not in row:
                self.rowjumps.append(x)
            
                self.spacejump.extend([(i,x) for i in range(self.len)])
        
    
        for i in range(self.len):
            for row in self.data:
                if row[i] == "#":
                    break
            else:
                self.columnjumps.append(i)
    
        for idx,i in enumerate(self.columnjumps):
            for y,row in enumerate(self.data):
                
                self.spacejump.append((i,y))
        

    def galaxycount(self):
        self.gc = 0
        self.g = []

        for y,row in enumerate(self.data):
            for x,tile in enumerate(row):
                if tile == "#":
                    self.gc += 1
                    self.g.append((x,y))

        self.advdisplay()

    def distances(self):

        self.all_dist = []
        
        total = self.gc
        for i in range(0,total - 1):
            for j in range(i + 1,total):
               
               
                p1 = self.g[i]
                p2 = self.g[j]
                self.all_dist.append(self.dist(p1,p2))
             
                
                # print(p1,p2,i + 1,j + 1,"dist",self.dist(p1,p2))
        print("answer",sum(self.all_dist))

    def dist(self,a,b):
        sx,lx = min(a[0] , b[0]),max(a[0] , b[0])
        sy,ly = min(a[1] , b[1]),max(a[1] , b[1])
        dx = dy = 0
        for i in range(sx,lx):
            if i in self.columnjumps:
                dx  += self.expansion
            else:
                dx += 1
        for i in range(sy,ly):
            if i in self.rowjumps:
                dy += self.expansion
            else:
                dy += 1
            
        return dx + dy   

with open("day11/data.txt") as file:
    input_data = file.read()
    main(input_data)



"""
0123

01 02 03 12 13 23 
so 1234

12,13,14,23,24,34
for i in range(1,4):
    p
for i in range(4):
    for j in range(4  - i):
        print(i,j)

"""
