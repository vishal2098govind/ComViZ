import pandas as pd
import dataframe_image as dfi
# from PIL import Image


def visualise_st(context):
    visual_st = pd.DataFrame.from_dict(context.symbol_table.symbols_map)

    dfi.export(visual_st, 'symbol_table.png')
    # Image.open('D:/GeeK/ComViz/symbol_table.png').show()
