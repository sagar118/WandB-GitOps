from typing import List

def sortColors(nums: List[int]) -> List:
    left, right = 0, len(nums) - 1
    idx = 0
    while idx <= right:
        if nums[idx] == 0:
            nums[left], nums[idx] = nums[idx], nums[left]
            left += 1
        elif nums[idx] == 2:
            nums[right], nums[idx] = nums[idx], nums[right]
            right -= 1
            idx -= 1
        idx += 1
    return nums

def test_unitTest():
    nums = [2,0,2,1,1,0]
#     assert sortColors(nums) == [0,0,1,1,2,2]
    assert sortColors(nums) == [0,0,1,1,2]
