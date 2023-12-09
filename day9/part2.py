
test = """10  13  16  21  30  45"""


def parser(data):
    data = data.split("\n")
    data = [list(map(int,lst.split()[::-1])) for lst in data]
    # print(data)
    return data

def main(data):
    data = parser(data)
    total = 0
    final = []

    for i in data:    
        val = extrapolate(i).number
        total += val
     
        
    print(total)
    
    

class extrapolate:
    def __init__(self,data,idx = None,test = None):
        self.data = [data]
        self.number = 0

        self.zeros_in()
        self.backtrack()
        

        if test:
            self.data.reverse()
            self.display()
            self.test()

        
    
    def display(self):
        for i in self.data:
            print("    "* self.data.index(i),i,len(i))
        print()


    
    def test(self):
        for i in range(len(self.data) - 1):
            if self.data[i][-1] - self.data[i][-2] == self.data[i + 1][-1]:
                continue
            print("BADDDDDDDDDDDDDDd")
            raise "bad cal"
        count = len(self.data[0])

        for i in self.data:
            if count != len(i):
                raise "bad tree"
            count -= 1
        
        

    def zeros_in(self):
        while self.data[-1].count(0) != len(self.data[-1]):
            tmp = self.data[-1]
            x = [tmp[i + 1] - tmp[i] for i in range(len(tmp) - 1)]
            self.data.append(x)
    
    def backtrack(self):
        self.data.reverse()
        self.data[0].append(0)
        number = 0

        for i in range(len(self.data) -1):
            number += self.data[i + 1][-1]
            self.data[i + 1].append(number)

        self.number = number
            

        #  1 2 z x
        #      y
        # x - z= y

        #1980437571
        #1993543191
        """
        -56 - x =  -3
        x = 56 - 3
        x = 53

        -542 - x = 53


        -542 + 56

        """



        

with open("data.txt") as file:
    input_data = file.read()
    main(input_data)



# x - -56 = -3 
#