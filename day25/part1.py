import networkx as nx
test = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""


def parser(data):
    data = [lst.split(":") for lst in data.split("\n")]
    data = {lst[0]:lst[1].split() for lst in data}
   
    return data

def main(data):
    data = parser(data)
    x = Connections(data)


class Connections:
    def __init__(self,data):
        self.data = data
        self.g = nx.Graph()
        self.creategraph()
        self.cutandsolve()
    
    def creategraph(self):
     
        for head,children in self.data.items():
            for child in children:
                self.g.add_edge(head,child)
                self.g.add_edge(child,head)

        
    def cutandsolve(self):
        self.g.remove_edges_from(nx.minimum_edge_cut(self.g))
        a,b = nx.connected_components(self.g)
        print(len(a) * len(b))



with open("day25/data.txt") as file:
    input_data = file.read()
    main(input_data)

