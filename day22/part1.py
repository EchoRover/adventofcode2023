
test = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

def parser(data):
    data = data.split("\n")
    data = [lst.split('~') for lst in data]
    data = [[tuple((map(int,(lst[0].split(','))))),tuple((map(int,(lst[1].split(',')))))] for lst in data]
    return data

def main(data):
    data = parser(data)
    solve = Solve(data)


class Solve:
    def __init__(self,data):
        self.data = data
 
        self.createallpoints()
    

    def createallpoints(self):
        n = []
        for st,en in self.data:
            if st == en:
                n.append(([(st,None)]))
            else:
                for i in range(3):
                    if st[i] != en[i]:
                        break
                print(i)
    
                points = [(st[:i] + (x,) + st[i + 1:],i) for x in range(st[i],en[i] + 1)]
                n.append((points))
                
        print(n)
    

    def fall(self,points):
        for bb in points:
            for x,y,z,d in bb:
                # d: 0:x 1:y 2:z





        
    


with open("day22/data.txt") as file:
    input_data = file.read()
    main(test)

