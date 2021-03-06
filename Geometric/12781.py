import sys


def isCCW(p1, p2, p3):
    ret = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    ret = ret - (p1[1] * p2[0]) - (p2[1] * p3[0]) - (p3[1] * p1[0])

    if ret > 0:
        return 1
    elif ret < 0:
        return -1
    else:
        return 0


def CrossCheck(x1, y1, x2, y2, x3, y3, x4, y4):
    r1 = isCCW([x1, y1], [x2, y2], [x3, y3])
    r2 = isCCW([x1, y1], [x2, y2], [x4, y4])
    r3 = isCCW([x3, y3], [x4, y4], [x1, y1])
    r4 = isCCW([x3, y3], [x4, y4], [x2, y2])

    if r1 * r2 == 0 and r3 * r4 == 0:
        if [x1, y1] > [x2, y2]:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if [x3, y3] > [x4, y4]:
            x3, y3, x4, y4 = x4, y4, x3, y3

        if [x1, y1] <= [x4, y4] and [x3, y3] <= [x2, y2]:
            return True
        else:
            return False

    if r1 * r2 < 0 and r3 * r4 < 0: # 등호를 넣으면 포개지는 모양도 포함
        return True
    else:
        return False

l = list(map(int, sys.stdin.readline().split()))
print(1) if CrossCheck(*l) else print(0)