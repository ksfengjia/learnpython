# -*- coding:utf-8 -*-

import os


def get_filenamelist(dir, keyword):
    """
    获取dir目录下包含keyword的filenamelist
    :param dir: 路径
    :param keyword: 关键词
    :return: filenamelist
    """
    filenamelist = []
    # os.listdir()——指定所有目录下所有的文件和目录名。
    for filename in os.listdir(dir):
        if keyword in filename:
            filenamelist.append(filename)
    return filenamelist


def get_orignal_summary(dir):
    """
    获取包含keystatement的首行到非空行
    :param dir: 路径
    """
    filenamelist = get_filenamelist(dir, '.out') # get original summary from SAPRE.out
    fileoutput = open(dir + '/Sapre_Summary.txt', 'w')
    keystatement = 'channel no.'

    for filename in filenamelist:
        fileinput = open(dir + '/' + filename, 'r')
        fileoutput.write(filename + '\n')
        fileoutput.write('\n')

        # while True should be used with break statement
        while True:
            line1 = fileinput.readline()
            if (line1 != ''):
                if (keystatement in line1):
                    while True:
                        line2 = fileinput.read()
                        if len(line2) > 1:
                            fileoutput.write(line2)
                        else:
                            break
            else:
                break
        fileinput.close()
    fileoutput.close()

# os.getcwd()——得到当前工作的目录。
# 处理/Realse/*.out文件
get_orignal_summary(os.getcwd() + '/Realse')


# get parsed summary for excel
def find_keyline(file, keyword):
    """

    :param file: 文件
    :param keyword: 关键词
    :return: 包含关键词的行
    """
    line = 'hello world'
    while line != '':
        line = file.readline()
        if keyword in line:
            return line
    raise KeyError('keyword dosen\'t exist.')


def parse_ssls(file, keyword):
    outlist = [keyword, ]

    # seek(offset,whence=0)
    # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    # whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
    #         0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    file.seek(0, 0)

    find_keyline(file, keyword)
#    find_keyline(file, 'ss-load_swing')
    for i in range(7):
        file.readline()
    # outlist.append(['dtime', 'power', 'md'])
    outlist.append(['axial zone', 'cor name', 'dnbr', 'rod no.' ,
                    'q surface', 'chf', 'uniform chf',
                    'faxial', 'fgrid','fwall', 'mass velocity', 'xe'])
    while True:
        splitline = file.readline().split()
        if len(splitline) > 1:
            if len(splitline) == 16:
                parseline = [splitline[i] for i in (0, 2, 5, 6, 7, 8, 9, 10, 11)]
                outlist.append(parseline)
            elif len(splitline[1]) == 25:
                parseline = [splitline[i] for i in (1, 3, 6, 7, 8, 9, 10, 11, 12)]
                outlist.append(parseline)
        else:
            break
    return outlist


def parse_SAPRE(file, keyword):
    outlist = [keyword, ]

    # seek(offset,whence=0)
    # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    # whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
    #         0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    file.seek(0, 0)

    find_keyline(file, keyword)
#    find_keyline(file, 'ss-load_swing')
    for i in range(7):
        file.readline()
    # outlist.append(['dtime', 'power', 'md'])
    outlist.append(['axial zone', 'cor name', 'dnbr', 'rod no.' ,
                    'q surface', 'chf', 'uniform chf',
                    'faxial', 'fgrid','fwall', 'mass velocity', 'xe'])
    while True:
        splitline = file.readline().split()
        if len(splitline) > 1:
            if len(splitline) == 16:
                parseline = [splitline[i] for i in (0, 2, 5, 6, 7, 8, 9, 10, 11)]
                outlist.append(parseline)
            elif len(splitline[1]) == 25:
                parseline = [splitline[i] for i in (1, 3, 6, 7, 8, 9, 10, 11, 12)]
                outlist.append(parseline)
        else:
            break
    return outlist

def get_parse_summary(fileinput, fileoutput, namelist, parsefunc):
    for keyword in namelist:
        for s in parsefunc(fileinput, keyword):
            # isinstance: Return whether an object is an instance of a class or of a subclass thereof
            # isinstance: 判断实例是否是这个类或者object是变量
            if isinstance(s, str):
                print s
                fileoutput.write(s)
            elif isinstance(s, list):
                print s
                fileoutput.write('    '.join(s))
            fileoutput.write('\n')
        fileoutput.write('\n')

filein = open(os.getcwd() + '/Realse/Sapre_Summary.txt', 'r')

fileout = open(os.getcwd() + '/Realse/Summary_DNBR.txt', 'w')

namelist_channel = []
for i in range(1,15):
    namelist_channel.append("%s%2d" % ('channel no.   ', i))
    print namelist_channel[i - 1]

get_parse_summary(filein, fileout, namelist_channel, parse_SAPRE)

filein.close()
fileout.close()

