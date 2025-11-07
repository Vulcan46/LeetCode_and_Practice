class Node:
    def __init__(self, val, is_head=False, next_node=None, count=0):
        self.val = val
        self.next = next_node
        self.isHead = is_head
        if is_head:
            self.count = 1
        else:
            self.count = count

    def add_node_at_end(self, val):
        if self is None:
            head: Node = Node(val, is_head=True, next_node=None, count=1)
            return head
        else:
            curr = self
            curr.count += 1
            while curr.next is not None:
                curr = curr.next
            new_node = Node(val)
            curr.next = new_node
            return self

    def add_node_at_i(self, val, i):
        if i == 0 or i==1:
            new_head = Node(val, is_head=True, next_node=self, count=self.count + 1)
            return new_head
        elif i > self.count:
            self.add_node_at_end(val)
        else:
            k = 1
            curr = self
            curr.count += 1
            while k+1<i:
                curr = curr.next
                k += 1
            new_node = Node(val)
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            return self

    def delete_node_at_i(self, i):
        curr = self
        if i>curr.count or i<1:
            print("Cannot delete")
        curr.count -= 1
        k = 1
        while k < i:
            curr = curr.next
            k += 1
        temp = curr.next.next
        curr.next.next = None
        curr.next = temp
        
    def print_linked_list(self):
        curr = self
        op =""
        while curr is not None:
            if curr.next is None:
                op = op + str(curr.val)
            else:
                op = op + str(curr.val) + "->"
            curr = curr.next
        print(op)

    def get_size(self):
        return self.count


head = Node(1,True)
head.add_node_at_end(2)
head.add_node_at_end(0)
head.add_node_at_end(9)
head.add_node_at_end(-1)
head.add_node_at_end(3)
head.add_node_at_end(7)
head.add_node_at_i(4,5)
head = head.add_node_at_i(99,1)
head.print_linked_list()
