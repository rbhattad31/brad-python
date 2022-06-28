def amicable_sum(num):
	divisor_sum = [0] * num
	for i in range(1, len(divisor_sum)):
		for j in range(i * 2, len(divisor_sum), i):
			divisor_sum[j] += i
	# Find all amicable pairs
	result = 0
	for i in range(1, len(divisor_sum)):
		j = divisor_sum[i]
		if j != i and j < len(divisor_sum) and divisor_sum[j] == i:
			result += i
	return str(result)


range_num = int(input("Enter the range number:"))

print(amicable_sum(range_num))
