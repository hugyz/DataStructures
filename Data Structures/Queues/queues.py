class Node:
    def __init__(self, d = None) -> None:
        self.data = d
        self.next = None
        self.prev = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, node: Node) -> None:

        if self.head is None and self.tail is None:
            self.head = self.tail = node
            return

        temp = self.tail
        self.tail = node

        temp.next = self.tail       #init for old tail
        self.tail.prev = temp       #init for new tail
        self.size += 1
 
    def dequeue(self) -> None:
        if self.head is None:
            return

        self.head = self.head.next
        
        self.head.prev = None
        self.size -= 1
 
    def peek(self) -> None:
        if self.head is not None:
            print("Head value: " + str(self.head.data))
            return
        print("Queue is empty : peek()")
 
    def is_empty(self) -> bool:
        if self.head is not None or self.tail is not None:      #either head or tail works
            return False
        return True

    def q_size(self) -> int:
        if not self.is_empty():
            return self.size
        return 0 
 
    def print_queue(self) -> None:
        temp = self.head
        while temp.next is not None:
            print(str(temp.data), end = "")
            temp = temp.next
            if temp.next is not None: print("<", end = "")
        print("<" + str(temp.data))

    def clear(self) -> None:
        if self.head is None:
            return
        while self.head.next is not None:
            self.head = self.head.next
        self.head = None
        self.size = 0
 
def main():
    q = Queue()

    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    q.dequeue()
    q.peek()

    q.enqueue(n0)
    q.enqueue(n1)
    q.enqueue(n2)
    q.enqueue(n3)

    q.peek()
    print("size:" + str(q.q_size()))

    
    print("Empty") if q.is_empty() else print("Not Empty")

    q.print_queue()

    q.dequeue()
    q.peek()

    q.clear()
    q.peek()

    q.clear()
    
    print("size:" + str(q.q_size()))

if __name__ == "__main__":
    main()