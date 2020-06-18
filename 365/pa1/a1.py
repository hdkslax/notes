# 365 programming project 1

'''
Q1. Given input Y Co Cg, print out the corresponing Y U V.
Y Co Cg are all integers in range [0..255]; Y U V should be rounded to the integers as well.
'''


def YCoCg_to_YUV(YCoCg=[]):
    Y = YCoCg[0]
    Co = YCoCg[1]
    Cg = YCoCg[2]

    # calculate corresponding RGB
    R = Y + Co - Cg
    G = Cg + Y
    B = Y - Co - Cg

    # print(R, G, B)
    # calculate corresponding YUV
    Y1 = round(0.299 * R + 0.587 * G + 0.114 * B)
    U = round((-0.299) * R + (-0.587) * G + (0.886) * B)
    V = round((0.701) * R + (-0.587) * G + (-0.114) * B)

    YUV = [Y1, U, V]

    return YUV


'''
Given an NxN picture (N in [4..16], and each pixel has a grey level in [0..255]), and a dither matrix
    0   3
    2   1
Print out resultant pictures with halftone printing and with ordered dithering, representatively. You may use "1" 
to represen "on", and "0" otherwise.
'''


def halftone_printing(picture=[[]]):
    # initialize a 2d array as return value
    N = len(picture[0])
    result = []
    for i in range(2 * N):
        result.append([0] * 2 * N)
    # print(result)
    for x in range(len(picture)):
        for y in range(len(picture[x])):
            temp_entry = []
            temp = int(picture[x][y] / (256 / 5))
            if temp > 0:
                temp_entry.append(1)
            else:
                temp_entry.append(0)
            if temp > 3:
                temp_entry.append(1)
            else:
                temp_entry.append(0)
            if temp > 2:
                temp_entry.append(1)
            else:
                temp_entry.append(0)
            if temp > 1:
                temp_entry.append(1)
            else:
                temp_entry.append(0)
            # print("the temp_entry is: ", temp_entry)
            result[2 * x][2 * y] = temp_entry[0]
            result[2 * x][2 * y + 1] = temp_entry[1]
            result[2 * x + 1][2 * y] = temp_entry[2]
            result[2 * x + 1][2 * y + 1] = temp_entry[3]

    for i in range(len(result)):
        print(result[i])

    print()


def ordered_dithering(picture=[[]]):
    # initialize a 2d array as return value
    N = len(picture[0])
    result = []
    for i in range(N):
        result.append([0] * N)

    for x in range(len(picture)):
        for y in range(len(picture[x])):
            temp = int(picture[x][y] / (256 / 5))
            if x % 2 == 0 and y % 2 == 0:
                if temp > 0:
                    result[x][y] = 1
            if x % 2 == 0 and y % 2 == 1:
                if temp > 3:
                    result[x][y] = 1
            if x % 2 == 1 and y % 2 == 0:
                if temp > 2:
                    result[x][y] = 1
            if x % 2 == 1 and y % 2 == 1:
                if temp > 1:
                    result[x][y] = 1

    for i in range(len(result)):
        print(result[i])

    print()


# main function for test
def main():
    print("Y U V =", YCoCg_to_YUV([105, 20, 45]))
    print("Y U V =", YCoCg_to_YUV([149, 69, 61]))
    print("Y U V =", YCoCg_to_YUV([108, 68, 7]))

    halftone_printing([[32, 25, 165, 231],
                       [157, 63, 79, 86],
                       [231, 36, 168, 132],
                       [15, 125, 218, 87]])

    ordered_dithering([[32, 25, 165, 231],
                       [157, 63, 79, 86],
                       [231, 36, 168, 132],
                       [15, 125, 218, 87]])

    halftone_printing([[95, 249, 7, 216, 60, 48, 210, 149],
                       [65, 168, 169, 36, 152, 46, 116, 192],
                       [219, 222, 250, 210, 88, 16, 96, 34],
                       [105, 56, 175, 249, 11, 108, 72, 215],
                       [114, 134, 4, 200, 229, 91, 103, 238],
                       [81, 17, 147, 146, 204, 20, 77, 36],
                       [51, 59, 112, 99, 103, 17, 46, 245],
                       [38, 151, 218, 143, 209, 165, 152, 198]])

    ordered_dithering([[95, 249, 7, 216, 60, 48, 210, 149],
                       [65, 168, 169, 36, 152, 46, 116, 192],
                       [219, 222, 250, 210, 88, 16, 96, 34],
                       [105, 56, 175, 249, 11, 108, 72, 215],
                       [114, 134, 4, 200, 229, 91, 103, 238],
                       [81, 17, 147, 146, 204, 20, 77, 36],
                       [51, 59, 112, 99, 103, 17, 46, 245],
                       [38, 151, 218, 143, 209, 165, 152, 198]])


if __name__ == "__main__":
    main()
