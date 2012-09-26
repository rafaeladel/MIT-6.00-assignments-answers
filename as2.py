def test(x):
    z = 0
    for a in range(0,150):
        for b in range(0,150):
            for c in range(0,150):
                y = 6*a+9*b+20*c
                if y <= x :
                    if y == x:
                        print "this --> " , a, b, c                       
                    else:                    
                        print a, b, c, y
                        z = y
    print "The largest number that cannot be exactly found is : %s" % z
                    
