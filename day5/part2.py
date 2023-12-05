import math
import cProfile
import pprint as p
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


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        # [{self.start},{self.end})  \t{list(range(self.start,self.end))}
        return f"[{self.start},{self.end})"

    def __bool__(self):
        return bool(self.start)

    def intersection(self, other):
        #-----------
        #       -------
        tm = Range(max(self.start,other.start),min(self.end,other.end))
        if tm.end > tm.start:
            return tm
        return None
    
    def subtract(self,other):
        ins = self.intersection(other)
        #----
        #    --
        if  ins == None:
            return [Range(self.start,self.end)]

        #----
        #----
        elif (self.start,self.end) == (ins.start,ins.end):
            return []
        #----
        #--
        elif self.start == ins.start:
            return [Range(ins.end,self.end)]
        # ---
        #   -
        
        elif self.end == ins.end:
            return [Range(self.start,ins.start)]
        
        # ----
        #  --

        else:
            return [Range(self.start,ins.start),Range(ins.end,self.end)]


    def add(self,plus):
        return Range(self.start + plus,self.end + plus)

        

# a = Range(1,5)
# b = a.add(2)
# print(a,b)
# b = Range(5,8)
# print(a,b)
# print(a.subtract(b))

class solver:
    def __init__(self, data):
        self.off = 0
        if self.off:
            return
        self.data = data
        self.seeds = []
        self.map = {}
        self.reverse_map = {}

        self.cutter()
        self.solve()

    def cutter(self):
        self.data = self.data.split("\n\n")

        for id, i in enumerate(self.data):
            head, values = i.split(":")
            if head == "seeds":
                values = values.split()
                values = list(map(int, values))
                self.seeds = [(values[i], values[i] + values[i + 1])
                              for i in range(0, len(values), 2)]
            else:
                values = values.split("\n")[1:]
                # dest_start , start , range , dest_Start - start,start + range
                # start <= num < start + range  and   deststart + num - start
                # i + [i[0] - i[1]] + [i[1] + i[2]]
                values = [i.split() for i in values]
                values = (list(map(int, lst)) for lst in values)
                values = tuple(
                    [{"start": i[1], "end": i[1] + i[2], "backlook": i[0] - i[1]}for i in values])

                self.map[id] = values

        self.seed = tuple(self.seeds)

        

    def info(self):
        p.pprint(self.map)
        p.pprint(self.seeds)
        print("total values:", sum([i[1] - i[0] for i in self.seeds]))

    def solve(self):
        self.low = math.inf

        for start,end in self.seeds:
            self.recursion(Range(start,end),0)
        print(self.low)
    

    def recursion(self,r ,layer):
        # print(r.start)
        if layer == len(self.map):
            self.low = min(self.low,r.start)
            return
        
        for part in self.map[layer + 1]:
            map_r = Range(part["start"],part["end"])
            ins = r.intersection(map_r)
            if ins is not None:
                modified_r = ins.add(part["backlook"])
                self.recursion(modified_r,layer + 1)
                others = r.subtract(map_r)
                if len(others) == 0:
                    return
                r = others[0]
                
                if len(others) == 2:
                    self.recursion(others[1],layer)
        
        self.recursion(r,layer + 1)


    


def problem5(data):
    solve = solver(data)

    # a.solveall()


with open("day5/data.txt") as f:
    dd = f.read()
    problem5(dd)













"""
Inspiration - https://youtu.be/b8ka6eZ4Vbk?si=VBiu8_NsUtARVPO7
"""