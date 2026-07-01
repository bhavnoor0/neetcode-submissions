class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        array = set(nums)
        longest = 0

        for n in array:
            if n-1 not in array:
                length = 1
                while n + length in array:
                    length += 1
                longest = max(length, longest)

        return longest
