test = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


class Reflections:
    def __init__(self, data):
        self.data = data
        self.dirs = {"n": (0, -1), "s": (0, 1), "e": (1, 0), "w": (-1, 0)}
        self.newdir = {
            '.': {'n': ['n'], 's': ['s'], 'e': ['e'], 'w': ['w']},
            '-': {'n': ["e","w"], 's': ['e',"w"], 'e': ['e'], 'w': ['w']},
            '|': {'e': ['n', 's'], 'w': ['n', 's'], 'n': ['n'], 's': ['s']},
            '/': {'n': ['e'], 's': ['w'], 'e': ['n'], 'w': ['s']},
            '\\': {'n': ['w'], 's': ['e'], 'e': ['s'], 'w': ['n']},
        }
        
        self.length, self.breadth = len(self.data[0]), len(self.data)

        a = []
        for i in range(self.length):
            a.append(self.doall(i,0,"s"))
            a.append(self.doall(i,self.breadth - 1,"n"))
        print("done 1")
        for i in range(self.breadth):
            a.append(self.doall(0,i,"e"))
            a.append(self.doall(self.length - 1,i,"w"))
        print("done 2")
        print(max(a))


        

    def doall(self, x, y, dire):

        self.stack = []
        self.unique = set()
        self.visited = []
        self.stack.append((x, y, dire))

        while len(self.stack) != 0:
            self.move(self.stack.pop())
            
            # print(len(self.stack))

        # print(len(self.unique))
        return len(self.unique)

    def move(self, parms):
        if parms in self.visited:
            return
        self.visited.append(parms)
        x, y, dirm = parms
        self.unique.add((x, y))
        tile = self.data[y][x]
        dirm = self.newdir[tile][dirm]
        # print(dirm)
        for i in dirm:
            
            x += self.dirs[i][0]
            y += self.dirs[i][1]
            
            if x in range(self.length) and y in range(self.breadth):
                self.stack.append((x, y, i))


with open("day16/data.txt") as f:
    data = f.read()
    # data = test
    data = data.split()
    reflect = Reflections(data)
