class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        maxfreq = 0
        qnt = 0
        for num in nums:
            if num not in freq:
                freq[num] = 1
            elif num in freq:
                freq[num] += 1
        
        for number in freq.keys():
            if freq[number] > maxfreq:
                maxfreq = freq[number]
        
        for frequency in freq.values():
            if frequency == maxfreq:
                qnt += frequency
        return qnt

