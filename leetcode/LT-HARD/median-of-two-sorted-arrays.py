from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    n = len(nums1)
    m = len(nums2)
    lo, hi = 0, n

    #len(nums1) n should be less then len(nums2) to logic to work, if len(nums1) > len(nums2), switch ttem and call the func again

    if n > m:
        return findMedianSortedArrays(nums2, nums1)

    while lo <= hi:

        mid1 = (lo + hi) // 2 #mid of smaller array
        mid2 = ((n + m + 1) // 2) - mid1  #remaining of firsthalf of merged array


        l1 = float('-inf') if mid1 == 0 else nums1[mid1-1]
        r1 = float('inf') if mid1 == n else nums1[mid1]

        l2 = float('-inf') if mid2 == 0 else nums2[mid2-1]
        r2 = float('inf') if mid2 == m else nums2[mid2]

        if l1 <= r2 and l2 <= r1:

            if (n+m) % 2 == 0:
                return (max(l1,l2) + min(r1,r2))/2.0
            else:
                return max(l1, l2)
        
        if l1 > r2:
            hi = mid1 - 1
        
        else:
            lo = mid1 + 1

    return 0

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays(nums1=nums1, nums2=nums2))
