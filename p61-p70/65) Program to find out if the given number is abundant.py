def is_abundant(n):
    factor_sum = sum([factor for factor in range(1, n) if n % factor == 0])
    return factor_sum > n


check_num = int(input("Enter the number to be verified:"))

print(is_abundant(check_num))
