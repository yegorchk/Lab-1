import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset=0, length=1, color=222):
    line = " " * length
    return f"{' ' * offset}{SET_COLOR}{color}m{line}{END}"




def draw_sign(n):
    main_color = 237
    print(f'{draw_line(5, 11, main_color)*n}')
    print(f'{draw_line(5 + 5, 1, main_color)}{' '*5}'*n)
    print(f'{f'{draw_line(5, 11, main_color)}'*n}')
    print(f'{draw_line(5 + 2, 1, main_color)}{4*" "}{draw_line(1, 1, main_color)}{' '*2}'*n)
    print(draw_line(5, 11, main_color)*n)


if __name__ == "__main__":
    n = int(input())
    draw_sign(n)
    
