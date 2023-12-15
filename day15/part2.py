
test = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def parser(data):
    return data.split(",")

def main(data):
    data = parser(data)
    hasher = Hashmap(data)


class Hashmap:
    def __init__(self,data):
        self.data = data
        self.boxes = [[] for _ in range(256)]

        self.initialization()
        # self.view()
        self.power()

        
    def initialization(self):
        for line in self.data:
            label = line[:-1] if "-" in line else line.split("=")[0]
            # print(label)
            correct_box = self.hash_string(label)
            if "-" in line:
                # print("dele",correct_box)
                for i in self.boxes[correct_box]:
                    # print(i,"hello")
                    if label in i:
                        self.boxes[correct_box].remove(i)
                        break

    
            elif "=" in line:
                power = int(line.split("=")[-1])
                for i in self.boxes[correct_box]:
                    if label in i:
                        i[1] = power
                        break
                else:
                    self.boxes[correct_box].append([label,power])
            
            # self.view()
    
    def power(self):
        all_power = []

        for idx,box in enumerate(self.boxes):
            if box != []:
                for idy,lens in enumerate(box):
                    # print((1 + idx) ,(idy + 1) , lens[-1])
                    power = (1 + idx) * (idy + 1) * lens[-1]
                    all_power.append(power)
        
        print(sum(all_power))



    def view(self):
        for idx,i in enumerate(self.boxes):
            if i != []:
                print(idx,i)
        print()






    
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

    


with open("day15/data.txt") as file:
    input_data = file.read()
    main(input_data)

