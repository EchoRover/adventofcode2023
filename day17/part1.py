
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


def parser(data):
    return data.split("\n")

def main(data):
    data = parser(data)
    path = Path(data)


class Path:
    def __init__(self,data):
        self.data = data
        self.length, self.breadth = len(self.data[0]),len(self.data)
        self.inversedir = {"n":"s","s":"n","e":"w","w":"e"}
        self.movedirs = {"n":(0,-1),"s":(0,1),"e":(1,0),"w":(-1,0)}
        self.heatloss = float('inf')

        self.startmove(0,0)
    def startmove(self,x,y):
        self.Stack = []
        self.Stack.append((x,y,'e',1,100))
        self.Stack.append((x,y,'s',1,100))
        while self.Stack != []:
            
        
            
            x,y,dirs,dist,heat = self.Stack.pop()
            self.move(x,y,dirs,dist,heat)
            self.display(x,y)
            print(x,y,dirs,dist,heat)
            a = input()
        print(self.heatloss)

        
    

    def move(self,x,y,direction,distance,heat):
        
        if (x,y) == (self.length - 1,self.breadth - 1):
            self.heatloss = min(self.heatloss,heat)
            return
        if heat > self.heatloss:
            return 
        dirs = ['n','s','e','w']
        
        dirs.remove(self.inversedir[direction])
        
        if distance == 3:
            dirs.remove(direction)
        newdirs = []
        for i in dirs:
            nx,ny = x + self.movedirs[i][0],y + self.movedirs[i][1]
            if( nx  in range(self.length)) and (ny in range(self.breadth)):
                newdirs.append((nx,ny,i))
        
        print(dirs,sorted(newdirs,key = self.power))

                

        dirs = sorted(newdirs,key = self.power)
        
       
        
        for i in dirs:
            if i[2] == direction:
                self.Stack.append((nx,ny,i[2],distance + 1,heat + int(self.data[y][x])))
            else:
                self.Stack.append((nx,ny,i[2],1,heat + int(self.data[y][x])))
    
    
    def display(self,x,y):
        for j in range(self.breadth):
            for i in range(self.length):
                if (i,j) == (x,y):
                    print("*",end = "")
                else:
                    print(self.data[j][i],end = "")
            print()
        print()
    def power(self,a):
        return abs(self.length - a[0]) + abs(self.breadth - a[1])
         



        


        



    


with open("day17/data.txt") as file:
    input_data = file.read()
    main(test)

