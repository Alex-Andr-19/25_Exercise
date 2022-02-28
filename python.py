ans_list = []

for m in range(30):
	for n in range(30):
		if 200000000 <= 2**m*3**n <= 400000000:
			ans_list.append(str(2**m*3**n))

ans_list.sort()

print('\n'.join( [f'{i+1} - {ans_list[i]}' for i in range(len(ans_list))] ))
