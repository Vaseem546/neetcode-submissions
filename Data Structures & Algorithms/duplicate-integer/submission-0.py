class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq_set=set()
        for i in nums:
            if i not in unq_set:
                unq_set.add(i)
            else:
                return True
        return False