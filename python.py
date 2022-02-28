def is_del_on_three(num):
	tmp = num
	m_sum = 0

	while tmp > 0:
		m_sum += tmp%10
		tmp //= 10

	return m_sum


ans_list = []

for m in range(30):
	for n in range(30):
		if 200000000 <= 2**m*3**n <= 400000000:
			ans_list.append(str(2**m*3**n))

search_list = [201326592, 229582512, 254803968, 322486272]

ans_list.sort()

print('\n'.join( [f'{i+1} - {ans_list[i]}' for i in range(len(ans_list))] ))



'''

123234 = 2*2*2*3*3*3*5
5 != 2^m*3^n



'''

