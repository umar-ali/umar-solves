
#Time limit exceeded solution submitted on Oct 30, 2021
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         length = len(nums)
#         sum2 = {}
#         for i in range(length):
#             for j in range(length):
#                 if i!=j and (j,i) not in sum2.keys() and abs( nums[i] + nums[j]) in nums:               
#                         sum2[(i,j)] = nums[i] + nums[j]
#         solution = []
#         sum = 0
#         newset = set()
#         for i in range(length):
#             newset.add(i)
#         keyset = set(sum2.keys())
#         for j in keyset:
#             for i in newset  - {j[0],j[1]}:
#                 sublist = [nums[j[0]],nums[j[1]],nums[i]]
#                 sublist.sort()
#                 if sublist not in solution and nums[i] + sum2[j] == 0 :
#                  solution.append(sublist)
#         return solution

from collections import defaultdict
def threeSum(nums:list[int]) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    res = []


    for i in range(n-2):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = n-1
        while l < r:
            t = nums[i] + nums[l] + nums[r]
            if t == 0:
                res.append([nums[i] , nums[l] , nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]: 
                        l +=1 
                while l < r and  nums[r] == nums[r+1]:
                        r -= 1
            elif t < 0:
                l += 1
            else:
                r -= 1
    return res

if __name__ == "__main__":
    # print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) #[[-1, 0, 1], [-1, -1, 2]]
    # print(threeSum([-1, 0, 1, 2, -1, -4])) #[[-1, 0, 1], [-1, -1, 2]]
    print(threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
    # print(threeSum([0,0,0])) #[[-1, 0, 1], [-1, -1, 2]]
