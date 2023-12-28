import math
test = r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
test2 = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

def parser(data):
    data = data.split("\n")
    data = [lst.split(" -> ") for lst in data]
    data = {a[0]:tuple(map(str.strip,a[1].split(","))) for a in data}

 
    return data

def main(data):
    data = parser(data)
    pp = Solve(data)

class Module:
    def __init__(self,name,children,data):
        if name == 'broadcaster':
            self.name = name
            self.type = 'broadcaster'
        elif '%' in name or '&' in name:
            self.name = name[1:]
            self.type = name[0]
        else:
            print("error not possible to get unique module")
        
        self.state = 'low'
        self.allstate = {}
    
        self.children = children
        if self.type == '&':
            self.setupconj(data)
    

    
    def __repr__(self):
        return self.name
    
    def setupconj(self,data):
        for key,vals in data.items():
            if self.name in vals:
                self.allstate[key[1:]] = 'low'

 

    
    def get(self,inp,mod = None):
        # print(self.name,inp,self.allstate,"get func")
        if self.type == 'broadcaster':
            return inp
        if self.type == '%':
            if inp == 'high':
                return None
            else:
                self.state = 'low' if self.state == 'high' else 'high'

                return self.state
        if self.type == '&':
            self.allstate[mod] = inp
        
            if all(val == 'high' for val in self.allstate.values()):
                return 'low'
            else:
                return 'high'







        


class Solve:
    def __init__(self,data,times = 1000):
        self.data = data

        self.times = times
        self.setup()
        self.findconnections()
        mylcm = []

        for i in self.allcon:
            mylcm.append(self.test(i))
        print(mylcm)

        print(f"ans  = {math.lcm(*mylcm)}")
    

    def setup(self):
        self.mods = {}
        for mod,chids in self.data.items():
            if mod == 'broadcaster':
                self.mods[mod] = Module(mod,chids,self.data)
            elif '%' in mod or '&' in mod:
                self.mods[mod[1:]] = Module(mod,chids,self.data)               
            else:
                print(mod)





    
    def findconnections(self):
        head = [key for key in self.data if 'rx' in self.data[key] ][0][1:]
      
        allcon = []
        for key,vals in self.data.items():
            if head in vals:
                allcon.append(key[1:])
        # self.allcon = {key:None for key in allcon}
        self.allcon = allcon

    
    def test(self,module):
        self.setup()
    

        c = 1

        while self.pressbutton(module) == None:
            c += 1

        return c

     




    
        


    def pressbutton(self,mymod):
        self.highp = 0
        self.lowp = 0

        q = [('broadcaster','low','button')]

        while q:
            
            
            module,pulse,head = q.pop(0)

           
            if pulse == 'low':
                self.lowp += 1
            elif pulse == 'high':
                self.highp += 1

            if module not in self.mods.keys():
                continue

            

            module = self.mods[module]
            output = module.get(pulse,head)
            # print(output,module,pulse,module.type)

            if output == None:
                continue
            if module.name == mymod and output == 'high':
                return "yea"
      

     

            for child in module.children:
                # print(f"{module} -{output}-> {child}")
             
            
    
                q.append((child,output,module.name))
            # print(q,module,output)
            
        # print(f"low: {self.lowp}, high: {self.highp}\n")
        
       

        



    


with open("data.txt") as file:
    print("assuming that all moduls conneted to & func is % or &")
    print("assuming that rx connected to one module and that is conneted to 4 & module that work in cycles")
    print("rx <low- &x <-allhigh-  (a,b,c,d) all low  \n")

    input_data = file.read()
    main(input_data)

#seven is too low