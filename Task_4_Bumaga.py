# У Кости есть бумажка, на которой написано n чисел. Также у него есть возможность не больше, чем k раз, взять любое число с бумажки, после чего закрасить одну из старых цифр, а на ее месте написать новую произвольную цифру.
# На какое максимальное значение Костя сможет увеличить сумму всех чисел на листочке?
# --------------------------------------
def max_increase(n, k, numbers):
    increases = []
    for number in numbers:
        str_number = str(number)
        length = len(str_number)
        for i, digit in enumerate(str_number):
            d = int(digit)
            if d < 9:
                increase = (9 - d) * (10 ** (length - i - 1))
                increases.append(increase)
    increases.sort(reverse=True)
    max_sum_increase = sum(increases[:k])
    return max_sum_increase


n, k = map(int, input().split())
numbers = list(map(int, input().split()))

print(max_increase(n, k, numbers))
# РЕШЕНИЕ ПОЛНОЕ
