last_index = 0
count = 0
search_after = 0
target_list = []
s = "atgacatgcacaagtatgcat"

## USING RECURSION :

##def start_count(s, t):
##    global last_index
##    global count
##    last_index = s.find(t, last_index)
##    if last_index != -1:
##        last_index += 1
##        count += 1
##        return start_count(s, t)
##    else :
##        return count

##print start_count(s, "strong")


## USING LOOPS:

while True:    
    last_index = s.find("atgc", search_after)
    if last_index != -1:
        target_list.append(last_index)
        search_after = last_index + 1
        count +=1
    else:
        break
    
print count, target_list
