import time

def draw_solid_line(offset = 0, length = 1, color = 42):
    line = ' ' * length
    # print(f'{" " * abs(offset)}\x1b[48;5;{color}m{line}\x1b[0m')
    print(f'{" " * abs(offset)}\x1b[{color}m{line}\x1b[0m')

def draw_multicolor_line(offset = 0, color_list = [], length_list = []):
    line = ' ' * offset
    for i in range(len(color_list)):
        line += (f'\x1b[{color_list[i]}m{" " * length_list[i]}\x1b[0m')
    print(line)

def send_multicolor_line(offset = 0, color_list = [], length_list = []):
    line = ' ' * offset
    for i in range(len(color_list)):
        line += (f'\x1b[{color_list[i]}m{" " * length_list[i]}\x1b[0m')
    return line
    

def draw_chessboard_line(offset = 0, length = 25, color = 222):
    square = '  '
    domino = (f'\x1b[48;5;{color}m{square}\x1b[0m{square}\x1b[0m')
    print("  " * abs(offset) + domino * 25)

def romb(height = 30, color = 42):
    offset = height // 2
    for line in range(0, height):
        draw_solid_line(offset, height - (2 * abs(line - height // 2)) - 1, color)
        offset -= 1
        
def chessboard(length = 25, height = 3, color = 42):
    for line in range(0, height):
        draw_chessboard_line(line % 2, length, color)

black = 40
red = 41
green = 42
yellow = 43
blue = 44
purple = 45
light_blue = 46
white = 47

color_list= [black, red, green, yellow, blue, purple, light_blue, white]

def romb_animation(color_list):
        for i in range(100):
            color = color_list[i % len(color_list)]
            time.sleep(0.2)
            romb(20, color)
            print('\x1b[21A')

def flag_japan():
    wide = 60
    color_list_japan = [white, red, white]
    length_list_japan0 = [30, 0, 30]
    length_list_japan1 = [28, 4, 28]
    length_list_japan2 = [24, 12, 24]
    length_list_japan3 = [22, 16, 22]
    length_list_japan4 = [19, 22, 19]
    length_list_japan5 = [18, 24, 18]
    length_list_japan6 = [16, 28, 16]
    for i in range(20):
        if abs(10 - i) > 7:
            draw_multicolor_line(0, color_list_japan, length_list_japan0)
            continue
        if abs(10 - i) > 6:
            draw_multicolor_line(0, color_list_japan, length_list_japan1)
            continue
        if abs(10 - i) > 5:
            draw_multicolor_line(0, color_list_japan, length_list_japan2)
            continue
        if abs(10 - i) > 4:
            draw_multicolor_line(0, color_list_japan, length_list_japan3)
            continue
        if abs(10 - i) > 3:
            draw_multicolor_line(0, color_list_japan, length_list_japan4) #mb japan5
            continue
        if abs(10 - i) > 2:
            draw_multicolor_line(0, color_list_japan, length_list_japan5)
            continue
        
        draw_multicolor_line(0, color_list_japan, length_list_japan6)

# def draw_point():
#     width = 60
#     height = 30
#     # draw_multicolor_line(0, [black, white, black], [width])
#     for i in range(height):
        

def function_3x(height = 9):
    height = min(height, 30)
    for i in range(height, -1, -1):
        new_line = str(i)
        if abs(i) < 10:
            new_line += ' '
        if (i % 3 == 0):
            new_line += send_multicolor_line(0, [black, white, black], [i // 3 * 2, 1 * 2, (height // 3 - i // 3) * 2])
        else:
            new_line += send_multicolor_line(0, [black], [(height // 3 + 1) * 2])
        print(new_line)
    x_ray = "  "
    for i in range(height // 3 + 1):
        if i < 10:
            x_ray += " "
        x_ray += str(i)
    print(x_ray)

def draw_to_points_line_squared(offset_not_squared = 0, color_list = [black, white], source_list = []):
    line = ' ' * offset_not_squared
    for i in source_list:
        line += (f'\x1b[{color_list[i]}m{"  "}\x1b[0m')
    print(line)

def make_source_list(length = 30, points_list = []):
    source_list = []
    for i in range(length):
        source_list.append(0)
    for i in points_list:
        source_list[i] = 1
    return source_list

def draw_x_ray(length):
    x_ray = ""
    for i in range(length + 1):
        if i < 10:
            x_ray += " "
        x_ray += str(i)
    print(x_ray)

def fit_length(length, height):
    res = 0
    while res * (height - 1) + 1 < length:
        res += 1
    return res * (height - 1) + 1

def change_source_list(source_list, backward = 0, length = 60):
    res = []
    lr_coordinator = backward
    for i in source_list:
        if lr_coordinator == 0:
            if i - 1 >= 0:
                res.append(i - 1)
            lr_coordinator = 1
            continue
        if lr_coordinator == 1:
            if i + 1 < length:
                res.append(i + 1)
            lr_coordinator = 0
            continue
    return res

def pattern_hollow_rhombus(offset = 0, height = 9, length = 60):
    beginning_points_list = []
    radius = height // 2
    point = radius
    while point < 60:
        beginning_points_list.append(point)
        beginning_points_list.append(point)
        point += 2 * radius
    next_point_list = beginning_points_list
    for i in range(height // 2):
        draw_to_points_line_squared(0, [black, white], make_source_list(length, next_point_list))
        next_point_list = change_source_list(next_point_list, 0, length)
    for i in range(height // 2 + 1):
        draw_to_points_line_squared(0, [black, white], make_source_list(length, next_point_list))
        next_point_list = change_source_list(next_point_list, 1, length)
        
def txt_task():
    with open('sequence.txt', 'r') as sequence:
        data = list(sequence)
        total = 0
        lower_minus_5 = 0
        upper_minus_5 = 0
        for value in data:
            value = float(value)
            if value > 0:
                continue
            if value < -5:
                lower_minus_5 += 1
            if value > -5:
                upper_minus_5 += 1
        total = upper_minus_5 + lower_minus_5
        proc_upper = upper_minus_5 / total * 100
        proc_upper = round(proc_upper, 2)
        proc_lower = 100 - proc_upper
        print(f'Percentage of non-positive numbers above -5 is {proc_upper}%')
        print(f'Percentage of non-positive numbers under -5 is {proc_lower}%')
            


if __name__ == "__main__":
    length = 57
    height = 11
    pattern_hollow_rhombus(0, height, fit_length(length, height))
    flag_japan()
    function_3x(30)
    txt_task()