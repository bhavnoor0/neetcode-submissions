class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = [0] * 26
        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord('a')] += 1
        left = 0
        right = len(s1)
        while right <= len(s2):
            count_s2 = [0] * 26
            for i in range(left, right):
                count_s2[ord(s2[i])-ord('a')] += 1
            if count_s2 == count_s1:
                return True
            else:
                right += 1
                left += 1  
        return False