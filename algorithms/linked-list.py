class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, node):
        nnode = node

        if not self.head:
            self.head = nnode
            return

        lnode = self.head
        while lnode.next:
            lnode = lnode.next
        lnode.next = nnode

    def prepend(self, data):
        nnode = Node(data)
        nnode.next = self.head
        self.head = nnode

    def insert_after(self, prev_node, data):
        nnode = Node(data)
        nnode.next = prev_node.next
        prev_node.next = nnode



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")
llist.insert_after_node(llist.head.next, "H")
llist.print_list()