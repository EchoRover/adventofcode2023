imptest = """#..#..#..##..#.
...#..##.##.#..
###.#.########.
##.#...##..##..
#.####...##...#
.####.#.####.#.
##.##..######..
.####..#....#..
.##.##.##..##.#
..#.##...##...#
#.#.#.##.##.##.
#####.#.#..#.#.
...##...####...
#.#..##.#..#.##
.####.#.####.#.
.####.#.####.#.
#.#..##.#..#.##"""


test1 = """#.##..##.
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
#....#..#"""
"""
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


test2  = """#.##..##.
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


        self.tot = 0
        for i in self.patterns:
            self.tot += self.allspots(i)
        print(self.tot)


    def analyze(self,pattern):
        ps = pattern.split("\n")
        dir = None

        # self.display(pattern)

        #row
        a = self.dohorizontaltest(ps) 

        
    
        dir = "row"
        if not len(a[0]):
            #column
            ps = self.transpose(pattern).split("\n")
            a = self.dohorizontaltest(ps)
            dir = "col"
        
        # wehave,wasdir = a,dir

        # a = self.dohorizontaltest(ps,True)
        # dir = "row"
        # if a == wehave or not a:
        #     ps = self.transpose(pattern).split("\n")
        #     a = self.dohorizontaltest(ps,True)
        #     dir = "col"
        # if not a:
        #     a = wehave
        #     dir = wasdir
        #     print("p"* 10)
        
        # assert a == wehave, "we have a prolem"
        
        old = self.analyze1(pattern)
        a.append(old)
        # print(a)

        
        if a[1] == None:
            a = a[0][0]
        else:
            if len(a[0]) > 1:
                a[0].remove(a[1])
            a = a[0][0]
        # print(a)
      
            




    
        return a if dir == "col" else a * 100

    def regulartest(self,pattern):
        a = self.quick_check_reflection(pattern.split("\n"))        
        if a:
            return a * 100
        pattern = self.transpose(pattern)
    
        a = self.quick_check_reflection(pattern.split("\n"))

        return a

    def quick_check_reflection(self,p):

        options = len(p) 
        
        for i in range(1,options):
            before,after = p[:i],p[i:]
            before.reverse()
        
            minlen = min(len(before),len(after))
        
            if after[:minlen] == before[:minlen]:
                return i
        
        return False
    
    def doreflection(sefl,p):
        options = len(p)

        for i in range(1,options):
            before,after = p[:i],p[i:]
            before.reverse()
        
            minlen = min(len(before),len(after))
            chance = True
        
            for j in range(minlen):
                if before[j] != after[j]:
                    if not (is_1_similar(before[j],after[j]) and chance):
                        break
                    else:
                        chance = False
            else:
                return True


        
        return False
    



    def dohorizontaltest(self,p):
      
        p = [lst for lst in p.split("\n")]

        options = len(p)
        alli = [] 
      
        for i in range(1,options):
            before,after = p[:i],p[i:]
            before.reverse()
        
            minlen = min(len(before),len(after))
      


            chance = False

            for j in range(minlen):
                
                if before[j] != after[j]:
                    if self.is_1_similar(before[j],after[j]) and chance:
                        chance = False
                    else:
                        break
            else:
                if not(i in alli):
                    alli.append(i)        
        return alli
    
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


    def allspots(self,data):
        regular = self.regulartest(data)

      
        files = []
        for idx,i in enumerate(data):
            if i == ".":
                ch = "#"
            elif i == "#":
                ch = "."
            else:
                ch = "\n"
            
            new = data[:idx] + ch + data[idx + 1:]

            newana = self.dohorizontaltest(new)
                  
            if newana != []:
            
                newana = [i * 100 for i in newana]
            else:
                new = self.transpose(new)
                newana = self.dohorizontaltest(new)



         
        
            if newana != [] and newana not in files:
        
                files.extend(newana)
        files = list(set(files))
            
        print(regular,files)


        if regular in files and len(files) == 2:
            files.remove(regular)
            return files[0]
        
        return regular


                
     
        # print(files)
        # print(regular)

            
    



    
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
    main(imptest)


#17622 low 2nd 

#33711 high 4th
#35210 weird 5th
#38894 high 1st 

#46594 3rd