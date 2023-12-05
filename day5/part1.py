
test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4  """
class solver:
    def __init__(self,data):
        self.data = data
        self.seeds = []
        self.soil = []
        self.fertilizer = []
        self.water = []
        self.light = []
        self.humidity=[]
        self.location = []
        self.map = {}
    
    def cutter(self):
        self.data = self.data.split("\n\n")
        for i in self.data:
            head,values = i.split(":")
            if head == "seeds":
                values = values.split()
                self.seeds = values
            else:
                values = values.split("\n")[1:]
                values = [i.split() for i in values]
                self.map[head] = values
                
            # print(head,values,sep="__")
        # print(self.map)
    
    def solveall(self):
        locations = []
        for seed in self.seeds:
            location = self.solveseed(int(seed))
            locations.append(location)
            # print(location)
        print(min(locations))
    

    def solveseed(self,num):
        history = [num]
        for part in self.map:
            
            for sub in self.map[part]:
                check = self.check(num,sub)
                if check:
                    num = check
                    history.append(num)
                    break
        # print(history)
        return num




    def check(self,num,info):
        info = [int(i) for i in info]
        destination,start,range = info
        if self.isin(num,start,range):
            return (destination + num - start) 
        return False

    
    def isin(self,num,a,aa):
        if num >= a and num < (a + aa):
            return True
        return False


def cutter(data):
    data = data.split("\n\n")
    
    print(data)


def problem5(data):
    a = solver(data)
    a.cutter()
    a.solveall()



with open("data.txt") as f:
    dd = f.read()
    problem5(dd)

