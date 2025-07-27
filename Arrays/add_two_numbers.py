# Runtime: 0 ms, faster than 100% of Python3 submissions
# Memory Usage: 17.88 MB, beats 57% of Python3 submissions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        iteration_num = 1
        carry_over = 0
        temp = ListNode(0)#temp variable to iterate through the loop
        answer = temp
        #return answer
        while l1 is not None or l2 is not None or carry_over != 0:
            current_sum = 0 #setting a variable to keep a track of the sum of current list of digits
            if l1 is not None:
                current_sum+=l1.val
                l1 = l1.next
            if l2 is not None:
                current_sum+=l2.val
                l2 = l2.next
            #print(current_sum,carry_over)
            if iteration_num == 1:
                if current_sum+carry_over > 9:
                    temp.val = (current_sum+carry_over)%10
                    carry_over = (current_sum+carry_over)//10
                else:
                    temp.val = (current_sum+carry_over)%10
                    carry_over=0
                iteration_num+=1
            else:
                if current_sum+carry_over > 9:
                    temp.next = ListNode((current_sum+carry_over)%10)
                    carry_over = (current_sum+carry_over)//10
                    #print(current_sum,carry_over,str(current_sum+carry_over),int(str(current_sum+carry_over)[1]),int(str(current_sum)[0]))
                else:
                    temp.next = ListNode((current_sum+carry_over)%10)
                    carry_over=0
                temp = temp.next
            #print(answer,carry_over,current_sum)
        #print(answer,temp)
        return answer
