# Runtime: 35 ms, faster than 81% of Python3 submissions
# Memory Usage: 17 MB, beats 83% of Python3 submissions

class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = str(x)
        negative = ''
        if reversed_x[0]=='-':
            negative = '-'
            reversed_x=reversed_x[1:]
        ans = ''
        for i in range(len(reversed_x)-1,-1,-1):
            ans+=reversed_x[i]
            #print(ans)
        if int(ans)>(2**31)-1:
            return 0
        return int(negative+ans)
