def reverseArrayGroups(a, a_size,n):
    temp = 0
    while temp < a_size:
        
        start = temp
        end = min(temp + n - 1, a_size - 1)
        
        while start < end:
            a[start],a[end] = a[end], a[start]
            start += 1
            end -= 1
        temp += n
        
        
a = [1,2,3,4,5,6,7,8,9]
n = 2
reverseArrayGroups(a, len(a), n)

for i in range(0, len(a)):
    print(a[i], end=' ')
    