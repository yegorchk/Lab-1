import time
import os


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = '\033[2J'
        

def draw_line(offset=0, length=1, color=222):
    line = " " * length
    return f"{' ' * offset}{SET_COLOR}{color}m{line}{END}"

colors = [223, 181]


def draw_animation():
    while True:
        for color in colors:
            color_1 = color
            print(f'{draw_line(5, 11, 243)}{draw_line(0,2,239)}')
            print(f'{draw_line(5, 12, 243)}{draw_line(0,2,239)}')
            print(f'{draw_line(5, 12, 223)}', end='')
            print(f'{draw_line(0, 2, 243)}{draw_line(0,2,239)}')
            print(f'{draw_line(5, 12, 223)}', end='')
            print(f'{draw_line(0, 2, 243)}{draw_line(0,2,239)}')
            print(f'{draw_line(5,2,223)}{draw_line(0,2,232)}{draw_line(0,2,223)}{draw_line(0,2,232)}{draw_line(0,4,223)}', end='')
            print(f'{draw_line(0, 2, 243)}{draw_line(0,2,239)}')
            print(f'{draw_line(5, 12, 223)}', end='')
            print(f'{draw_line(0, 2, 223)}{draw_line(0,4,181)}')
            print(f'{draw_line(5,2,223)}{draw_line(0,2,223)}{draw_line(0,2,181)}{draw_line(0,2,181)}{draw_line(0,4,223)}', end='')
            print(f'{draw_line(0, 2, 223)}{draw_line(0,2,181)}')
            print(f'{draw_line(7, 2, 223)}{draw_line(0, 4, color)}{draw_line(0, 4, 223)}', end='')
            print(f'{draw_line(0,2,181)}')
            print(f'{draw_line(7, 2, 223)}{draw_line(0, 4, 223)}{draw_line(0, 4, 223)}', end='')
            print(f'{draw_line(0,2,181)}')

            time.sleep(0.2)

            os.system("clear")

    
if __name__ == "__main__":
    draw_animation()