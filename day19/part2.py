
test = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


def parser(data):
    data,qs = data.split("\n\n")
    qs = qs.split("\n")
    qall = []
    dd = {}
    start = None

    for i in data.split("\n"):
        center = i.find("{")
        if start == None:
            start = i[:center]
        
        dd[i[:center]] = i[center + 1: -1].split(",")
    


    
   
    for i in qs:
        qd = {}
        
        for term in i[1:-1].split(","):
            pointer,number = term.split("=")
            qd[pointer] = int(number)
        
        qall.append(qd)
    


    return dd,qall,start

def main(data):
    data,ques,start = parser(data)
 
    x = Workflow(data,ques,start)


class Workflow:
    def __init__(self,data,ques,start):
        self.data = data
        self.ques = ques
        self.start = start 
        # print(self.data)

        self.solveall()
    
    def solveall(self):
        self.tot = 0

        for i in self.ques:
            self.solveworkflow(i,self.start)
        
        print(self.tot)

    
    def solveworkflow(self,rules,start):
        self.mystart = 'in' 
     
        self.info = rules
        
        while self.mystart in self.data:
            self.dorule(self.data[self.mystart])
        
        if self.mystart in "XMAS":
            self.tot += sum(self.info.values())

            
    
    def dorule(self,rule):
       
        for i in rule:
            if ":" not in i:
                self.mystart = i
                return
            
            cond,out = i.split(":")
            splitter = ">" if ">" in i else "<"
            cond = cond.split(splitter)
            
            if splitter == ">":
                if self.info[cond[0]] > int(cond[1]):
                    self.mystart = out
                    return
            else:
                if self.info[cond[0]] < int(cond[1]):
                    self.mystart = out
                    return


            

    


with open("day19/data.txt") as file:
    input_data = file.read()
    main(input_data)

