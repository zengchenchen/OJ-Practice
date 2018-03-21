class Solution:
    def isPalindrome(self, head):
        prev = None
        p = head
        while head:
            curr = ListNode(head.val)  # 重新建立一个链表，两链表的val进行对比
            head = head.next
            curr.next = prev
            prev = curr
        while prev:
            if prev.val != p.val:  # 初始输入链表并未变化，但head=None,所以使用p进行比较
                return False
            prev = prev.next
            head = head.next
        return True
