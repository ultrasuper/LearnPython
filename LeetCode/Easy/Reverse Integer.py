class Solution:
    def reverse(self, x: int) -> int:
        self.x = x
        signed = 1
        if self.x >= 0:
            pass
        else:
            signed = -1
        tmp = str(abs(self.x))
        def reverse_string(self, my_str: str) -> str:
            self.my_str = my_str
            tmp = ''
            for i in range(len(self.my_str)):
                tmp += self.my_str[len(self.my_str) -1  - i]
            return tmp
        reverse_tmp = reverse_string(self, tmp)
        output = signed * int(reverse_tmp)
        if (output > 2**31 - 1) or (output < -(2**31)):
                return 0
        else: return output