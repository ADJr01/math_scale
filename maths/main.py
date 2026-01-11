from maths.softmax import soft_max

if __name__ == '__main__':
    nums = [1,2,3]
    result = soft_max(nums)
    total = sum(result)
    print(result)
    print(total)