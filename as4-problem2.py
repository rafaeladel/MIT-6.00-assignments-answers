def nestEggFixed(salary, save, growth):	
	retire_list = []
	retire_list.append(salary*save)
	for i in range(0,len(growth)):
		retire_list.append(retire_list[i] * (1 + 0.01 * growth[i]) + salary * save)
		print "Year : %d" % i, "Fund : %f" % retire_list[i], "of growth : %f" % growth[i]
		
g_arr = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ,1.0]
nestEggFixed(500, 0.1, g_arr)
