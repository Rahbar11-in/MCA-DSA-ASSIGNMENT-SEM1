class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous

def print_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(values)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print_list(head)
head = reverse_list(head)
print_list(head)
