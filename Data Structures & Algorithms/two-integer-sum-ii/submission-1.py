class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        array = numbers
        left = 0
        right = len(array) - 1
        while left < right:
            current_sum = array[left] + array[right]

            if current_sum == target:
                return [left + 1, right+1]
            elif current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1