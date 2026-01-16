import numpy as np

if __name__ == '__main__':
    nums = np.random.random(10)
    max = np.max(nums)
    min = np.min(nums)
    max_index = np.argmax(nums)
    min_index = np.argmin(nums)
    print(f"Max is {max} at index {max_index}")
    print(f"Min is {min} at index {min_index}")