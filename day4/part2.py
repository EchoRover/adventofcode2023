test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""



def cutter(line):
    cardno = line.split(":")[0].split()[-1]

    others = line.split(":")[-1].split("|")
    winning = others[0].split()
    ournos = others[-1].split()
    ss = score(winning,ournos)
    
    # print("* " + cardno,winning,ournos,ss,sep = "\n",end = "\n\n")

    return int(cardno),ss


def score(winning,our):
    score = 0
    for i in our:
        if i in winning:
            score += 1
    return score

def processor(data):
    copies = {key:1 for key in data}
    for card in data:
       updatecopies(copies,data,data[card])
    # print(copies)

    return sum(copies.values())

def updatecopies(copylist,data,values):
    for val in values:
        if data[val]:
            updatecopies(copylist,data,data[val])
        copylist[val] += 1


def problem4(data):
    total = {}

    for line in data.split("\n"):


        no,ss = (cutter(line)) 
        total[no] = list(range(no+1,no + ss +1))
         

    # for i in total:
    #     print(i,":",len(total[i]))
    result = processor(total)

    print(result)


with open("data.txt") as f:
    dd = f.read()
    problem4(dd)