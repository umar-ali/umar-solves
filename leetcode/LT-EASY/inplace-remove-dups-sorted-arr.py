
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
def remove_dups(nums:list):
    l = len(nums)
    if l <=1:
        return l
    i = 0
    j = 1
    while j < l:
        if nums[i] == nums[j]:
            j+=1
        else:
           nums[i+1] = nums[j]
           i+=1
           j+=1
    return i+1


if __name__ =="__main__":
    nums = [0,0,1,1,1,2,2,2, 3,3, 3,4]
    zeros = [0] * 10
    print(remove_dups(nums))