class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        finlist=[]
        for x in range(len(nums)):
            y=abs(nums[x])-1
            if nums[y]>0:
                nums[y]*=-1
        px=[x+1 for x in range(len(nums)) if nums[x]>0 ]
        return px
