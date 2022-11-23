# colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# with open("D:/test_txt/Курс 'Python разработка'/rainbow_colors.txt", "w") as rainbow_colors:
#     for color in colors_list:
#         print(color, file=rainbow_colors)

with open("D:/test_txt/Курс 'Python разработка'/rainbow_colors.txt", "a") as rainbow_colors:
    print('dark green', file=rainbow_colors)
    print('dark blue', file=rainbow_colors)

colors_list = []
with open("D:/test_txt/Курс 'Python разработка'/rainbow_colors.txt", "r") as rainbow_colors:
    for color in rainbow_colors:
        colors_list.append(color.strip())
print(colors_list)

