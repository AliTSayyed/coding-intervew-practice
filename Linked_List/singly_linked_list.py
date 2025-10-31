class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(3)

Head.next = A
A.next = B
B.next = C

# Traverse the list - O(n)

curr = Head
while curr:
    print(curr)
    curr = curr.next

# Display linked list - O(n)


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))


display(Head)


# Search for a node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False


search(Head, 7)
