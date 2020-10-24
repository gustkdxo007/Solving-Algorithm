def minX(arr):
    x = 0
    sum_ = 0
    for i in range(len(arr)):
        tmp = sum_ + arr[i]
        if tmp >= 1:
            sum_ = tmp
        else:
            x += (abs(tmp)+1)
            sum_ += (abs(tmp)+1+arr[i])
    return x

print(minX([-5,4,-2,3,1,-1,-6,-1,0,5]))
print(minX([-5, 4, -2, 3, 1]))