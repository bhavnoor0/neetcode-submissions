class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = "".join(char.lower() for char in s if char.isalnum())
        return m == m[::-1]