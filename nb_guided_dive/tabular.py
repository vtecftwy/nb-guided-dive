# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs-dev/03_tabular.ipynb.

# %% auto 0
__all__ = ['imported_objects', 'mount_gdrive', 'config_fastai_for_colab', 'gv', 'ml_process', 'count_files']

# %% ../nbs-dev/03_tabular.ipynb 3
imported_objects  = ['np', 'pd','shutil', 'Path']
try:
    __all__.extend(imported_objects)
except:
    __all__ = imported_objects

# %% ../nbs-dev/03_tabular.ipynb 4
import numpy as np
import pandas as pd
import graphviz
import matplotlib as mpl
import shutil
import torch
import warnings

from pathlib import Path
from PIL import Image

from pandas.api.types import CategoricalDtype
from scipy.cluster import hierarchy as hc

# %% ../nbs-dev/03_tabular.ipynb 5
def mount_gdrive(path_to_ds=None):

    if path_to_ds is None:
        dataset = Path('/content/gdrive/MyDrive/img-ds.zip')
    else:
        dataset = Path(path_to_ds)

    try:
        from google.colab import drive
        drive.mount('/content/gdrive')
        if not dataset.is_file():
            raise ValueError(f"Dataset cannot be found at <{dataset.absolute()}> ")
    except:
        print('This notebook should be run on Google Colab')

# %% ../nbs-dev/03_tabular.ipynb 6
def config_fastai_for_colab(path_to_ds=None):
    
    warnings.filterwarnings('ignore')
    
    # matplotlib settings
    mpl.rcParams['savefig.dpi']= 200
    mpl.rcParams['font.size']=12
    
    # fastai seed
    set_seed(88)
    
    # pytorch settings
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.set_printoptions(linewidth=200)

    # numpy and pandas settings
    np.set_printoptions(linewidth=200)
    pd.set_option('display.max_columns',999)
    
    # mount goggle gdrive
    mount_gdrive(path_to_ds)

# %% ../nbs-dev/03_tabular.ipynb 7
def gv(code=None): 
    return graphviz.Source('digraph G{ rankdir="LR"' + code + '; }')

def ml_process():
    code = '''ordering=in
        problem[shape=cds width=1 height=1 label="1\nFrame business problem \ninto a ML problem"]
        data[shape=cylinder width=1 height=1 label="2\nCollect, and prepare \ndata, incl. labeling"]
        modeling[shape=box3d width=1 height=1 label="3\nBuild model \nand train it"]
        evaluate[shape=component width=1 height=1 label="4\nEvaluate and \nvalidate model"]
        improve[shape=rarrow width=1 height=1 label="5\nImprove model to \nreach expected standard"]
        problem->data->modeling->evaluate->improve'''
    return gv(code)

# %% ../nbs-dev/03_tabular.ipynb 8
def count_files(path):
    """Count the number if files in the folder pointed as path, and its subfolders"""
    if isinstance(path, str): path = Path(path)
    nb_img = len([f for f in path.iterdir() if f.is_file()])
    if nb_img > 0:
        print(f"{nb_img:,d} in folder {path.name}")
    for d in [d for d in path.iterdir() if d.is_dir()]:
        nb_img = len([f for f in d.iterdir() if f.is_file()])
        print(f"{nb_img:,d} in folder {d.name}")
