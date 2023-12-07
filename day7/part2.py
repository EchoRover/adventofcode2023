
test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def parser_solver(data):
    #step
    data = data.split("\n")
    data = [(i.split())for i in data]
    data = [tuple((par[0],int(par[1]))) for par in data ]

    ranks = {key:[] for key in range(1,8)}
    for i in data:
        ranks[cardtype(i[0])].append(i)
    
    finalranks = []
    for i in range(1,8):
        ranks[i] = fixranks(ranks[i])
        finalranks.extend(ranks[i])
    score = 0
    for index,val in enumerate(finalranks):
        score += (val[1] * (index + 1))
    # print(finalranks)

    print(score)
        

def compare(a,b,mode_TF = False):
    """is a > b"""
    
    strength = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"][::-1]

    for idx,val in enumerate(a[0]):
        if val == b[0][idx]:
            continue
        if strength.index(val) > strength.index(b[0][idx]):
            if mode_TF:
                return True
            return [b,a]
        else:
            if mode_TF:
                return False
            return [a,b]
    return [a,b]

def fixranks(data: list) -> list:   
    if len(data) == 1 or len(data) == 0:
        return data 
    return insertionsort(data)

def insertionsort(arr: list) ->list:
    for i in range(1,len(arr)):
        key = arr[i]

        j = i - 1

        while j >= 0 and  not( compare(key,arr[j],mode_TF= True)):
            arr[j + 1] = arr[j]
            j -=1
        arr[j + 1] = key
    return arr






def cardtype(card):
    Uniques = set(list(card))
    al = len(Uniques)
    if "J" not in Uniques:    
        match al:
            case 1:
                return 7 #AAAAA five of kind
            case 5:
                return 1  #ABCDE high card 
            case 4:
                return 2 #ABCDD  one pair
            
            case 3:
                letters_list = list(card)
                for letter in Uniques:
                    if letters_list.count(letter) == 3:
                        return 4
                return 3            
            case 2:
                letters_list = list(card)
                for letter in Uniques:
                    if letters_list.count(letter) == 4:
                        return 6
                return 5
    match al:
        case 1:
            return 7
        case 5:
            return 2
        case 4:
            return 4


        case 2:
            return 7
            letters_list = list(card)
            for letter in Uniques:
                    if letters_list.count(letter) == 4:
                        return 7
            return 7
        case 3:
                letters_list = list(card)
                for letter in Uniques:
                    if letters_list.count(letter) == 3:
                        return 6
                if letters_list.count("J") == 2:
                    return 6
                return 5

        



            

#name  uni pt  joker1  jocker2 jocker3 jocker 4 jocker5
#AAAAA  1  7    7<  
#AAAAB  2  6    7<
#AAABB  2  5    7<       (aaaaa)       (bbbbb)
#AAABC  3  4     6<(aaaab)               6(bbbbc)
#AABBC  3  3             6(aaaac)           5(aaabb)
#AABCD  4  2    4(AAABC) 4(AAABC)<           
#ABCDE  5  1    2<   


        


def main(data):
    parser_solver(data)


with open("day7/data.txt") as file:
    input = file.read()
    main(input)



"""failed codes"""
def scorecard(card):
    # print(card)
    strength = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"][::-1]
    card = list(card)
    card = [strength.index(i) for i in card]
    multipler = [243,81,27,9,3]
    card = [card[i] * multipler[i] for i in range(5)]
    # print(sum(card))
    return(sum(card))


def ins(lst:list)->list:
    for i in range(1,len(lst)):
        pointer_val = lst[i]
        print(lst,i+1)

        pointer_back = i - 1

        while pointer_back >= 0 and pointer_val < lst[pointer_back]:
            print(lst,"before")
            lst[ pointer_back + 1] = lst[pointer_back]
            print(lst,"after")

            pointer_back -=1
        lst[pointer_back + 1] = pointer_val
    
    print(lst)

