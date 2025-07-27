# Runtime: 3 ms, faster than 51% of Python3 submissions
# Memory Usage: 18 MB, beats 40% of Python3 submissions

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = 0
        len_of_nums1 = len(nums1)
        len_of_nums2 = len(nums2)
        rem = (len_of_nums1+len_of_nums2)%2
        i = 0
        j = 0
        num_of_loop = 0
        #print(rem,len_of_nums1,len_of_nums2)
        if rem==0:
            index_of_ans = (len_of_nums1+len_of_nums2)//2
            while num_of_loop<=index_of_ans:
                if i<len_of_nums1 and j<len_of_nums2:
                    #print(nums1[i],nums2[j])
                    if nums1[i]<=nums2[j]:
                        if num_of_loop == index_of_ans-1:
                            ans = nums1[i]
                        elif num_of_loop == index_of_ans:
                            ans=(ans+nums1[i])/2
                            break
                        i+=1
                    else:
                        if num_of_loop == index_of_ans-1:
                            ans = nums2[j]
                        elif num_of_loop == index_of_ans:
                            ans=(ans+nums2[j])/2
                            break
                        j+=1
                elif i<len_of_nums1:
                    #print(nums1[i])
                    if num_of_loop == index_of_ans-1:
                        ans = nums1[i]
                    elif num_of_loop == index_of_ans:
                        ans=(ans+nums1[i])/2
                        break
                    i+=1
                else:
                    if num_of_loop == index_of_ans-1:
                        ans = nums2[j]
                    elif num_of_loop == index_of_ans:
                        ans=(ans+nums2[j])/2
                        break
                    #print(ans)
                    j+=1
                num_of_loop+=1
        else:
            index_of_ans = ((len_of_nums1+len_of_nums2)//2)+1
            while num_of_loop<index_of_ans:
                if i<len_of_nums1 and j<len_of_nums2:
                    if nums1[i]<=nums2[j]:
                        if num_of_loop == index_of_ans-1:
                            ans = nums1[i]
                            break
                        i+=1
                    else:
                        if num_of_loop == index_of_ans-1:
                            ans = nums2[j]
                            break
                        j+=1
                elif i<len_of_nums1:
                    if num_of_loop == index_of_ans-1:
                        ans = nums1[i]
                        break
                    i+=1    
                else:
                    if num_of_loop == index_of_ans-1:
                        ans = nums2[j]
                        break
                    j+=1               
                num_of_loop+=1
        return ans
