
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
    data = [[int(lst[2][-2]),int('' + lst[2][2:-2],16)] for lst in data]

    return data



def main(data):
    data = parser(data)
    dig = Digger(data)


class Digger:
    def __init__(self,data):
        self.data = data
        self.move = {0:(1,0),2:(-1,0),3:(0,-1),1:(0,1)}
        
 

        self.positions = []


        self.createborder()

        self.findvolumn()

    

    def createborder(self):
        self.x = self.y = 0
        self.border = 0

        for direction,times in self.data:
            
            self.positions.append((self.x,self.y))
            self.x += self.move[direction][0] * times
            self.y += self.move[direction][1] * times
            self.border += times
        
        assert self.x == 0  and self.y == 0,"somthing is wrong"
    
         
        # print(self.border)
        
    
    def findvolumn(self):
        self.volume = self.border/2 + 1


        area = 0

        for point in range(len(self.positions) - 1):
            x1,y1,x2,y2 = self.positions[point][0],self.positions[point][1],self.positions[point + 1][0],self.positions[point + 1][1]
            area += (x1 * y2) - (x2 * y1)
    
        self.volume += (area/2)

        print("volumn", self.volume)
            


    

    
    



    

            
    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

