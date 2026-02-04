
nums =[1, 5, 8, 4, 7, 6, 5, 3, 1]
i = -1
j = len(nums) - 2
while j >= 0:
    if nums[j] < nums[j + 1]:
        i = j
        break
    j -= 1
if i == -1:
    left = i + 1
    right = len(nums) - 1
    while left < right:
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
else:
    j = len(nums) - 1
    while j > i:
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            break
        j -= 1
    left = i + 1
    right = len(nums) - 1
    while left < right:
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
print(nums)