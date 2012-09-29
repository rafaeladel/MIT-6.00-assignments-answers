import math
log_sum = 0
x = raw_input("Enter a number : ")
numRange = range(2, int(x)+1)

is_prime = True

for i in numRange:
    for x in range(2, i):
        if i % x == 0:
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime == True:
        log_sum += math.log(i)
        print i

print "Sum of log's : %e" % log_sum
print "Ratio : %d" % (log_sum/int(x))

