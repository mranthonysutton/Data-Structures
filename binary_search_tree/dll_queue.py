from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0

        # Why is our DLL a good choice to store our elements?

        # Set the storage to the linked list from DoublyLinkedList
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add 1 to the size of the storage and add whatever value is passed in
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size == 0:
            return None

        # We want to set the value to a variable so we can return it
        else:
            value = self.storage.tail.value
            # Remove 1 from the size and call the helper function
            # and removes the item
            self.size -= 1
            self.storage.remove_from_tail()

            # return what was removed
            return value

    def len(self):
        return self.storage.length
