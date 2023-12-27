
test = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def parser(data):
   data = [lst.split("@") for lst in data.split("\n")]
   data = [(list(map(int,lst[0].split(","))),list(map(int,lst[1].split(",")))) for lst in data]



   return data

def main(data):
    data = parser(data)
    x = HaleSim(data,200000000000000,400000000000000)


class HaleSim:
    def __init__(self,data,least = 7,most = 27):
        self.data = data
        self.least = least
        self.most = most

        self.test()
    
    def test(self):
        self.intersection = 0
        for i in range(len(self.data)):
            for j in range(i):
                self.check(*self.data[j],*self.data[i])

              
                
            

        print(self.intersection)
    
    def check(self,a,b,c,d):
        x1, y1, x2, y2 = a[0],a[1],a[0] + b[0],a[1] + b[1]
        x3, y3, x4, y4 = c[0],c[1],c[0] + d[0],c[1] + d[1]

        A1, B1, C1 = y2 - y1, x1 - x2, x1 * y2 - y1 * x2
        A2, B2, C2 = y4 - y3, x3 - x4, x3 * y4 - y3 * x4

        determinant = A1 * B2 - A2 * B1

        if determinant == 0:
            return
        
        else:

            # intersection_x = (C1 * B2 - C2 * B1) / determinant
            # if self.least <= intersection_x <= self.most:
            #     if x2 >  x1:
            #         if intersection_x < x1:
            #             print("back 1")
            #     elif intersection_x > x1:
            #         print("back 2")
            # else:
            #     print("out x")

            # intersection_y = (A1 * C2 - A2 * C1) / determinant
            # if self.least <= intersection_y <= self.most:
            #     if (y2 > y1) :
            #         if (intersection_y < y1):
            #             print("back 3")

            #     elif intersection_y > y1:
            #         print("back 4")

            #     self.intersection += 1
            # else:
            #     print("out y")
            
            # print(a,c,intersection_x,intersection_y)

            intersection_x = (C1 * B2 - C2 * B1) / determinant
            if self.least <= intersection_x <= self.most:
                if x2 >  x1:
                    if intersection_x < x1:
                        return
                elif intersection_x > x1:
                    return
                if x4 >  x3:
                    if intersection_x < x3:
                        return
                elif intersection_x > x3:
                    return
            else:
                return

            intersection_y = (A1 * C2 - A2 * C1) / determinant
            if self.least <= intersection_y <= self.most:
                if (y2 > y1) :
                    if (intersection_y < y1):
                        return

                elif intersection_y > y1:
                    return
                if (y4 > y3) :
                    if (intersection_y < y3):
                        return

                elif intersection_y > y3:
                    return

                self.intersection += 1
            else:
                return
            
            # print(a,c,intersection_x,intersection_y)
        
        
    


with open("data.txt") as file:
    input_data = file.read()
    main(input_data)

