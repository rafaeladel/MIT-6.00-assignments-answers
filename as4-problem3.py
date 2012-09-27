def postRetirement(savings, growth, expenses):	
	fund_arr = []
	fund_arr.append(savings* (1 + 0.01 * growth[0]) - expenses)
	for i in range(1,len(growth)):
		fund_arr.append(fund_arr[i-1] * (1 + 0.01 * growth[i]) - expenses)
		print "End of year : %d" % i, "Fund : %f" % fund_arr[i], "of growth : %f" % growth[i]
		
g_arr = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ,1.0]
postRetirement(1000, g_arr, 100.0)
