from collections import Counter
def removeElement(nums, val):
        numlen = len(nums)
        cnt=0
        for i in range(len(nums)):
                if nums[i] == val:
                        cnt+=1
                        numlen-=1
                else:
                        newidx = i-cnt
                        nums[newidx] = nums[i]
        return numlen


nums = removeElement([1,1,1,1], 1)

print (nums)