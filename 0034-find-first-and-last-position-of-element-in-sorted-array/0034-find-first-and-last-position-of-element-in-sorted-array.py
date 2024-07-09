class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,h,mid=0,len(nums)-1,0
        res=[-1,-1]

        while l<=h:
            mid= (l+h)//2
            if target == nums[mid]:
                res[0]=mid
                h=mid-1
            elif nums[mid] < target:
                l=mid+1
            else:
                h= mid-1

        l,h,mid=0,len(nums)-1,0

        while l<=h:
            mid= (l+h)//2
            if target == nums[mid]:
                res[1]=mid
                l=mid+1
            elif nums[mid] < target:
                l=mid+1
            else:
                h= mid-1
        return res