class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            product=1
            j=0
            while j<len(nums):
                if i!=j:
                    product *= nums[j]
                j+=1
            output.append(product)
        return output
                
        