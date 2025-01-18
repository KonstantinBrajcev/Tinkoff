# Миша сидел в переговорке и решил нарисовать ее план на листке бумаги. Когда он закончил рисовать план переговорки, он положил лист с планом на пол переговорки. Теперь ему стало интересно: а есть ли на плане точка, которая лежит ровно на том месте пола, за которое она отвечает?
# Помогите ему найти эту точку.
# -----------------------------------------
import math


def find_map(coodr, x, y):
    dx = math.sqrt((coodr[2] - coodr[0])**2 + (coodr[3] - coodr[1])**2)*- \
        1 if coodr[0] > coodr[2] else math.sqrt(
            (coodr[2] - coodr[0])**2 + (coodr[3] - coodr[1])**2)
    dy = math.sqrt((coodr[2] - coodr[4])**2 + (coodr[5] - coodr[3])**2)*- \
        1 if coodr[3] > coodr[5] else math.sqrt(
            (coodr[2] - coodr[4])**2 + (coodr[5] - coodr[3])**2)
    scalex = dx/x
    scaley = dy/y*-1
    new_coord = [coodr[0]+coodr[0]*scalex, coodr[1]-coodr[1]*scaley, coodr[0]+coodr[2]*scalex, coodr[1]-coodr[3]*scaley,
                 coodr[0]+coodr[4]*scalex, coodr[1]-coodr[5]*scaley, coodr[0]+coodr[6]*scalex, coodr[1]-coodr[7]*scaley]
    return new_coord


def task8(x, y, corners):
    xx, yy = 0, 0
    for _ in range(100):
        alpha = xx / x
        beta = yy / y
        xx = (1 - alpha) * ((1 - beta) * corners[0] + beta * corners[6]) + alpha * (
            (1 - beta) * corners[2] + beta * corners[4])
        yy = (1 - alpha) * ((1 - beta) * corners[1] + beta * corners[7]) + alpha * (
            (1 - beta) * corners[3] + beta * corners[5])
    return xx, yy


x, y = map(float, input().split())
coodr = list(map(float, input().split()))
while True:
    new_coodr = find_map(coodr, x, y)
    if (math.fabs(new_coodr[0] - new_coodr[4]) <= 0.00001 and math.fabs(new_coodr[1] - new_coodr[5]) <= 0.00001):
        result = (new_coodr[0], new_coodr[1])
        break
    else:
        coodr = new_coodr

print("{:.4f} {:.4f}".format(round(result[0], 4), round(result[1], 4)))
# ЧАСТИЧНОЕ РЕШЕНИЕ/ПРОЙДЕННЫЕ ТЕСТЫ - 5
