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
    cosmos = Cosmos(data)
    
class Cosmos:

    def __init__(self,data):
        self.data = data
        self.len = len(data[0])
        self.bre = len(data)

        
        self.expand()
        self.display()

        self.galaxycount()
        print("no of iterations",self.comb(self.gc,2))
        self.distances()
       
    

    def display(self):
        for row in self.data:
            print("".join(row))
        print()
    def comb(self,n,r):
        a = math.factorial

        return a(n)/(a(r)*a(n- r))



    def expand(self):
        # rows 
        insertlist = []
        for x,row in enumerate(self.data):
            if "#" not in row:
                insertlist.append(x)

        for idx,i in enumerate(insertlist):
            self.data.insert(i + idx,["."] * self.len)
        
        #col
        insertlist.clear()
    
       

        for i in range(self.len):
            for row in self.data:
                if row[i] == "#":
                    break
            else:
                insertlist.append(i)
            
        #col
        for idx,i in enumerate(insertlist):
            for row in self.data:
                row.insert(i + idx ,".")

    def galaxycount(self):
        self.gc = 0
        self.g = []

        for y,row in enumerate(self.data):
            for x,tile in enumerate(row):
                if tile == "#":
                    self.gc += 1
                    self.g.append((x,y))

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
        # a =  math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        a = abs(a[0] - b[0]) +abs(a[1] - b[1])
        return round(a)

            


        
        


with open("data.txt") as file:
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
