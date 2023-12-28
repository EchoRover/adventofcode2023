from collections import deque
test = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def parser(data):
    return data.split("\n")


def main(data, steps):
    data = parser(data)
    step = Steps(data, steps)


class Steps:
    def __init__(self, data, steps):
        self.data = data
        self.steps = steps
        self.length = len(self.data[0])
        self.breadth = len(self.data)
        self.getorigin()

        self.move()

    def move(self):
        self.seen = set()
        final = set()
        fin = 0
        queue = deque([(self.x, self.y, 0, 0, 0)])
        a = 0
        b = 0
        while queue:
            a += 1
            x, y, drx, dry, dist = queue.popleft()

            if (x, y, dist) in self.seen:
                b += 1

                continue
            self.seen.add((x, y, dist))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                nx = x + dx
                ny = y + dy

                if self.data[ny % self.breadth][nx % self.length] != '#':

                    if dist + 1 == self.steps:
                        fin += 1
                        final.add((nx, ny))

                    else:
                        queue.appendleft((nx, ny, dx, dy, dist + 1))

            # self.display(seen)

        print(len(final), fin, fin - len(final))
        # print(self.seen)

        print(f"seen length = {len(self.seen)} \nloop_called(a) = {a}")
        print(f"a = {a} \n(in seen and gone back)b = {b} \na + b = {a + b}")
        print(f"\nAnswer for {self.steps} is", len(final))

    def display(self, data):
        print(data)
        tmp = [list(lst.replace('.', ' ').replace('#', '.'))
               for lst in self.data]

        for x, y in data:
            tmp[y][x] = '0'
        for i in tmp:
            print("".join(i))
        print()

    def getorigin(self):
        for y in range(self.breadth):
            for x in range(self.length):
                if self.data[y][x] == 'S':
                    self.x, self.y = x, y
                    return


with open("day21/data.txt") as file:
    input_data = file.read()
    main(test, 1000)
