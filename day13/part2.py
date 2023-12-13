
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


test  = """#.##..##.
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

.#.##.#.#
.##..##..
.#.##.#..
#......##
#......##
.#.##.#..
.##..##.#

#..#....#
###..##..
.##.#####
.##.#####
###..##..
#..#....#
#..##...#"""

def parser(data):
    return data.split("\n\n")

def main(data):
    data = parser(data)
    refl = Reflection(data)


class Reflection:

    def __init__(self,data):
        self.patterns = data
        self.count = 0
        self.doall()
    

    def doall(self):
        for a in self.patterns:
            result = self.analyze(a)
            print(result)
            self.count += result
            
            
        print(self.count)

    def analyze(self,pattern):
        ps = pattern.split("\n")
        dir = None

        self.display(pattern)

        #row
        a = self.dohorizontaltest(ps) 
        dir = "row"
        if not a:
            #column
            ps = self.transpose(pattern).split("\n")
            a = self.dohorizontaltest(ps)
            dir = "col"
        
        wehave,wasdir = a,dir

        a = self.dohorizontaltest(ps,True)
        dir = "row"
        if a == wehave or not a:
            ps = self.transpose(pattern).split("\n")
            a = self.dohorizontaltest(ps,True)
            dir = "col"
        if not a:
            a = wehave
            dir = wasdir
            print("p"* 10)
        
        # assert a == wehave, "we have a prolem"
            




    
        return a if dir == "col" else a * 100

    def smugefix(self,pattern):
        return pattern



    def dohorizontaltest(self,p,chance = False):

        options = len(p) 
        
        for i in range(1,options):
            before,after = p[:i],p[i:]
            before.reverse()
        
            minlen = min(len(before),len(after))
            
            # print(before,after)
            # print(minlen)

            for j in range(minlen):
                
                if before[j] != after[j]:
                    if self.is_1_similar(before[j],after[j]) and chance:
                        chance = False
                    else:
                        break
            else:
                return i
 

        
        return False
    
    def transpose(self,p):
        p = [list(lst) for   lst in p.split("\n")]
        pp = [[(j,i) for j in range(len(p))] for i in range(len(p[0]))]

        for j in range(len(p)):
            for i in range(len(p[0])):
            
                pp[i][j] = p[j][i]
      

        return "\n".join(["".join(lst) for lst in pp])
    

    def is_1_similar(self,line1,line2,error = 0):
        # print(line1,line2)
    
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                error += 1
            if error > 1:
                return False
        
        return True
    



    
    def display(self,patt):
        for i in patt.split("\n"):
            print(i)
        print()

    def tests(self):
        a = "123\n456"

        assert a == self.transpose(self.transpose(a))
        assert "14\n25\n36" == self.transpose(a)



with open("day13/data.txt") as file:
    input_data = file.read()
    main(test)


#17622 low

#38894 high