#19. 删除链表的倒数第 N 个结点

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list = ListNode(-1, head)
        front = list
        rear = head

        #后指针移动到对应删除位置的下一个位置
        for i in range(n):
            rear = rear.next

        #两个指针同时移动
        while rear is not None:
            front = front.next
            rear = rear.next

        #删除对应节点
        front.next = front.next.next

        return list.next

#测试
listNode = ListNode(-1)
front = listNode
for i in range(1):
    Node = ListNode(i)
    front.next = Node
    front = front.next
s = Solution()
s.removeNthFromEnd(listNode,2)
for j in range(1):
    listNode = listNode.next
    print(listNode.val,end="")
