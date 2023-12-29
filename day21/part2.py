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


def main(data, steps):
    data = parser(data)
    step = Steps(data, steps)


class Steps:
    def __init__(self, data, steps):
        self.data = data
        self.steps = steps
        self.length = len(self.data[0])
        self.breadth = len(self.data)

        assert self.length == self.breadth

        self.getorigin()
        self.solve()


      
    
    def solve(self):
   
        points,offset = self.get_relation()
        x,y,z,_ = points


        c = x
        a = (z - 2 * y + c)/2
        b = y - c - a

        # c = alpha
        # a = (gamma - 2 * beta + c) / 2
        # b = beta - c - a

        def f(x):
            return a * x ** 2 + b * x + c


        print("ans = ",round(f(self.steps // (2 * self.length) - offset)))


    def move(self, mygoal):
        orig = self.steps % (2 * self.length)
        final = set()
        seen = {(self.x, self.y)} 
        q = deque([(self.x, self.y, orig + 2 * self.length * mygoal)])


        while q:
            x, y, dist = q.popleft()

            if dist % 2 == 0:
                final.add((x, y))

            if dist == 0:
                continue

            for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                if self.data[ny % self.breadth][nx % self.length] == "#" or (nx, ny) in seen:
                    continue

                seen.add((nx, ny))
                q.append((nx, ny, dist - 1))

               
       

        return len(final)


    def getorigin(self):
        for y in range(self.breadth):
            for x in range(self.length):
                if self.data[y][x] == 'S':
                    self.x, self.y = x, y
                    return
        raise "start x and y not fount"
    
    def get_relation(self):
        points = []
        results = []
        x = 0

        while True:   
          
            points.append(self.move(x))
            x += 1
           
          
            if len(points) >= 4:
                d1 = points[3] - points[2]
                d2 = points[2] - points[1]
                d3 = points[1] - points[0]
                sd1 = abs(d1) - abs(d2)
                sd2 = abs(d2) - abs(d3)
            
                if sd1 == sd2:
                    return points,x - 4
                else:
                    points.pop(0)
    # f(x) 
    # f(x + 2x)
    # f(x + 4x)
   



with open("data.txt") as file:
    input_data = file.read()
    main(input_data,26501365)



#inspiration :https://www.youtube.com/watch?v=C5wYxR6ZAPM&t=6009s&ab_channel=HyperNeutrino