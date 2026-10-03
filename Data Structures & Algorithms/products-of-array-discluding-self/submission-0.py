class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefprod = [1]*len(nums)
        sufprod = [1]*len(nums)
        currprod =1 
        for i in range(len(nums)):
            prefprod[i] = currprod*prefprod[i]
            currprod *= nums[i]
        currprod = 1
        for i in range(len(nums)-1,-1,-1):
            sufprod[i] = currprod*sufprod[i]
            currprod *=nums[i]
        #print(prefprod)
        #print(sufprod)
        for i in range(len(nums)):
            prefprod[i] = prefprod[i]*sufprod[i]
        return prefprod
            