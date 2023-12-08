
test = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
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
    
def followinstruction(currentpositions,steps,instructions,nodes):
    
    if currentpositions == "ZZZ":
        return steps    
    nextrule = instructions[steps % len(instructions)]
     
    return followinstruction(nodes[currentpositions][nextrule],steps + 1,instructions,nodes)

def follow2(instructions,nodes):
    steps = 0
    nextrule = instructions[steps % len(instructions)]
    currentpositions = nodes["AAA"][nextrule]

    while currentpositions != "ZZZ":
        steps += 1
        nextrule = instructions[steps % len(instructions)]
        
        currentpositions = nodes[currentpositions][nextrule]
    return steps + 1


def main(data):
    
    instructions,nodes = parser(data)
    steps = follow2(instructions,nodes)
    print(steps)


with open("data.txt") as file:
    input = file.read()
    main(input)

