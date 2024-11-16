class Node:
    def __init__(self, value=None) -> None:
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def value_at_index(self, index:int) -> int:
        if self.count-1 < index:
            return None
        temp = self.head
        count = 0
        while count < index:
            temp = temp.next
            count += 1
        return temp.val

    def insert_head(self, node: Node) -> None:
        temp = self.head
        self.head = node
        self.head.next = temp
        self.count += 1

    def insert_tail(self, node:Node) -> None:
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        self.count += 1

    def insert(self, index:int, node:Node) -> None:
        if self.count < index:
            print("index out of bounds")
            return
        elif index == 0:
            self.insert_head(node)
            return
        elif index == self.count:
            self.insert_tail(node)
            return

        temp = self.head
        count = 0
        while count < index-1:
            count += 1
            temp = temp.next
        temp2 = temp.next
        temp.next = node
        node.next = temp2
        self.count += 1

    def delete_head(self) -> Node:
        if self.head is None:
            print("Empty linked list : delete_head()")
            return None
        temp = self.head
        self.head = self.head.next
        self.count -= 1
        return temp

    def delete_tail(self):
        if self.head is None:
            print("Empty linked list : delete_tail()")
            return None
        elif self.head.next is None:
            return self.delete_head()            
        
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        self.count -= 1


    def delete(self, index:int):
        if self.count == 0:
            print("nothing in linked list : delete()")
            return
        if self.count-1 < index:
            print("index out of bounds : delete()")
            return
        elif index == 0:
            self.delete_head()
            return
        elif index == self.count - 1:
            self.delete_tail()
            return
        elif self.count == 1:
            self.delete_head()
            return

        temp = self.head
        count = 0
        while count < index-1:
            temp = temp.next
            count += 1
        temp2 = temp.next.next
        temp.next = temp2
        self.count -= 1

    def max(self) -> int:
        if self.head is None:
            return None
        
        temp = self.head
        max = self.head.val
        while temp is not None:
            if max < temp.val:
                max = temp.val
            temp = temp.next
        return max

    def min(self):
        if self.head is None:
            return None
        
        temp = self.head
        min = self.head.val
        while temp is not None:
            if min > temp.val:
                min = temp.val
            temp = temp.next
        return min

    def print_linked_list(self):
        if self.count == 0:
            print("Linked list is empty : print_linked_list()")
            return
        
        temp = self.head
        while temp.next is not None:
            print(str(temp.val) + ">", end = "")
            temp = temp.next
        print(str(temp.val))

    def __len__(self):
        return self.count

def main():
    ll = LinkedList()

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    ll.insert_head(n1)
    ll.insert_head(n2)

    ll.print_linked_list()

    ll.insert_tail(n3)
    print("length: " + str(len(ll)))
    ll.print_linked_list()

    print("Value at index 4: " + str(ll.value_at_index(4)))
    print("Value at index 0: " + str(ll.value_at_index(0)))

    ll.insert(2, n4)
    ll.insert(3, n5)

    print("Max: " + str(ll.max()))
    print("Min: " + str(ll.min()))

    ll.print_linked_list()
    
    ll.delete(5)
    ll.delete(2)
    ll.delete(2)
    ll.delete(2)
    ll.delete(1)
    ll.delete(0)

    ll.print_linked_list()


if __name__ == "__main__":
    main()

