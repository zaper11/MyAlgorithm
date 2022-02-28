def mergeSort(nums):
    if len(nums) > 1:
        stand = len(nums) // 2
        left = nums[:stand]
        right = nums[stand:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    return nums


def findTarget(numArr, target):
    i = 0
    while i < len(numArr):
        if numArr[i] == target:
            return i + 1
        elif numArr[i] > target:
            return i + 1
        elif i == len(numArr) - 1:
            return i + 2
        i += 1


def solve(nums, target):
    nums = mergeSort(nums)
    ans = findTarget(nums, target)
    return ans
