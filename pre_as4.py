def get_root(x, ep):
    low = 0
    high = max(x, 1.0)
    guess = ( low + high )/2.0
    loop_count = 0

    while abs(guess**2 - x) > ep and loop_count <=100:
        if guess**2 < x:
            low = guess
        else :
            high = guess
        
        guess = (low + high)/2.0
        loop_count += 1    
    print guess

get_root(25, 0.001)
get_root(9, 0.001)
