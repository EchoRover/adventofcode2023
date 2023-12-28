
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
    def __init__(self,name,chids):
        if name == 'broadcaster':
            self.name = name
            self.type = 'broadcaster'
        elif '%' in name or '&' in name:
            self.name = name[1:]
            self.type = name[0]
        else:
            print("ero")
        self.state = 'low'
        self.allstate = {}
        self.children = chids
    
    def __repr__(self):
        return self.name
    
    def get(self,inp,mod = None):
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
    def __init__(self,data):
        self.data = data
        self.mods = {}
        for mod,chids in self.data.items():
            if mod == 'broadcaster':
                self.mods[mod] = Module(mod,chids)
            elif '%' in mod or '&' in mod:
                self.mods[mod[1:]] = Module(mod,chids)               
            else:
                print(mod)
            
        low = high = 0

        for i in range(1):
            nl,nh = self.pressbutton()
            low += nl
            high += nh

       
        print(low,high)
        
        print("ans = ",(low +0) * high)

    
        


    def pressbutton(self):
        self.highp = self.lowp = 0

        q = [('broadcaster','low')]

        while q:
            
            module,pulse = q.pop(0)
            if module not in self.mods.keys():
                # print(module)
                continue

            if pulse == 'low':
                self.lowp += 1
            else:
                self.highp += 1
            module = self.mods[module]
            output = module.get(pulse,module.name)
            # print(output,module,pulse,module.type)

            if output == None:
                continue

            for child in module.children:
            
            
    
                q.append((child,output))
            print(q,module,output)
            
            
        return (self.lowp,self.highp)

        



    


with open("day20/data.txt") as file:
    input_data = file.read()
    main(test2)

