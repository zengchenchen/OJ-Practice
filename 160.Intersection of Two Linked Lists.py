class ListNote(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def getIntersectionNode(self):
        headA = ListNote('a1')
        headA.next = ListNote('c1')
        headB = ListNote('B1')
        headB.next = ListNote('B2')
        headB.next.next = headA.next
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa


a = Solution()
print(a.getIntersectionNode())
