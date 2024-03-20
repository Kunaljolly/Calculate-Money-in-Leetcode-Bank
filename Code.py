class Solution:
    def totalMoney(self, n: int) -> int:
        i = 1
        count = 0
        for x in range(1,n+1):
            if x%7 != 0:
                count+=i
                i += 1
            else:
                count += i
                i -= 5
        return count

