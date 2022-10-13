from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class A(Screen):
    a = []
    b = []
    lst = [[0 for i in range(9)] for j in range(9)]
    for i in range(1, 10):
        for j in range(1, 10):
            inp = str(input("Input " + str(i) + "," + str(j) + " :"))
            if (inp == ''):
                a.append(0)
                lst[i - 1][j - 1] = a
            else:
                a.append(int(inp))
                lst[i - 1][j - 1] = a

    def next(self):
            def is_empty(grid):
                for i in range(9):
                    for j in range(9):
                        if (grid[i][j] == 0):
                            return i, j
                return None, None

            def is_valid(grid, r, c, num):
                rw = grid[r]
                if (num in rw):
                    return False
                cl = [grid[i][c] for i in range(9)]
                if (num in cl):
                    return False
                rs = (r // 3) * 3
                cs = (c // 3) * 3
                for i in range(rs, rs + 3):
                    for j in range(cs, cs + 3):
                        if (grid[i][j] == num):
                            return False
                return True

            def sudoku2(grid):
                r, c = is_empty(grid)
                if (r is None):
                    return True
                for num in range(1, 10):
                    if (is_valid(grid, r, c, num)):
                        grid[r][c] = num
                        if (sudoku2(grid)):
                            return True

                    grid[r][c] = 0
                return False

            grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                    [5, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 7, 0, 0, 0, 0, 3, 1],
                    [0, 0, 3, 0, 1, 0, 0, 8, 0],
                    [9, 0, 0, 8, 6, 3, 0, 0, 5],
                    [0, 5, 0, 0, 9, 0, 6, 0, 0],
                    [1, 3, 0, 0, 0, 0, 2, 5, 0],
                    [0, 0, 0, 0, 0, 0, 0, 7, 4],
                    [0, 0, 5, 2, 0, 6, 3, 0, 0]]
            sudoku2(grid)
            return grid

class B(Screen):
    o = A()
    ar = o.next()
    g = sum(ar,[])

class M(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class main(App):
    def build(self):
        return kv

o = main()
o.run()

