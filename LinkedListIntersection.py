# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        current_node_A = headA;
        current_node_B = headB;
        len_A = 0
        len_B = 0

        while (current_node_A):
            current_node_A = current_node_A.next;
            len_A = len_A + 1

        while (current_node_B):
            current_node_B = current_node_B.next;
            len_B = len_B + 1

        difference = len_A - len_B

        current_node_A = headA;
        current_node_B = headB;

        if (difference >= 0):
            for i in range(0, difference):
                current_node_A = current_node_A.next;

            while (current_node_A):
                if current_node_A == current_node_B:
                    return current_node_A
                current_node_A = current_node_A.next
                current_node_B = current_node_B.next

            return None

        else:
            for i in range(0, abs(difference)):
                current_node_B = current_node_B.next;

            while (current_node_A):
                if current_node_A == current_node_B:
                    return current_node_A
                current_node_A = current_node_A.next
                current_node_B = current_node_B.next

            return None





