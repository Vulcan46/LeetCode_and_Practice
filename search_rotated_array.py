def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Identify which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target is in the sorted left half
            else:
                left = mid + 1  # Target is in the messy right half
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Target is in the sorted right half
            else:
                right = mid - 1  # Target is in the messy left half

    return -1


print(search_rotated_array([13,20,90,111,0,5,3,9,11],90))