def operate(operator, *args):

    def addition(nums):
        result = 0
        for num in nums:
            result += num
        return result

    def subtraction(nums):
        result = nums[0]
        for num in nums[1:]:
            result -= num
        return result

    def multiplication(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    def division(nums):
        result = nums[0]
        for num in nums[1:]:
            if num == 0:
                return 'Cannot divide by 0'
            result /= num
        return result

    operations = {
        '+': addition(args),
        '-': subtraction(args),
        '*': multiplication(args),
        '/': division(args)
    }

    return operations[operator]


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
