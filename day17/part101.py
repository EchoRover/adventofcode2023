
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


def main(data):
    pathsolver = PathSolver(data.split())


class PathSolver:
    def __init__(self,data):
        self.data = data
        self.length,self.breadth = len(self.data[0]),len(self.data)
        self.lowest_heatloss = float('inf')
        # self.display()
        self.findpath(0,0)
    
    def findpath(self,x,y):
        self.stack = [(x,y,"s",1,[],0),(x,y,"e",1,[],0)]
        self.all = [(x,y,"s",1,[],0),(x,y,"e",1,[],0)]
        while self.stack != []:
            cc = self.lowest_heatloss
            x,y,prevdir,dist,path,heat = self.stack.pop()
            self.display(path)
            print(self.lowest_heatloss,heat)
            a = input()
            

            self.move(x,y,prevdir,dist,path,heat)
            if cc != self.lowest_heatloss:
                print(self.lowest_heatloss)
            # self.stack.sort(reverse = True,key = self.order)

        print(self.lowest_heatloss)
    
    def move(self,x,y,prevdir,distance,path,heat):
        heat += int(self.data[y][x])
        if (heat + self.dist((1,(x,y)))) > self.lowest_heatloss:
            return 
        if (x,y) == (self.length - 1,self.breadth - 1):
            self.lowest_heatloss = min(self.lowest_heatloss,heat)
            return
        if (x,y) in path:
            return
        path.append((x,y))
        paths = {"n":(x,y - 1),"s":(x,y + 1),"e":(x + 1,y),"w":(x - 1,y)}
        rev = {"n":"s","e":"w","w":"e","s":"n"}      
        del paths[(rev[prevdir])]

        if distance == 3:
            try:
                del paths[prevdir]
            except:
                print("path not found")
        final = []
        for key in paths:
            if paths[key][0] in range(self.length):
                if paths[key][1] in range(self.breadth):
                    final.append((key,paths[key]))
        final = sorted(final,key = self.dist2,reverse = True)


                
                
        # print(final)
        
        for newdir,xy in final:
          
            if newdir == prevdir:
                out = (xy[0],xy[1],newdir,distance + 1,path.copy(),heat)
             
            else:
                out = (xy[0],xy[1],newdir, 1,path.copy(),heat)
            if out not in self.all:
                self.stack.append(out) 
                self.all.append(out)

                
            



    def dist2(self,x):
        return int(self.data[x[1][1]][x[1][0]]) * 0.5 + abs(x[1][0] - self.length - 1) * 0.5 + abs(x[1][1] - self.breadth - 1) * 0.5


    
    def dist(self,x):
        return abs(x[1][0] - self.length - 1) + abs(x[1][1] - self.breadth - 1)
    
    def display(self,path):
        copy = [["." for i in range(self.length)] for j in range(self.breadth)]
        for x,y in path:
            copy[y][x] = "#"
        for row in copy:
            print("".join(row))
        print()

    def order(self,x):
        return abs(x[0] - self.length - 1) + abs(x[1] - self.breadth - 1)



with open("day17/data.txt") as f:
    inpdata = f.read()
    main(test)