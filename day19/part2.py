
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


    for i in data.split("\n"):
        center = i.find("{")
     
        
        dd[i[:center]] = i[center + 1: -1].split(",")

    return dd

def main(data):
    data = parser(data)
 
    x = Workflow(data)


class Workflow:
    def __init__(self,data,minr = 1,maxr = 4000):
        self.data = data
        self.min_r = minr
        self.max_r = maxr
       
        self.solveall()

        
    
    def solveall(self):
        qs = {key:(self.min_r,self.max_r) for key in "samx"}
        

        for key,val in qs.items():
            qs[key] = self.solveworkflow(key,val)
            
        print(qs)

        lengths = [val[1] - val[0] for val in qs.values()]
        ans = lengths[0] * lengths[1] * lengths[2] * lengths[3]
        print(ans)
        
        
        

    
    def solveworkflow(self,key,val):
        self.tot = 1
        
        self.mystart = 'in'
        self.myrange = val
        self.mykey = key
          
        
        while self.mystart in self.data:
            # print(self.myrange,self.mystart)
            self.dorule(self.data[self.mystart])
        
        return self.myrange
        print(self.myrange)

            
    
    def dorule(self,rule):
     
    
           
        for i in rule:
           
            if ":" not in i:
                self.mystart = i
                return
            
            cond,out = i.split(":")
            splitter = ">" if ">" in i else "<"
            thiskey,number = cond.split(splitter)
            number = int(number)

            if thiskey != self.mykey:
                continue
            st1,en1 = self.myrange
          
            if splitter == ">":
               st2,en2 = (number + 1,self.max_r)
            else:
                st2,en2 = (self.min_r,number - 1)
            
          
            if st2 <= st1 and en1 <= en2:
                #if my range is inside
                print("inside")
                self.mystart = out 
                return
            elif st1 > en2 or st2 > en1:
                # there is no intersection
                continue
            else:
                print(st2,en2)
                print(rule)
                match splitter:
                    case '>':
                        # [ x to 4000]
                        print((st2,en1))
                        self.myrange = (st2,en1)
                    case '<':
                        print((st1,en2),"fdf")
                        # [1 to fdfd]
                        self.myrange = (st1,en2)
                    
                    
                self.mystart = out 
               
           
            



            

    


with open("day19/data.txt") as file:
    input_data = file.read()
    main(test)

