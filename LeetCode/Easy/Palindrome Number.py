class Solution:
    def isPalindrome(self, x: int) -> bool:
        true = True
        false = False
        if x < 0:
            return false
        elif x == 0:
            return true
        elif x > 0:
            origin = str(x)
            reverse = ''
            for i in range(len(origin)):
                reverse += origin[len(origin) - 1 - i]
            if origin == reverse:
                return true
            else:
                return false