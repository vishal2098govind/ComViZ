# from anytree import RenderTree, AnyNode
from anytree.exporter import UniqueDotExporter
from PIL import Image


def visualize_parse_tree(trace):

    if trace:
        # for pre, fill, node in RenderTree(trace[0]):
        #     print(f'{pre}{node.name}')

        UniqueDotExporter(trace[0]).to_picture("arith_pt.png")
        Image.open(rf'D:/GeeK/ComViz/arith_pt.png').show()
