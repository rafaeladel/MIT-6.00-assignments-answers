def nestEggFixed(salary, save, growth, years):	
	retire_list = []
	retire_list.append(salary * save)
	for i in range(1,years+1):
		retire_list.append(retire_list[i-1] * (1 + 0.01 * growth) + salary * save)
		print "Year : %d" % i, "Fund : %d" % retire_list[i-1] 
		
nestEggFixed(500, 0.1, 2, 10)
