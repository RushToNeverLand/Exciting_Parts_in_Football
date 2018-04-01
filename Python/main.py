# -*- coding: utf-8 -*-
from Ocr import *
from Captcha import *
from functions import *
import subprocess
import locale, sys

def getinfo(infile):
    cmd = 'ffmpeg.exe -i "' + infile + '"'
    subprocess.call(cmd)


# print(locale.getdefaultlocale())
def analyze(infile, outfile, start, end):
    capcha1(infile, start, end, 120)
    ocr1()
    changes = readChange()
    ans = []
    for change in changes:
        killtemp()
        capcha1(infile, int(change[0]) - 10, int(change[1]) + 10, 10)
        ocr1()
        changes2 = readChange()
        for change2 in changes2:
            killtemp()
            capcha1(infile, int(change2[0]) - 1, int(change2[1]) + 1, 1)
            ocr1()
            changes3 = readChange()
            ans.append(changes3[0][0])
    killtemp()
    i = 1
    for good in ans:
        cutscene(infile, outfile, i, int(good))
        i = i + 1


def start(infile, outfile):
    length = getlength(infile)
    analyze(infile, outfile, 120, length - 120)
    open("D:/footballproject12345.txt","w")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
start(sys.argv[1], sys.argv[2])
# start('G:\Soccer\Video\西甲\【90分钟足球网】8月21日 西甲第1轮 巴萨vs贝蒂斯 全场 720P SKY 英语.mkv','F:/PycharmCode/Project')