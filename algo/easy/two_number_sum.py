def twoNumberSum(array, targetSum):

    array.sort()
    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer < right_pointer:
        currentSum = array[left_pointer] + array[right_pointer]
        if currentSum == targetSum:
            return [array[left_pointer], array[right_pointer]]
        elif currentSum < targetSum:
            left_pointer += 1
        elif currentSum > targetSum:
             right_pointer -= 1
            
    return [] 