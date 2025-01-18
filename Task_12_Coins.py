# У Артемия есть бесконечное число монет, каждая из которых одного из трех номиналов.
# Его интересует, какие суммы от 1 до N рублей он может набрать в свой кошелек, если там заранее лежала монета величиной в 1 рубль.
# -----------------------------------------
def count_sums(limit, coins):
    possible_sums = [False] * (limit + 1)
    possible_sums[1] = True
    for coin in coins:
        for j in range(coin, limit + 1):
            if possible_sums[j - coin]:
                possible_sums[j] = True
    return sum(possible_sums)


limit = int(input())
coins = list(map(int, input().split()))
print(count_sums(limit, coins))
# ЧАСТИЧНОЕ РЕШЕНИЕ/ПРОЙДЕННЫХ ТЕСТОВ - 20
