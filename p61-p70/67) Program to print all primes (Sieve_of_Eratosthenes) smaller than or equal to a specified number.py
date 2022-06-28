def sieve_of_eratosthenes(m):

    prime = [True for _ in range(m + 1)]
    p = 2
    while p * p <= m:

        if prime[p]:

            for i in range(p * p, m + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, m + 1):
        if prime[p]:
            print(p)


if __name__ == '__main__':
    n = 20
    print("Following are the prime numbers smaller"),
    print("than or equal to", n)
    sieve_of_eratosthenes(n)
