# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_imports.ipynb.

# %% auto 0
__all__ = ['top_level', 'gv']

# %% ../01_imports.ipynb 3
print('start imports')

__all__ = ['np', 'pd','shutil', 'Path', 'duckduckgo_search', 'display_image_cleaner']

# %% ../01_imports.ipynb 4
import numpy as np
import pandas as pd
import graphviz
import matplotlib as mpl
import shutil

from google.colab import drive
from jmd_imagescraper.core import duckduckgo_search
from jmd_imagescraper.imagecleaner import display_image_cleaner
from pathlib import Path

# from pandas.api.types import CategoricalDtype
# from scipy.cluster import hierarchy as hc

# %% ../01_imports.ipynb 5
mpl.rcParams['savefig.dpi']= 200
mpl.rcParams['font.size']=12

set_seed(88)

torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
torch.set_printoptions(linewidth=200)

np.set_printoptions(linewidth=200)
pd.set_option('display.max_columns',999)



print('import and configurations finished')

# %% ../01_imports.ipynb 7
def gv(s): 
    return graphviz.Source('digraph G{ rankdir="LR"' + s + '; }')

# Prepare diagram 'Top Level'
top_level = '''ordering=in
            problem[shape=cds width=1 height=1 label="1\nFrame business problem \ninto a ML problem"]
            data[shape=cylinder width=1 height=1 label="2\nCollect, and prepare \ndata, incl. labeling"]
            modeling[shape=box3d width=1 height=1 label="3\nBuild model \nand train it"]
            evaluate[shape=component width=1 height=1 label="4\nEvaluate and \nvalidate model"]
            improve[shape=rarrow width=1 height=1 label="5\nImprove model to \nreach expected standard"]
            problem->data->modeling->evaluate->improve'''
