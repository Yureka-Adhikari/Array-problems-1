def leaders(a,a_size):
    currentmax = a[a_size - 1]
    print(currentmax)
    
    for i in range(a_size-2, -1, -1 ):
        if a[i] > currentmax:
            currentmax = a[i]
            print(currentmax)
            
    
a = [12, 23, 2, 1, 345, 67, 90]
leaders(a, len(a))