class ListNote(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList(object):
    def initlist(self, data):
        self.head = ListNote(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNote(i)
            p.next = node
            p = p.next

    def hasCycle(self):
        try:
            slow = self.head
            fast = self.head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


a = LinkList()
a.initlist([1, 2, 3, 2, 1])
print(a.hasCycle())
