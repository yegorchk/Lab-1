import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"
ifsquare = []


def move_cursor_left(n):
    print(f'\033[{n}D', end='')


def draw_line(offset=0, length=1, color=222):
    line = " " * length
    return f"{' ' * offset}{SET_COLOR}{color}m{line}{END}"


def draw_function():
    n = 12
    for y in range(12, -1, -1):
        print(f'{n} ', end='')
        print(draw_line(y**2,1,222))
        ifsquare.append(y**2)
        print()
        n -= 1


if __name__ == "__main__":
    draw_function()
    print('  ', end='')
    for i in range(169): 
        if i in ifsquare: 
            if i//10>0: move_cursor_left(1)
            print(i, end='')
        else:
            print(' ', end='')