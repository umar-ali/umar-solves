
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
def remove_dups(nums:list):
    i = 1
    dups = 0
    l = len(nums)

    if l <=1:
        return l
        
    while True:
        if i + dups == l:
            break
        if nums[i-1] == nums[i]:
            dup= nums.pop(i)
            nums.append(dup)
            dups+=1
            continue
        i +=1
    return l - dups


if __name__ =="__main__":
    nums = [0,0,1,1,1,2,2,2, 3,3, 3,4]
    zeros = [0] * 10
    print(remove_dups(zeros))