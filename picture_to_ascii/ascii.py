# -*- coding:utf-8 -*-

from PIL import Image
import argparse

# 命令行输入参数处理
# ArgumentParser构造器的大部分调用都将使用description=关键字参数。这个参数给出程序做什么以及如何工作的简短描述
# 有些程序喜欢在参数的描述之后显示额外的关于程序的描述。这些文本可以使用ArgumentParser的epilog=参数指定：
# formatter_class格式化类ArgumentDefaultsHelpFormatter，将添加每个参数的默认值信息。
parser = argparse.ArgumentParser(description='tansfer pic to ascii',
                                 epilog='This fuction is interesting.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80, help='enter the width of the picture')  # 输出字符画宽
parser.add_argument('--height', type=int, default=80, help='enter the height of the picture')  # 输出字符画高
# 'version' - 它期待version=参数出现在add_argument()调用中，在调用时打印出版本信息并退出：
parser.add_argument('--version', action='version', version='%(prog)s 2.0')

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':

    im = Image.open(IMG)
    # 设置缩放图片的质量（ PIL.Image.NEAREST：最低质量， PIL.Image.BILINEAR：双线性，
    # PIL.Image.BICUBIC：三次样条插值，Image.ANTIALIAS：最高质量）
    # im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    im = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    # print txt

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
