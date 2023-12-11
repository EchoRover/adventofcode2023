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


def problem1(inp):

    total = []
    for i in inp.split("\n"):    
        total.append(getnumber(i))
    print(sum(total))



with open("data.txt") as f:
    text = f.read()
    problem1(text)

