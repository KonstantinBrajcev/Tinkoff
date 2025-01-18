# Леше в институте рассказали Малую теорему Ферма:
# a^(p − 1) ≡ 1 (mod p) p — простое
# С помощью этого утверждения можно искать обратное по модулю. А именно, если a ≢ (mod p),a ≡ (modp), то a^(−1) a ≡ 1 (mod p), a^(−1) = a^(p − 2).
# Теперь Леша решает домашнюю работу, в которой есть задача: надо посчитать ∑x=l,r 1/x(mod p)
# Помогите ему с этим.
# -----------------------------------
def modular_inverse(a, p):
    return pow(a, p - 2, p)


def sum_of_inverses(l, r, p):
    total_sum = 0
    for x in range(l, r + 1):
        total_sum = (total_sum + modular_inverse(x, p)) % p
    return total_sum


l, r, p = map(int, input().split())
result = sum_of_inverses(l, r, p)
print(result)
# ЧАСТИЧНОЕ РЕШЕНИЕ/ПРОЙДЕННЫХ ТЕСТОВ - 16
