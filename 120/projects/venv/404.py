def d():
    c = "DSKJ YOLZCOZ VUZY JU JSZ YLQCLILOKCOZ UI JSLCQY LY JHEBN GLRKHHZ. JSZ GHLQSJ BLQSJ YSUUJLCQ KOHUYY JSZ YWN - LY LJ K QUUV UH K GKV UAZC? JKWZ JSZ ZFKATBZ UI SEAKC HLQSJY."
    p = ""
    for char in c:
        if char == " ":
            p += " "
        elif char == "K":
            p += "a"
        elif char == "J":
            p += "t"
        elif char == "L":
            p += "i"
        elif char == "Y":
            p += "s"
        elif char == "S":
            p += "h"
        elif char == "U":
            p += "o"
        elif char == "I":
            p += "f"
        elif char == "Z":
            p += "e"
        elif char == "O":
            p += "c"
        elif char == "C":
            p += "n"
        elif char == "Q":
            p += "g"
        elif char == "V":
            p += "d"
        elif char == "G":
            p += "b"
        elif char == "H":
            p += "r"
        elif char == "W":
            p += "k"
        elif char == "R":
            p += "z"
        elif char == "N":
            p += "y"
        elif char == "E":
            p += "u"
        elif char == "A":
            p += "m"
        elif char == "B":
            p += "l"
        elif char == "D":
            p += "w"
        else:
            p += char
    print(p)


if __name__ == '__main__':
    # for a in range(1,25):
    #     for b in range(0,25):
    #         d(a,b)
    d()
