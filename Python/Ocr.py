import os, subprocess, sys


def ocr1():
    x = os.listdir('data')
    f2 = open("data/out.txt", "a")
    for name in x:
        if "Lcrop" in name:
            # print(name)
            try:

                subprocess.call("tesseract/tesseract.exe  data/Lcrop" + name[5:10] + ".jpg out -psm 10 digits")
                f = open('out.txt')
                s1 = f.read()
                f.close()
                subprocess.call("tesseract/tesseract.exe  data/Rcrop" + name[5:10] + ".jpg out -psm 10 digits")
                f = open('out.txt')
                s2 = f.read()
                f.close()
                # print("第" + name[5:10] + "秒时")
                # print(str(s1) + "比" + str(s2))
                f2.write(name[5:10] + ":")
                f2.write(str(int(s1[0:1])) + str(int(s2[0:1])) + "\n")
            except:
                pass

    f2.close()
    if os.path.exists("out.txt"):
        os.remove("out.txt")
