# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.



# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = ListNode(data) # create a new node
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print(node.val)
            node = node.next

class Solution:

    def addTwoNumbers(self, l1, l2):

        L1=LinkedList()
        L2=LinkedList()
        for j in range(len(l2)):
            L2.add_node(l2[j])
        for i in range(len(l1)):
            L1.add_node(l1[i])

        node1 =L1.cur_node
        node2 =L2.cur_node
        L3=LinkedList()
        while node2 and node1:
            val1=node1.val
            val2=node2.val
            sum=val1+val2
            if sum<=9:
                L3.add_node(sum)
                node1=node1.next
                node2=node2.next
            else:
                tmp=sum%10
                L3.add_node(tmp)
                node1=node1.next
                node2=node2.next
                node2.val=node2.val+1
        list=[]
        node=L3.cur_node
        while node:
            print(node.val)
            list.append(node.val)
            node=node.next
        list.reverse()
        newlist=list
        return newlist


if __name__ == "__main__":

    l1=[2, 4, 3]
    l2=[5, 6, 4]
    test=Solution()

    result=test.addTwoNumbers(l1,l2)
    print(result)
