def isPalindrome(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start]!= arr[end]:
            return False
        start += 1
        end -= 1

    return True

# Test Case
# arr = [1, 2, 3, 2, 1]
# print(isPalindrome(arr)) # True

# arr = [1, 2, 3, 4]
# print(isPalindrome(arr)) # False
def removeElements(arr, x):
    result = []

    for num in arr:
        if num!= x:
            result.append(num)

    return result

# Method 2: In-place using two pointers
def removeElementsInPlace(arr, x):
    k = 0 # pointer for next position

    for i in range(len(arr)):
        if arr[i]!= x:
            arr[k] = arr[i]
            k += 1

    return k # new length, arr[0:k] has answer

# Test Case
# arr = [3, 2, 2, 3], x = 3
# print(removeElements(arr, 3)) # [2, 2]

# arr = [0,1,2,2,3,0,4,2], x = 2
# k = removeElementsInPlace(arr, 2)
# print(k, arr[:k]) # 5 [0,1,3,0,4]
