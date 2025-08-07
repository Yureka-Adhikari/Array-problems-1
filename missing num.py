def missing_num(arr, arr_length):
    
    for j in range(1, arr_length + 1):
        if j not in arr:
            print("Missing number is:", j)
            return
            
    print("No missing number found in the array.")
    
arr = [1, 2, 3, 5, 6]
missing_num(arr, len(arr))