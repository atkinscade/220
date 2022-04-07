

def fibonacci(num):
    n_1, n_2 = 1, 1
    fib_seq = []
    count = 0
    while count < num and num > 1:
        fib_seq.append(n_1)
        result = n_1 + n_2
        n_1 = n_2
        n_2 = result
        count += 1
    return fib_seq[num - 1]


def double_investment(principal, rate):
    year = 0
    total = total0 = principal
    while total < 2*total0:
        total = total + total * rate + 1
        year += 1
    return year


def syracuse(num):
    nums = [num]
    while num != 1:
        if (num % 2) == 0:
            res = num // 2
            nums.append(res)
            num = res
        else:
            res = num * 3 + 1
            nums.append(res)
            num = res
    return nums


def goldbach(num):
    # get primes
    primes = []
    val = 1
    while val <= num:
        count = 0
        i = 2
        while i <= val // 2:
            if val % i == 0:
                count = count + 1
                break
            i = i + 1
        if count == 0 and val != 1:
            primes.append(val)
        val = val + 1
    # goldy function
    if (
        num % 2 != 0
    ):
        return None

    idx_a = 0
    idx_b = 0

    prime_a = primes[idx_a]
    prime_b = primes[idx_b]

    while prime_a + prime_b != num:
        if prime_b == primes[-1]:
            idx_a = idx_a + 1
            idx_b = idx_a + 1
            prime_a = primes[idx_a]
            prime_b = primes[idx_b]
        else:
            idx_b = idx_b + 1
            prime_b = primes[idx_b]
    return [prime_a, prime_b]






