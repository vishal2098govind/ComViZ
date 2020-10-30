from anytree import AnyNode
from anytree.exporter import UniqueDotExporter
from PIL import Image


trace = []


def pre_order(node, parent=None):
    if node:
        if type(node).__name__ == 'BinaryOperationNode':
            root = AnyNode(name=node.op_token.value, parent=parent)

            trace.append(root)
            visualize_ast(trace[0])

            pre_order(node=node.left_node, parent=root)

            pre_order(node=node.right_node, parent=root)
        else:
            if type(node).__name__ == 'UnaryOperationNode':
                root = AnyNode(name=node, parent=parent)
                trace.append(root)
                visualize_ast(trace[0])
                pre_order(node.right_node, parent=root)
            elif type(node).__name__ in ['NumberNode', 'Token', 'VariableAccessNode']:
                trace.append(AnyNode(name=node, parent=parent))
                visualize_ast(trace[0])
            elif type(node).__name__ == 'VariableAssignNode':
                root = AnyNode(name=node.op_token, parent=parent)

                trace.append(root)

                pre_order(node=node.var_name_token, parent=root)
                pre_order(node=node.var_value_node, parent=root)


def visualize_ast(node=None):
    if node:
        pre_order(node)

        global trace

        # for pre, fill, node in RenderTree(trace[0]):
        #     print(f'{pre}{node.name}')
        UniqueDotExporter(trace[0]).to_picture("arith_ast.png")
        # re_trace = trace
        # trace = []
        Image.open(rf'D:/GeeK/ComViz/arith_ast.png').show()
        return trace
