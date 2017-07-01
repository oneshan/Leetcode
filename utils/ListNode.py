class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def createListNode(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    printListNode(dummy.next)
    return dummy.next


def printListNode(head):
    arr = []
    while head:
        arr += head.val,
        head = head.next
    print("List: ", arr)
    return
