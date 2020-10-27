from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from PIL import Image
trace = []


def pre_order(node, parent=None):
    if node:
        if type(node).__name__ == 'BinaryOperationNode':
            root = Node(node.op_token, parent=parent)

            trace.append(root)

            pre_order(node.left_node, parent=root)

            pre_order(node.right_node, parent=root)
        else:
            if type(node).__name__ == 'UnaryOperationNode':
                root = Node(node.op_token, parent=parent)
                trace.append(root)
                pre_order(node.right_node, parent=root)
            elif type(node).__name__ == 'NumberNode':
                trace.append(Node(name=node.num_token.value, parent=parent))


def visualize(node):
    pre_order(node)

    global trace

    for pre, fill, node in RenderTree(trace[0]):
        print(f'{pre}{node.name}')

    DotExporter(trace[0]).to_picture("arith_ast.png")
    Image.open(r'D:/GeeK/ComViz/arith_ast.png').show()

    trace = []

