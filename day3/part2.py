test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def borderup(data):
    date = data.split("\n")
    data = data
    width = len(data.split("\n")[0])
    data = "."*width + "\n" + data + "\n" + "."*width
    print(data)


def getnumber(x,y,length,breadth,data):
    positions = [(1,1),(-1,-1),(0,1),(1,0),(1,-1),(0,-1),(-1,0),(-1,1)]
    numbers = []
    idx = []
    for pos in positions:
        newx = x + pos[0]
        newy = y + pos[1]

        if allowed(newx,newy,length,breadth):
            if data[newy][newx].isdigit():
                number,code = crawler(newx,newy,data,length,breadth,data[y][x])

                if not(code  in idx):
                    idx.append(code)
                    numbers.append(number)
    print(numbers)
    return numbers




def allowed(x,y,length,breadth):
    if x >= 0 and y >= 0 and x <length and y < breadth:
        return True
    return False


def crawler(x,y,data,length,breadth,main):
    defx = x
    defy = y
    number = data[y][x]
    code = (str(y) + str(x))

    defn = main
    
    
    while 1:
        x += 1
        
        if not allowed(x,y,length,breadth):
            break
        if data[y][x] == defn or data[y][x] == ".":
            break
        number += data[y][x]
        code += (str(y) + str(x))
    
    x = defx
    y = defy
    while 1:
        
        x -= 1
        if not allowed(x,y,length,breadth):
            break
        if data[y][x] == defn or data[y][x] == ".":
            break
        number = data[y][x] + number    
        code = (str(y) + str(x)) + code

        
    

    return int(number),code
    


def problem3(data):
    data = data.split("\n")
    breadth = len(data)
    
    length = len(data[0])
    total = []

    for j in range(breadth):
        for i in range(length):
            a = data[j][i]
            
            if a == "*":
                b = (getnumber(i,j,length,breadth,data))
                if len(b) == 2:
                    b1 = b[0] * b [1]
                    total.append(b1)
    print(sum(total))


    

with open("data.txt") as f:
    dd = f.read()
    problem3(dd)
