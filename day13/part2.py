imptest = """#..#..#..##..#.
...#..##.##.#..
###.#.########.
##.#...##..##..
#.####...##...#
.####.#.####.#.
##.##..######..
.####..#....#..
.##.##.##..##.#
..#.##...##...#
#.#.#.##.##.##.
#####.#.#..#.#.
...##...####...
#.#..##.#..#.##
.####.#.####.#.
.####.#.####.#.
#.#..##.#..#.##"""


test1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
"""
##.####.######.##
.#.#..#.#....#.#.
...#..#...##...#.
###....########..
#..#..#..####..#.
.#.#..#.#.##.#.#.
...####...##...##
..##..##......##.
##.#..#.######.#.
..#....#....#.#..
..#....#......#..
#...##...####...#
#.######.####.###
..##..##......##.
#........####...."""


test2 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

.#.##.#.#
.##..##..
.#.##.#..
#......##
#......##
.#.##.#..
.##..##.#

#..#....#
###..##..
.##.#####
.##.#####
###..##..
#..#....#
#..##...#"""


def parser(data):
    return data.split("\n\n")


def main(data):
    data = parser(data)
    refl = Reflection(data)


class Reflection:

    def __init__(self, data):
        self.patterns = data
        self.count = 0
        self.solve()

    def solve(self):
        self.tot = 0
        for i in self.patterns:
            self.tot += self.regulartest(i, func=self.doreflection)
        print("final ", self.tot)

    def regulartest(self, pattern: str, func) -> int:
        a = func(pattern.split("\n"))
        if a:
            return a * 100
        pattern = self.transpose(pattern)

        a = func(pattern.split("\n"))

        assert type(a) == int, "regular test gives non int"

        return a

    def quick_check_reflection(self, p: list):

        options = len(p)

        for i in range(1, options):
            before, after = p[:i], p[i:]
            before.reverse()

            minlen = min(len(before), len(after))

            if after[:minlen] == before[:minlen]:
                return i

        return False

    def doreflection(self, p: list) -> int:
        options = len(p)

        for i in range(1, options):
            before, after = p[:i], p[i:]
            before.reverse()

            minlen = min(len(before), len(after))
            chance = True

            # going through
            # not equal and chance
            # check for chance
            #    True - > false
            #     False - > break
            # no chance
            # break
            #

            # full  loop over
            # chance used return i

            # self.display("\n".join(p),pointer = i)

            for j in range(minlen):

                if (before[j] != after[j]):
                    if chance == True:
                        if self.is_1_similar(before[j], after[j]):
                            chance = False
                        else:
                            # print("due to no chance")
                            break

                    else:

                        # print("due to not similar")

                        break

            else:
                if not chance:
                    return i

        return False

    # utility functions

    def transpose(self, p: str) -> str:

        p = [list(lst) for lst in p.split("\n")]
        pp = [[(j, i) for j in range(len(p))] for i in range(len(p[0]))]

        for j in range(len(p)):
            for i in range(len(p[0])):

                pp[i][j] = p[j][i]

        return "\n".join(["".join(lst) for lst in pp])

    def is_1_similar(self, line1: str, line2: str, error=0) -> bool:
        # print(line1,line2)

        for i in range(len(line1)):
            if line1[i] != line2[i]:
                error += 1
            if error > 1:
                return False

        return True

    def display(self, patt: str, pointer=None) -> str:
        if pointer:
            print(pointer)

        for idx, i in enumerate(patt.split("\n")):
            i = i.replace("#", " ")
            if pointer == idx:
                print(">", i)
            else:
                print(" ", i)
        print()

    def tests(self):
        a = "123\n456"

        assert a == self.transpose(self.transpose(a))
        assert "14\n25\n36" == self.transpose(a)


with open("day13/data.txt") as file:
    input_data = file.read()
    main(input_data)


# 17622 low 2nd

# 33711 high 4th
# 35210 weird 5th
# 38894 high 1st

# 46594 3rd
