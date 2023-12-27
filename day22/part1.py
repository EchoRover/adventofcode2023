
test = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


class Brick:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.create_points()
    

    def create_points(self):
        self.points = set((self.start,self.end))
        print(self.start,self.end)
    
        for i in range(self.start[0],self.end[0] +0):
            self.points.add((i,self.start[1],self.start[2]))
        for i in range(self.start[1],self.end[1] + 0):
            self.points.add((self.start[0],self.start[i],self.start[2]))
        for i in range(self.start[2],self.end[2] + 0):
            self.points.add((self.start[0],self.start[1],self.start[1]))
    
    def subtract(self,d):
        x,y,z = d
        for i in range(a):
            f

    


def parser(data):
    data = data.split("\n")
    data = [lst.split('~') for lst in data]
    data = [[tuple((map(int,(lst[0].split(','))))),tuple((map(int,(lst[1].split(',')))))] for lst in data]
    return data

def main(data):
    data = parser(data)
    solve = Solve(data)


class Solve:
    def __init__(self,data):
        self.data = data
        self.points = []
        self.createpoints()
        print(self.points)
        for i in self.points:
            print(i.points)
    
    def createpoints(self):
        for a in self.data:
           
            x,y,z  = a[0]
            x2,y2,z3 = a[1]
            self.points.append(Brick(a[0],a[1]))

        
    


with open("day22/data.txt") as file:
    input_data = file.read()
    main(test)

