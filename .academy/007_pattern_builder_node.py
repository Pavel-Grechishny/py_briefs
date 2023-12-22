class Node:
    id_ = 1
    
    def __init__(self, parent = None, name: str = 'node'):
        self.id = self.__class__.id_
        self.parent: Node = parent
        self.name: str = f'{name}_{self.id}'
        self.next: Node = None
        self.__class__.id_ += 1

    def include(self, name: str):
        self.next = Node(self, name)
        return self.next
    
    def __repr__(self):
        return f'{self.name}'

# >>> node = Node()
# >>> node.include('child').include('one').include('two')
# two_4
# >>> node.next
# child_2
# >>> node.next.next
# one_3
# >>> node.next.next.next
# two_4
# >>> node.next.next.next.parent
# one_3
# >>> node.next.next.next.parent.parent
# child_2
# >>> node.next.next.next.parent.parent.parent
# node_1
# >>> node.next.next.next.parent.parent.parent.parent