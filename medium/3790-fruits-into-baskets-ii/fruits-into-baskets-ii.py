class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = 0
        for i in range(len(fruits)):
            for j in range(len(fruits)):
                if fruits[i] <= baskets[j]:
                    baskets[j] = -1
                    placed += 1
                    break
        return len(fruits) - placed
