import os
import time 


defaults = """
test = \"""  \"""


def parser(data):
    pass

def main(data):
    pass


with open("data.txt") as file:
    input = file.read()
    main(test)

"""
defaults2 = """

with open("part1.py") as file:
    data = file.read()

with open("part2.py","w") as file:
    file.write(data)

"""


def setupday(day = None):
    if not day:
        day = time.localtime().tm_mday
    dirname = "day" + str(day)
    try:
        os.mkdir(dirname)
    except:
        print("dir exists")
        return
    f = open(dirname + "/part1.py","w")
    f.write(defaults.format(day = day))
    f.close()
    f = open(dirname + "/part2.py","a")
    f.write(defaults2.format(day = day))
    f.close()
    f = open(dirname + "/data.txt","a").close()



def sample():
    pass
    if __name__ == "__main__":
        exit()
    print(__file__)
    return
    with open(__file__,"w") as file:
        file.write(defaults)



if __name__ == "__main__":
    setupday()
    



