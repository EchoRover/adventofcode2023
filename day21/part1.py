from collections import deque
test = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def parser(data):
    return data.split("\n")

def main(data,steps):
    data = parser(data)
    step = Steps(data,steps)


class Steps:
    def __init__(self,data,steps):
        self.data = data
        self.steps = steps
        self.length = len(self.data[0])
        self.breadth = len(self.data)
        self.getorigin()

        self.move()
    
    def move(self):
        self.seen = set()
        final  = set()
        queue = deque([(self.x,self.y,0,0,0)])
        a = 0
        while queue:
            a += 1
       
            x,y,drx,dry,dist = queue.popleft()
            if self.data[y][x] == '#':
                continue
            if (x,y,drx,dry,dist) in self.seen:
                continue
            self.seen.add((x,y,drx,dry,dist))
    
            if dist == self.steps:
                final.add((x,y))
                continue

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                
                nx = x + dx
                ny = y + dy
                
                
                if nx in range(self.length) and (ny in range(self.breadth)) and self.data[ny][nx] != '#':
                    queue.append((nx,ny,dx,dy,dist + 1))
            
            # self.display(seen)
        
        print(len(final))
        # print(self.seen)
        print(len(self.seen),a)
    
    def display(self,data):
        print(data)
        tmp = [list(lst.replace('.',' ').replace('#','.')  ) for lst in self.data]
        
        for x,y in data:
            tmp[y][x] = '0'
        for i in tmp:
            print("".join(i))
        print()




    def getorigin(self):
        for y in range(self.breadth):
            for x in range(self.length):
                if self.data[y][x] == 'S':
                    self.x,self.y = x,y
                    return 



with open("data.txt") as file:
    input_data = file.read()
    main(input_data,64)

