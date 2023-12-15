
test = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def parser(data):
    return data.split(",")

def main(data):
    data = parser(data)
    hasher = Hash(data)


class Hash:
    def __init__(self,data):
        self.data = data
        # print(self.hash_string("HASH"))
        self.hashall()

    
    def hashall(self):
        total = 0
        for i in self.data:
            total += self.hash_string(i)
        print(total)

    

    def hash_string(self,string):
        currentval = 0

        for char in string:
            currentval += ord(char)
            currentval *= 17
            currentval %= 256
        return currentval

    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

