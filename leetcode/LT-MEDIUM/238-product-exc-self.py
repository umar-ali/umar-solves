
def productExceptSelf(nums):
    ln = len(nums)
    result = [1] * ln
    prefix_prod = [1] * ln
    suffix_prod = [1] * ln

    #calculate prefix 
    for i in range(1, ln):
        prefix_prod[i] = prefix_prod[i-1] * nums[i-1]

    #calculate suffix
    for i in range(ln-2, -1, -1):
        suffix_prod[i] = suffix_prod[i+1] * nums[i+1]

    for i in range(ln):
        result[i] = prefix_prod[i] * suffix_prod[i]
    return result




   
    
if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))
