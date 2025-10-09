
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

if __name__ == "__main__":
    # print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) #[[-1, 0, 1], [-1, -1, 2]]
