import sympy

test = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def parser(data):
   data = [lst.split("@") for lst in data.split("\n")]
   data = [(list(map(int,lst[0].split(","))),list(map(int,lst[1].split(",")))) for lst in data]



   return data

def main(data):
    data = parser(data)
    x = HaleSim(data)


class HaleSim:
    def __init__(self,data):
        self.data = data
   
 

        self.test()
    
    def test(self):
        xr,yr,zr,vxr,vyr,vzr = sympy.symbols("xr,yr,zr,vxr,vyr,vzr")
        equations = []

        for a,b in self.data:
            sx,sy,sz = a
            vx,vy,vz = b
            equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
            equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        
        answers = sympy.solve(equations)[0]
        # print(answers)
       
        print(answers[xr] + answers[yr] + answers[zr])

            


        
    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)




#inspiration from 
#https://youtu.be/guOyA7Ijqgk?si=SFxM6iyg8utvOgGQ