class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False

first = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

first.next = second
second.next = third
third.next = fourth
fourth.next = second

print(has_cycle(first))
