import math
from itertools import permutations
test = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def parser(data):
    data = [lst.split() for lst in data.split("\n")]
    data = [[lst[0],tuple(map(int,lst[1].split(",")))] for lst in data]
    return data

def main(data):
    data = parser(data)
    spings = Springs(data)

    
class Springs:
    def __init__(self,data):
        self.data = data

        self.solve()

    def solve(self):
        total = 0
        for line in self.data:
            total += ( self.arrangeline(line))
          
        print(total)
    

    def display(self,*line):
        print(*line,sep = " ")
        
    def arrangeline(self,line):
        data,data2 = line
        self.var = []
        self.createallcombinations(data,0,sum(data2))
        self.correct = []
        for i in self.var:
            xx = i.split(".")
            xx = [i.count("#")  for i in xx if i != ""]
            if tuple(xx) == tuple(data2):
                self.correct.append(i)


        # print(len(self.correct))
  
        # print(self.permutation(qcount,2))
        return len(self.correct)
    
    def createallcombinations(self,string,index,tot):
        
        if index == len(string):
            if string.count("#") == tot:
                self.var.append(string)
        elif string[index] == "?":
            self.createallcombinations(string[:index] + "#" + string[index + 1:],index + 1,tot)
            self.createallcombinations(string[:index] + "." + string[index + 1:],index + 1,tot)
        else:
            self.createallcombinations(string,index + 1,tot)


        
       
      
        # print(data)

    def combination(self,n,r):
        a = math.factorial
        return a(n)/(a(n - r) * a(r))
    def permutation(self,n,r):
        a = math.factorial
        return (a(n)/(a(n - r)))


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

