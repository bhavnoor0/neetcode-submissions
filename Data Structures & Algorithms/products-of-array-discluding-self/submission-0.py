class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(0, len(nums)):
            new_list = nums[:i] + nums[i+1:]

            product = 1
            for n in new_list:
                product *= n

            l.append(product)

        return(l)
        