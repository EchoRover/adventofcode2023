from collections import deque
import heapq
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
    return data.split("\n")

def main(data):
    data = parser(data)
    path = Path(data)


class Path:
    def __init__(self,data):
        self.data = data
        self.length = len(self.data)
        self.breadth = len(self.data[0])
        self.get_s()
        self.solve()
    
    def get_s(self):
        self.y = 0
        for i in range(self.length):
            if self.data[self.y][i] == '.':
                self.x = i
                return 
    
    def solve(self):
        dist = -float('inf')
        queue = deque([(0,self.x,self.y)])
        # heapq.heapify(queue)
        visited = []
    



        while queue:
         
            # queue = sorted(queue)
            queue = sorted(queue)
            queue = deque(queue)
            
            
            # mydist,x,y = heapq.heappop(queue)
            mydist,x,y = queue.pop()


            if self.data[y][x] == '#':
                continue

            if (x,y) in visited:
                continue
            visited.append((x,y))

            if y == (self.breadth - 1):
                dist = max(dist,mydist)
                
                
            

            # if self.data[y][x] in '<>^v':
            #     dit = {"<":(-1,0),">":(1,0),"^":(0,-1),"v":(0,1)}
            #     # print(self.data[y][x],dit[self.data[y][x]])

            #     nx = x +  dit[self.data[y][x]][0]
            #     ny = y +  dit[self.data[y][x]][1]

            #     queue.append((nx,ny,path.copy(),mydist + 1))

            #     continue



            for dx,dy in [(0,-1),(0,1),(1,0),(-1,0)]:
    
                nx = dx + x
                ny = dy + y

                if 0 <= nx < self.length and 0 <= ny < self.breadth:
                    if (nx,ny) not in visited:
                        # heapq.heappush(queue, (mydist + 1,nx,ny))
                        queue.append((mydist + 1,nx,ny))

                    

                    
        print(dist)
    
    def order(self,x):
        return x[-1]
    
    def display(self,data):
        tmp = [list(lst) for lst in self.data]
        for x,y in data:
            tmp[y][x] = '0'
        
        for i in tmp:
            print("".join(i))
        print()
            


    


with open("day24/data.txt") as file:
    input_data = file.read()
    main(test)

