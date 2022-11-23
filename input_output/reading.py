# x = input('Input something: ')
# print('Output something: ' + x)

# lorem_ipsum_text = open("D:/test_txt/Курс 'Python разработка'/sample.txt", 'r')
# for line in lorem_ipsum_text:
#     print(line, end='')
# lorem_ipsum_text.close()

# lorem_ipsum_text = open("D:/test_txt/Курс 'Python разработка'/sample.txt", 'r')
# for line in lorem_ipsum_text:
#     if 'mary' in line.lower():
#         print(line, end='')
# lorem_ipsum_text.close()

# with open("D:/test_txt/Курс 'Python разработка'/sample.txt", "r") as lorem_ipsum_text:
#     for line in lorem_ipsum_text:
#         if 'mary' in line.lower():
#             print(line, end='')

# with open("D:/test_txt/Курс 'Python разработка'/sample.txt", "r") as lorem_ipsum_text:
#     line = lorem_ipsum_text.readline()
#     while line:
#         print(line, end='')
#         line = lorem_ipsum_text.readline()

# with open("D:/test_txt/Курс 'Python разработка'/sample.txt", "r") as lorem_ipsum_text:
#     lines = lorem_ipsum_text.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line)

with open("D:/test_txt/Курс 'Python разработка'/sample.txt", "r") as lorem_ipsum_text:
    text = lorem_ipsum_text.read()
print(text)