class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        n = len(nums) - 1
        i,j=0,len(nums)-1
        while n>=0:
            if nums[n]%2==0:
                res[i] = nums[n]
                i +=1
                n -=1
            else:
                res[j] = nums[n]
                j -=1
                n -=1
        return res
