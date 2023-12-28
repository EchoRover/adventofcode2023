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
    # data = [("?".join([lst[0]]* 5),",".join([lst[1]]* 5),) for lst in data]
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
        c = 1
        self.cache = {}
        for line in self.data:
            self.calls = 0
            

            
            
            total += self.allarrangments(line[0],line[1])
            # print(total,c,self.calls)
            # print(self.cache)
            c += 1
          
        print(total)
        print(self.cache)
    
    def allarrangments(self,line : str, numbers : list) -> int:
        num_index = numbers[0]
        numcount = 0
         
        
        for i in range(len(line)):
            tile = line[i]
            if tile == "?":
                pass

            
        print(line,numbers)
        return 0


    

    def display(self,*line):
        print(*line,sep = " ")
    
    def gen2(self,data,nums,string,index):
        
    
        if index == len(data):
            if string.count("#") == sum(nums):
               if tuple([len(i)  for i in string.split(".") if i != ""]) == nums:
                return 1
            return 0

        key = (string,index,nums)
        if key in self.cache:
            self.calls += 1
            return self.cache[key]

        result = 0
        if string[index] == "?":
            result += self.gen2(data,nums,string[:index] + "#" + string[index + 1:],index + 1)
            result += self.gen2(data,nums,string[:index] + "." + string[index + 1:],index + 1)
        else:
            result += self.gen2(data,nums,string,index + 1)
        
        self.cache[key] =result

        return result

        
    

    def combination(self,n,r):
        a = math.factorial
        return a(n)/(a(n - r) * a(r))
    def permutation(self,n,r):
        a = math.factorial
        return (a(n)/(a(n - r)))


with open("day12/data.txt") as file:
    input_data = file.read()
    main(test)

