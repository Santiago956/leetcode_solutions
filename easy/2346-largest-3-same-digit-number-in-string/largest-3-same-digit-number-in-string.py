class Solution:
    def largestGoodInteger(self, num: str) -> str:
        biggest = 0
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                if int(num[i:i+3]) >= int(biggest):
                    biggest = num[i:i+3]
        return "" if biggest == 0 else biggest
            