class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s)-1
        while right > left:
            if s[left] != s[right]:
                if not((s[left] >='a' and s[left] <= 'z') or (s[left] >='0' and s[left] <= '9')):
                    left += 1
                    continue
                elif not((s[right] >='a' and s[right] <= 'z') or (s[right] >='0' and s[right] <= '9')):
                    right -= 1
                    continue
                else:
                    return False
            right -= 1
            left += 1
        return True