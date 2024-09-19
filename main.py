def drawline(offset = 0, length = 1):
    line = ' ' * length
    print(f'{" " * abs(offset)}\x1b[48;5;42m{line}\x1b[0m')

def romb(height = 30):
    offset = height // 2
    for line in range(0, height):
        drawline(offset, height - (2 * abs(line - height // 2)) - 1)
        offset -= 1
        


if __name__ == "__main__":
    romb(20)
    romb(70)