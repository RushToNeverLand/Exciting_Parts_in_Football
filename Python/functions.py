import os
import shutil, subprocess


def killtemp():
    shutil.rmtree("data")


def readChange():
    cur = []
    res = []
    f = open("data/out.txt")
    lines = f.readlines()
    last = lines[0][6:8]
    lastline = lines[0]
    for line in lines:
        # print(line.strip('\n'))
        # print(line[0:5])
        # print(line[6:8])
        if line[6:8] != last:
            cur.append(lastline[0:5])
            cur.append(line[0:5])
            res.append(cur)
            cur = []
        last = line[6:8]
        lastline = line

    f.close()
    return res


def cutscene(infile, outdoc, num, change):
    if os.path.exists(outdoc):
        pass
    else:
        os.makedirs(outdoc)
    subprocess.call(
        'ffmpeg.exe  -ss ' + str(
            change - 30) + ' -i "' + infile + '" -y -vcodec copy -acodec copy -t 90 ' + outdoc + '/' + str(
            num) + '.mp4')


def getlength(infile):
    output = subprocess.Popen(
        'ffprobe.exe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "' + infile + '"',
        stdout=subprocess.PIPE, shell=True).communicate()
    return int(float(str(output[0].decode('UTF-8'))))

