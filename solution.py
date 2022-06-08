class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a=len(nums)+1
        lstfin = [0]*a
        finres=[]
        for x in nums:
            lstfin[x]+=1
        for x in range(1,a):
            if lstfin[x]==0:
                finres.append(x)
        return finres
        
