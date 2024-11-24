#Stack - LIFO

class Node:
    def __init__(self, v=0) -> None:
        self.value = v
        self.prev = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
    
    def push(self, node: Node) -> Node:
        node.prev = self.top
        self.top = node
        self.size += 1

    def pop(self) -> Node:
        if self.size == 0:
            print("Stack unpoppable")
            return
        #garbage collection automatically handled
        temp = self.top
        self.top = self.top.prev
        self.size -= 1
        print("removed: " + str(temp.value))
        return temp

    def peek(self) -> Node:
        if self.top is not None:
            print("Top of stack: " + str(self.top.value))
            return self.top
        else:
            print("Stack is empty : peek()")
            return

    def is_empty(self):
        if self.size == 0:
            print("Stack is empty : is_empty()")

    def print_stack(self):
        if self.top is not None:  # Ensure the stack is not empty
            print(self.recursing(self.top) + " < Top of Stack")
        else:
            print("Stack is empty : print_stack()")
            
    def recursing(self, node: Node) -> str:
        if node.prev is not None:
            return self.recursing(node.prev) + " < " + str(node.value)
        else:
            return str(node.value)
    
    def stack_size(self):
        print("Size: " + str(self.size))

def main():
    #print statments added in higher level
    s = Stack()
    node0 = Node()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    s.print_stack()

    s.push(node0)
    s.push(node1)
    s.push(node2)

    s.stack_size()

    s.print_stack()

    s.pop()
    s.pop()

    s.peek()
    
    s.pop()
    s.print_stack()
    s.peek()
    s.is_empty()

    s.stack_size()

if __name__ == "__main__":
    main()