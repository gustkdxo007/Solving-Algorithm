def balancedSum(arr):
    answer = 0xffffff
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]
    for i in range(1, len(arr)-1):
        left = arr[i-1]
        right = arr[len(arr)-1] - arr[i]
        if left == right:
            answer = min(answer, i)
    return answer

print(balancedSum([1, 2, 3, 3]))