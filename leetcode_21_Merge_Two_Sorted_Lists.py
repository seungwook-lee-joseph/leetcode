# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = []
        while (1):
            if list1 == None:
                break
            else:
                result.append(list1.val)
                list1 = list1.next

        while (1):
            if list2 == None:
                break
            else:
                result.append(list2.val)
                list2 = list2.next
                
        result = sorted(result, reverse=True)

        ResultNode = None

        for i in range(0, len(result)):
            if ResultNode == None:
                ResultNode = ListNode()
            
            if i == 0:
                ResultNode.val = result[i]
            else:
                newNode = ListNode()
                newNode.val = result[i]
                newNode.next = ResultNode
                ResultNode = newNode
        
        return ResultNode
            
            