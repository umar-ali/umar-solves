
def findDuplicate(nums:list[int]) -> int:
    #cycle detection
    #find start of the cycle

    #To find the cycles existence, slow moves one unit, fast moves double
    #if they meet (intersection point) show the cycel
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    #to find the start of cycle, 
    #move slow to start, and keep the fast at intersection
    #move them one unit, when they meet that's the cycle start
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast


if __name__ == "__main__":
    print(findDuplicate([2,4, 3, 1, 4, 5]))


