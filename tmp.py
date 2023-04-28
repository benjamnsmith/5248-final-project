import math, subprocess, shlex

nextB = 5
triedB = []
runs = 0
found = 0


def primes(n):
    sieve = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i, n + 1, i):
                sieve[j] = False
    return primes


def pollard(n):
    global runs
    global triedB
    global nextB
    global found

    runs += 1
    B = nextB
    triedB.append(B)
    prime_list = primes(B)
    print("Factors of {} are {}".format(B, prime_list))
    M = 1
    for q in prime_list:
        exponent = math.floor(math.log(B, q))
        M *= (q ** exponent)
        print("{} ^ ({})".format(q, exponent))
    print("M = {}".format(M))
    a = 2

    g = int(subprocess.run(shlex.split("wolframscript -c 'GCD[{}^{} - 1, {}]'".format(a, M, n)), capture_output=True, text=True).stdout)
    print("gcd({}^{}-1, {})".format(a, M, n))
    print("GCD: {}".format(g))

    if 1 < g < n:
        found = g
        return g
    elif g == 1:
        nextB = B+1
    elif g == n:
        nextB = B-1

    if nextB < 0 or nextB > n or nextB in triedB:
        return -1
    else:
        pollard(n)


print("Factoring 12283...")
pollard(12283)
print("A factor of 12283 is {}. It took {} runs to get there.".format(found, runs))