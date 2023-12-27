
test = r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""


def parser(data):
    data = data.split("\n")
    data = [lst.split(" -> ") for lst in data]
    data = {a[0]:tuple(map(str.strip,a[1].split(","))) for a in data}

    print(data)
    return data

def main(data):
    data = parser(data)
    pp = PulseProp(data)

class Module:
    def __init__(self,name,output):
        self.name = name
        self.output = output
        self.type = None
        self.most_recent = None
        self.settype()
    
    def settype(self):
        if 'broadcaster' == self.name:
            self.type = "broadcaster"
            return
        if self.name.startswith("%"):
            self.type = "flip"
            self.name = self.name[1:]
            return
        if self.name.startswith("&"):
            self.type = 'add'
            self.name = self.name[1:]
    
    def do(self,*args):
        match self.type:
            case 'flip':
                return self.flip(args)
            case 'add':
                return self.add(args)
    
    def broadcaster(self):
        return tuple(zip(self.output,(0,) * len(self.output)))
    
    def flip(self,pulse):
        pulse = pulse[0]
        if self.most_recent:
            return (self.output,pulse)
        self.most_recent = 0 if self.most_recent else 1
        return (self.output,self.most_recent)
        
        pulse = pulse[0]
        print(pulse,self.output)
        pulse = 1 if pulse == 0 else 0
        return (self.output,pulse)
    
    def add(self,pulse):
        self.most_recent = pulse[0]
        if self.most_recent:
            return (self.output,0)
        return (self.output,1)


        ...


class PulseProp:
    def __init__(self,data):
        self.data = data
        self.createmod()
    

        self.pushbutton()
        
    
    def pushbutton(self):
        broad = self.mods['broadcaster']
        stack = list(broad.broadcaster())
        
        while stack:
            mod,val = stack.pop()
            a = self.mods[mod].do(val)
            stack.append(a)
        
        
    
    def createmod(self):
        self.mods = {}
        for i in self.data:
            tmp = Module(i,self.data[i])
            self.mods[tmp.name] = tmp

    


with open("day20/data.txt") as file:
    input_data = file.read()
    main(test)

