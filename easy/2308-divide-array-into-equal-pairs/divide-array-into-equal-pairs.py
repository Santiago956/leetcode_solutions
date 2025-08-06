class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
     quantity = {}

     for i in nums:
        if i in quantity:
            quantity[i] += 1
        else:
            quantity[i] = 1
    
    
     for count in quantity.values():
        if count % 2 != 0:
             return False
            
     return True