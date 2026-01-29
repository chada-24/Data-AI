def is_prime(n):
    if n <= 1:
        return "false"
    if n == 2:
        return "true"

    def check(i):
        if i == 1:
            return "true"
        if n % i == 0:
            return "false"
        return check(i - 1)

    return check(n - 1)

a = 5
print(is_prime(a))
