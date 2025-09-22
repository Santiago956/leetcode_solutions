class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        qnt = 0
        for num in nums:
            if num not in freq:
                freq[num] = 1
            elif num in freq:
                freq[num] += 1
        
        maxfreq = max(freq.values())

        for frequency in freq.values():
            if frequency == maxfreq:
                qnt += frequency
        return qnt

