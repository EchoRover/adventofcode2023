import numpy as np
test = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""






class Heatsolver:
    def __init__(self,data):
        self.data = data
        self.length = len(self.data[0])
        self.breadth = len(self.data)

        self.solve()
    
    def solve(self):
        # x,y drx,dry dist ,steps,heat
        self.queue = [(0,0,0,-1,0,1)]
        self.seen = set()

        while self.queue:
            self.queue.sort()

            heat,x,y,drx,dry,dist = self.queue.pop(0)
            # self.display(heat)

            # print(x,y,drx,dry,dist,heat)

            if (x == (self.length - 1)) and (y == (self.breadth - 1)):
                print("Heat is :")
                print(heat)
                return
                

            if (x,y,drx,dry,dist) in self.seen:
                continue
            self.seen.add((x,y,drx,dry,dist))

   
           

            for dx,dy in [(0,-1),(1,0),(0,1),(-1,0)]:    
                if (dx == -drx) and (dy == -dry):
                    continue
                
                nx = x + dx
                ny = y + dy
                if nx in range(self.length) and ny in range(self.breadth):
                    cost = int(self.data[ny][nx])
                    if (dx == drx) and (dy == dry):
                        if dist < 3:
                            self.queue.append((heat + cost,nx,ny,dx,dy,dist + 1))
                        continue
                    
                    self.queue.append((heat + cost,nx,ny,dx,dy,1))
            
        print("Done! -- something went wrong :(")
    
    def display(self,h):
        temp = [["." for j in range(self.length)] for i in range(self.breadth)]
        for i in self.seen:
            temp[i[1]][i[0]] = "#"
        for i in temp:
            print("".join(i))
        print(h)
        a = input()
    
    def sorter(self,x):
        return x[-1]  




def parser(data):
    return data.split("\n")

with open("day17/data.txt") as f:
    inpdata = f.read()
    a = parser(inpdata)
    ss = Heatsolver(a)