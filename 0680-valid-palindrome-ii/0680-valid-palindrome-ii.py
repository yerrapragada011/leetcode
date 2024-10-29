class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(string, left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        s = list(s)
        start = 0
        end = len(s) - 1
  
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return check_palindrome(s, start + 1, end) or check_palindrome(s, start, end - 1)
  
        return True