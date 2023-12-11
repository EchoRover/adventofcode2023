test = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
test2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def getnumber(line):
    num = "0"
    for i in line:
        if i.isdigit():
            num += i
            break
    for i in line[::-1]:
        if i.isdigit():
            num += i
            break
    return int(num)


def fixline(line):
    nums = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    for j in range(len(line)+1):
        current = line[:j]
        # print("stat",current,line)
        for i in nums:
            
            if current.find(i) > -1:
                current = current.replace(i,str(nums[i]).rjust(len(i),"_"))
                # print(current,i)
                
                line = current + line[j:]
                break
    
    # print(line,"final")
        
    return line.replace("_","")

def problem1(inp):
    

    total = []
    for i in inp.split("\n"):
        line = fixline(i)
        print(line)
        
        total.append(getnumber(line))
    print(sum(total))

# print(fixline("eighttwothree"))


with open("data.txt") as f:
    text = f.read()
    problem1(text)

