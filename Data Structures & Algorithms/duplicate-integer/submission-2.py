class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        input = []

        for n in nums:
            if n in input:
                return True
            input.append(n)
        return False