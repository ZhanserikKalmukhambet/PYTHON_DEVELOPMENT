def bin_s(goal: int, a) -> int:
        l = 0
        r = len(a) - 1
        mid = -1
        
        while l <= r:
            mid = (l + r) // 2
            
            if goal > a[mid]:
                l = mid + 1
            elif goal < a[mid]:
                r = mid - 1
            else:
                return mid
        return -1
    
def twoSum(numbers, target: int):
    for i in range(len(numbers)):
        ind = bin_s(target - numbers[i], numbers[i:])
        if ind != -1:
            return [i, ind]