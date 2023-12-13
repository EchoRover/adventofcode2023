
test = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

##.####.######.##
.#.#..#.#....#.#.
...#..#...##...#.
###....########..
#..#..#..####..#.
.#.#..#.#.##.#.#.
...####...##...##
..##..##......##.
##.#..#.######.#.
..#....#....#.#..
..#....#......#..
#...##...####...#
#.######.####.###
..##..##......##.
#........####...."""


def parser(data):
    return data.split("\n\n")

def main(data):
    data = parser(data)
    refl = Reflection(data)


class Reflection:

    def __init__(self,data):
        self.patterns = data
        self.count = 0

        # a = "123\n456"
        # print(self.transpose(self.transpose(a)))

      
    
        # print(self.transpose(self.transpose(a)))

        self.doall()
    

    def doall(self):
        for a in self.patterns:
            self.count += self.analyze(a)
            
        print(self.count)

    def analyze(self,pattern):


        a = self.dohorizontaltest(pattern.split("\n"))
        if a:
            return a * 100
        pattern = self.transpose(pattern)
    
        a = self.dohorizontaltest(pattern.split("\n"))
    
        return a



    def dohorizontaltest(self,p):

        options = len(p) 
        
        for i in range(1,options):
            before,after = p[:i],p[i:]
            before.reverse()
        
            minlen = min(len(before),len(after))
        
            if after[:minlen] == before[:minlen]:
                return i
 

        
        return False
    
    def transpose(self,p):
        p = [list(lst) for   lst in p.split("\n")]
        pp = [[(j,i) for j in range(len(p))] for i in range(len(p[0]))]

        for j in range(len(p)):
            for i in range(len(p[0])):
            
                pp[i][j] = p[j][i]
      

        return "\n".join(["".join(lst) for lst in pp])
    



    
    def display(self,patt):
        for i in patt.split("\n"):
            print(i)
        print()



with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

