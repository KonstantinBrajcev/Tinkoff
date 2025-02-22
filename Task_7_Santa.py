# В школе перед Новым Годом устраивают игру в Тайного Санту. Каждому ученику i выдается ученик ai, которому он должен подарить подарок.
# Костя, как администратор игры, определил каждому школьнику свое число ai. Но потом его коллега Маша спросила: А правда ли, что если начать цепочку подарков от школьника 1 к школьнику a1, потом aa1 и так далее, то цепочка замкнется на школьнике 1, после того, как задействует всех остальных учеников ровно по одному разу?
# Костя не знает, правда это или нет, но он собирается изменить ровно одно число ai, чтобы получить конфигурацию, которая устроит Машу. Помогите ему с этим.
# -------------------------------
def is_cycle(path):
    flag = 0
    cycle = [False] * len(path)

    for i in range(len(path)):
        if cycle[flag]:
            return False
        else:
            cycle[flag] = True
            flag = path[flag]

    for i in range(len(cycle)):
        if not cycle[i]:
            return False
    return flag == 0


n = int(input())
a = list(map(lambda x: x-1, map(int, input().split())))

no_gift = -1
double_gift = -1
double_gift2 = -1
have_double_gift = 0
have_no_gift = 0
have_other_error = 0
counters = [0] * n

for i in a:
    counters[i] += 1
for i in range(len(a)):
    if counters[i] == 2:
        have_double_gift += 1
    if counters[a[i]] == 2:
        if double_gift == -1:
            double_gift = i
        elif double_gift2 == -1:
            double_gift2 = i
    if counters[i] == 0:
        have_no_gift += 1
        no_gift = i
    if counters[i] > 2:
        have_other_error += 1
        break

if have_double_gift == 1 and have_no_gift == 1 and have_other_error == 0:
    index = double_gift
    tmp = a[index]
    a[index] = no_gift
    if is_cycle(a):
        print(index+1, no_gift+1)
    else:
        a[index] = tmp
        index = double_gift2
        a[index] = no_gift
        if is_cycle(a):
            print(index+1, no_gift+1)
        else:
            print("-1 -1")
else:
    print("-1 -1")
# ПОЛНОЕ РЕШЕНИЕ
