class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.head is None:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value) 
        new_node = Node(value)
        prev = self.get(index - 1)
        next = prev.next
        prev.next = new_node
        new_node.next = next
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        next = temp.next
        prev.next = next
        temp.next = None
        self.length -= 1
        return temp
        
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def partition_list(self, num):
        if self.head is None:
            return None
        dummy1, dummy2 = Node(0), Node(0)
        prev1 = dummy1
        prev2 = dummy2
        temp = self.head
        while temp is not None:
            if temp.value < num:
                prev1.next = temp
                prev1 = prev1.next
            else:
                prev2.next = temp
                prev2 = prev2.next
            temp = temp.next
        prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next


# Testing the LinkedList class and its methods

# Create a LinkedList and perform operations
my_linked_list = LinkedList(1)

# Test 1: Print the initial list
print("Initial list:")
my_linked_list.print_list()

# Test 2: Append values to the list
print("\nAppending values 2, 3, 4, 5, 6 to the list...")
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

# Test 3: Print the list after appending values
print("\nList after appending 5 values:")
my_linked_list.print_list()

# Test 4: Prepend a value to the list
print("\nPrepending value 0 to the list...")
my_linked_list.prepend(0)

# Test 5: Print the list after prepending a value
print("\nList after prepending value 0:")
my_linked_list.print_list()

# Test 6: Pop a value from the list
print("\nPopping one value from the list...")
popped_node = my_linked_list.pop()
if popped_node:
    print(f"Popped value: {popped_node.value}")
else:
    print("List is empty, nothing to pop.")

# Test 7: Print the list after popping one value
print("\nList after popping one value:")
my_linked_list.print_list()

# Test 8: Pop the first element from the list
print("\nPopping the first value from the list...")
popped_first_node = my_linked_list.pop_first()
if popped_first_node:
    print(f"Popped first value: {popped_first_node.value}")
else:
    print("List is empty, nothing to pop.")

# Test 9: Print the list after popping the first value
print("\nList after popping the first value:")
my_linked_list.print_list()

# Test 10: Set value at a specific index
print("\nSetting value 10 at index 2...")
my_linked_list.set_value(2, 10)

# Test 11: Print the list after setting a value
print("\nList after setting value at index 2:")
my_linked_list.print_list()

# Test 12: Insert a value at index 2
print("\nInserting value 99 at index 2...")
my_linked_list.insert(2, 99)

# Test 13: Print the list after inserting a value
print("\nList after inserting value at index 2:")
my_linked_list.print_list()

# Test 14: Remove a value at index 3
print("\nRemoving value at index 3...")
removed_node = my_linked_list.remove(3)
if removed_node:
    print(f"Removed value: {removed_node.value}")
else:
    print("Invalid index, nothing to remove.")

# Test 15: Print the list after removing a value
print("\nList after removing value at index 3:")
my_linked_list.print_list()

# Test 16: Reverse the list
print("\nReversing the list...")
my_linked_list.reverse()

# Test 17: Print the list after reversing
print("\nList after reversing:")
my_linked_list.print_list()

# Test 18: Partition List:
my_linked_list.partition_list(5)
print("\nAfter partition_list() method: ")
my_linked_list.print_list()