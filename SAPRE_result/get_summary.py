# -*- coding:utf-8 -*-

import os

# get original summary from DNBR.output

def get_filenamelist(dir, keyword):
    filenamelist = []
    # os.listdir()——指定所有目录下所有的文件和目录名。
    for s in os.listdir(dir):
        if keyword in s:
            filenamelist.append(s)
    return filenamelist

def get_orignal_summary(dir):
    filenamelist = get_filenamelist(dir, '.out')
    fileoutput = open(dir + '/Sapre_Summary.txt', 'w')
    for s in filenamelist:
        fileinput = open(dir + '/' + s, 'r')
        fileoutput.write(s + '\n')
        fileoutput.write('\n')
        while True:
            line = fileinput.readline()
            if (line != ''):
                if ('channel no.' in line):
                    fileoutput.write(line)
                    for index in range(7):
                        line2 = fileinput.readline()
                        fileoutput.write(line2)
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

# get_orignal_summary(os.getcwd() + '/mshimbaseload3_deplcr')
# get_orignal_summary(os.getcwd() + '/mshimbaseload3_nodeplcr')
# os.getcwd()——得到当前工作的目录。
get_orignal_summary(os.getcwd() + '/Realse')

# get parsed summary for excel

def find_keyline(file, keyword):
    line = 'hello world'
    while line != '':
        line = file.readline()
        if keyword in line:
            return line
    raise KeyError('keyword dosen\'t exist.)

def parse_ssls(file, keyword):
    outlist = [keyword, ]

    # seek(offset,whence=0)
    # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    # whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
    #         0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    file.seek(0,0)
	find_keyline(file, keyword)
	






