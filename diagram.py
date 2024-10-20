import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset=0, length=1, color=222):
    line = " " * length
    return f"{' ' * offset}{SET_COLOR}{color}m{line}{END}"


f = open('sequence.txt')


if __name__ == "__main__":
    s1 = 0
    s2 = 0
    n = 0

    for i in f:
        n += 1
        if n < 126:
            a = i.strip()
            s1 += float(a)
        elif 125<n<251:
            a = i.strip()
            s2 += float(a)

    s1, s2 = abs(s1), abs(s2)
    s1 /= 125
    s2 /= 125

    per1 = int(100*(s1/(s1+s2)))
    per2 = 100 - per1

    for i in range(100,0,-1):
        if i > per1:
            print(i)
        if i <= per1 and i > per2:
            print(f'{i}{draw_line(5,3,222)}')
        if i <= per1 and i <= per2:
            if i <= 9:
                print(f'{i}{draw_line(6,3,222)}{draw_line(4,3,222)}')
                continue
            print(f'{i}{draw_line(5,3,222)}{draw_line(4,3,222)}')

    print(f'{' '*7}s1{5*' '}s2')


f.close()