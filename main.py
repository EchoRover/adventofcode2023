import os
import time 


defaults = """
test = \"""  \"""

with open("data.txt") as f:
    dd = f.read()
    problem{day}(test)

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
    f = open(dirname + "/part2.py","a").close()
    f = open(dirname + "/data.txt","a").close()


if __name__ == "__main__":
    setupday()



