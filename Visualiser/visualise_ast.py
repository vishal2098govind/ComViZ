from anytree import AnyNode, RenderTree
from anytree.exporter import UniqueDotExporter
from PIL import Image
trace = []


def pre_order(node, parent=None):
    if node:
        if type(node).__name__ == 'BinaryOperationNode':
            root = AnyNode(name=node, parent=parent)

            trace.append(root)
            visualize_ast(trace[0])

            pre_order(node.left_node, parent=root)

            pre_order(node.right_node, parent=root)
        else:
            if type(node).__name__ == 'UnaryOperationNode':
                root = AnyNode(name=node, parent=parent)
                trace.append(root)
                visualize_ast(trace[0])
                pre_order(node.right_node, parent=root)
            elif type(node).__name__ == 'NumberNode':
                trace.append(AnyNode(name=node, parent=parent))
                visualize_ast(trace[0])


def visualize_ast(node):
    pre_order(node)

    global trace

    for pre, fill, node in RenderTree(trace[0]):
        print(f'{pre}{node.name}')

    UniqueDotExporter(trace[0]).to_picture("arith_ast.png")
    Image.open(rf'D:/GeeK/ComViz/arith_ast.png').show()
