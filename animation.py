import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = '\033[2J'
        

def draw_line(offset=0, length=1, color=222):
    line = " " * length
    return f"{' ' * offset}{SET_COLOR}{color}m{line}{END}"

colors = [[243,239], [254,252]]


def draw_animation():
    while True:
        for color in colors:
            color_1 = color[0]
            color_2 = color[1]
            print(f'{draw_line(5, 11, color_1)}{draw_line(0,2,color_2)}')
            print(f'{draw_line(5, 12, color_1)}{draw_line(0,2,color_2)}')
            print(f'{draw_line(5, 12, 223)}', end='')
            print(f'{draw_line(0, 2, color_1)}{draw_line(0,2,color_2)}')
            print(f'{draw_line(5, 12, 223)}', end='')
            print(f'{draw_line(0, 2, color_1)}{draw_line(0,2,color_2)}')
            print(f'{draw_line(5,2,223)}{draw_line(0,2,232)}{draw_line(0,2,223)}{draw_line(0,2,232)}{draw_line(0,4,223)}', end='')
            print(f'{draw_line(0, 2, color_1)}{draw_line(0,2,color_2)}')
            print(f'{draw_line(5, 12, 223)}', end='')
            print(f'{draw_line(0, 2, 223)}{draw_line(0,4,181)}')
            print(f'{draw_line(5,2,223)}{draw_line(0,2,223)}{draw_line(0,2,181)}{draw_line(0,2,181)}{draw_line(0,4,223)}', end='')
            print(f'{draw_line(0, 2, 223)}{draw_line(0,2,181)}')
            print(f'{draw_line(7, 10, 223)}', end='')
            print(f'{draw_line(0,2,181)}')

            print(f'\033[{8}A', end='')
            print(f'\033[{14}D', end='')

            time.sleep(2)

    
if __name__ == "__main__":
    draw_animation()