class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict={}
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] =1

        sorted_keys = sorted(num_dict.keys(),key=lambda x:num_dict[x],reverse = True)
        return sorted_keys[:k]
        



        