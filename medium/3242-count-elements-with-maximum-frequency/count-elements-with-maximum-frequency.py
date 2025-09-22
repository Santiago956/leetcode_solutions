
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        freq = Counter(nums)
        maxfreq = max(freq.values())
        return sum(value for value in freq.values() if value == maxfreq)

