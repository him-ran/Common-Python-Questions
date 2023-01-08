'''
Description: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
             Add the two numbers and return the sum as a linked list.
Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# to find the length of the linked list
def findlength(head):
    cur = head
    count = 0
    while (cur != None):
        count = count + 1
        cur = cur.next
    return count


# to convert linked list to array
def convertarr(head):
    len = findlength(head)
    arr = []
    index = 0
    cur = head

    while (cur != None):
        arr.append(cur.val)
        cur = cur.next

    return arr
    # printing the array which we created
    # printarray(arr, len)


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = convertarr(l1)
        l2 = convertarr(l2)
        num1 = int(''.join(map(str, reversed(l1))))
        num2 = int(''.join(map(str, reversed(l2))))
        sum = num1 + num2
        res = list(map(int, str(sum)))
        res = reversed(res)
        responseLL = lst2link(list(res))
        return responseLL





