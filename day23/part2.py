from collections import deque

from time import sleep
test = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


def parser(data):
    return [list(lst.replace('.',' ')) for lst in data.split("\n")]

def main(data):
    data = parser(data)
   

    path = Path(data)


class Path:
    def __init__(self,data):
        self.data = data
        self.length = len(self.data)
        self.breadth = len(self.data[0])
        self.get_s()
        graph = self.getgraph()
        self.solve(graph)
       

    
    
    def get_s(self):
        self.ss = (self.data[0].index(' '),0)
        self.ed = (self.data[self.breadth - 1].index(' '),self.breadth - 1)


    def getgraph(self):
        
        points = []
        
        for y in range(self.breadth):
            for x in range(self.length):
                if self.data[y][x] == '#':
                    continue
                s = 0

                for dx,dy in ((0,-1),(0,1),(1,0),(-1,0)):
                    nx = x + dx
                    ny = y + dy
                
                    if (nx in range(self.length)) and (ny in range(self.breadth)) and (self.data[ny][nx] != '#'):
                        s += 1  
          
                    
                if s > 2 or y == 0 or y == (self.breadth - 1):
                    points.append((x,y))

      
        # self.d(points)
        # print(points)

        graph = {key : {} for key in points}


        for xx,yy in points:

            stack = [(0,xx,yy)]
            seen = {(xx,yy)}
            while stack:
                n,x,y = stack.pop()
                if n != 0 and (x,y) in points:
                    graph[(xx,yy)][(x,y)] = n
                    continue
                for dx,dy in ((0,-1),(0,1),(1,0),(-1,0)):
                    nx = x + dx
                    ny = y + dy
                
                    if (nx in range(self.length)) and (ny in range(self.breadth)) and (self.data[ny][nx] != '#') and ((nx,ny) not in seen):
                        stack.append((n + 1,nx,ny))
                        seen.add((nx,ny))


        return graph
    
    def solve(self,graph):

        seen = set()

        def dfs(pt):
            if pt == self.ed:
                return 0
            m = -float("inf")
            seen.add(pt)

            for nx in graph[pt]:
                if nx not in seen:
                    m = max(m,dfs(nx) + graph[pt][nx])
            seen.remove(pt)

            return m
        ans = dfs(self.ss)
        print(ans)


    
    def d(self,points):
        temp = [lst.copy() for lst in self.data]
        for x,y in points:
            temp[y][x] = "*"
        temp = "\n".join(["".join(lst).replace("#",".") for lst in temp])
        print(temp,"\n")

       
      
        
        


        







    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)


#inspiration from https://youtu.be/NTLYL7Mg2jU?si=uUfvCLWA-PtcMySV