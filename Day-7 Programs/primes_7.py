def sieve_of_eratosthenes(num):
    limit = num+1
    not_prime_num = set()
    prime_nums = []

    for i in range(2, limit):
        if i in not_prime_num:
            continue

        for f in range(i*2, limit, i):
            not_prime_num.add(f)

        prime_nums.append(i)

    return prime_nums


user_num = int(input("Enter the number: "))
print(sieve_of_eratosthenes(user_num))
