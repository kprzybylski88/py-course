class Node:
    parent = None
    children = []
    name = ''
    def __init__(self, parent, name) -> None:
        self.children = []
        self.parent = parent
        self.name = name
        
        if parent is not None:
            parent.addChild(self)

    def addChild(self, child):
        self.children.append(child)


root = Node(None, '0')
child1 = Node(root, '1')
child2 = Node(root, '2')
child21 = Node(child2, '2.1')
child22 = Node(child2, '2.2')
child23 = Node(child2, '2.3')
child11 = Node(child1, '1.1')
child12 = Node(child1, '1.2')
child13 = Node(child1, '1.3')
child131 = Node(child13, '1.3.1')
child132 = Node(child13, '1.3.2')


def travel(node: Node):
    print('nazwa:  ' + node.name)

    if len(node.children) > 0:
        print('Trawersowanie dzieci')
        for child in node.children:
            travel(child)
        print('koniec trawersowania: '+ node.name)
    


travel(root)

