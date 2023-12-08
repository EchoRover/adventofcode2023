from pprint import pprint 
import math
from functools import reduce
test = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
test2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

def parser(data):
    instructions,nodes = data.split("\n\n")
    instructions = [1 if i == "R" else 0  for i in instructions ]
    nodes = nodes.split("\n")
    nodes = [tuple(map(str.strip,node.split("="))) for node in nodes]
    nodes = {i[0]:(i[1][1:4],i[1][6:-1]) for i in nodes}
    print(instructions,nodes)
    return instructions,nodes



def do1(instructions,nodes,start):
    steps = -1
    nextrule = instructions[steps % len(instructions)]
    currentnode = start       
    while True:
        steps += 1 
        nextrule = instructions[steps % len(instructions)]
        currentnode = nodes[currentnode][nextrule]

        
        yield currentnode


def is_allfollowed(currentpositions,endlen):
    return sum([i.endswith("Z") for i in currentpositions]) == endlen
    

def main(data):
    
    instructions,nodes = parser(data)
    start = {i for i in nodes if i.endswith("A")}
      
    lcm = 1
    for s in start:
        gen = do1(instructions, nodes, s)
        step = 1
        while not next(gen).endswith("Z"):
            step += 1
        lcm = lcm * step // math.gcd(lcm, step)

    print(lcm)
    

def gcdarray(arr,idx):
    if len(arr) - 1 == idx:
        return arr[idx]
    a = arr[idx]
    b = gcdarray(arr,idx +1)
    return math.gcd(a,b)



        


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

#1.1673406230679783e+25

#2026633026159684687360