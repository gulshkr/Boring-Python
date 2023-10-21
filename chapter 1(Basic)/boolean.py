class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_middle(self):
        if not self.head:
            return None

        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr.value

# Create a linked list
linked_list = LinkedList()
values = [1, 2, 3, 4, 5]
for value in values:
    linked_list.append(value)

# Find the middle of the linked list
middle = linked_list.find_middle()
if middle is not None:
    print("The middle of the linked list is:", middle)
else:
    print("The linked list is empty.")