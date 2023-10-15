nums = [801, 400, 647, 706, 328, 802, 951, 860, 132, 591]

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return ("Found at index", i)
    return -1

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return ("Found at index", i) # Return the index where the target element is found
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if the target element is not in the array

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    print(nums,": this is after")

def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        # Flag to optimize the sorting process
        swapped = False

        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                # Swap if the element found is greater than the next element
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break
    print(nums)

print(nums,": this is before")

    
