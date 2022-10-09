# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_imports.ipynb.

# %% auto 0
__all__ = ['config_fastai_for_colab', 'mount_gdrive', 'gv', 'clean_image_directory']

# %% ../01_imports.ipynb 3
__all__ = ['np', 'pd','shutil', 
           'Path', 
           'duckduckgo_search', 'display_image_cleaner', 'clean_image_directory', 'gv', 'config_fastai_for_colab'
          ]

# %% ../01_imports.ipynb 4
import numpy as np
import pandas as pd
import graphviz
import matplotlib as mpl
import shutil
import torch

from fastai.vision.all import set_seed
from jmd_imagescraper.core import duckduckgo_search
from jmd_imagescraper.imagecleaner import display_image_cleaner
from pathlib import Path
from PIL import Image

from pandas.api.types import CategoricalDtype
from scipy.cluster import hierarchy as hc

# %% ../01_imports.ipynb 5
def config_fastai_for_colab():
    mpl.rcParams['savefig.dpi']= 200
    mpl.rcParams['font.size']=12

    set_seed(88)

    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.set_printoptions(linewidth=200)

    np.set_printoptions(linewidth=200)
    pd.set_option('display.max_columns',999)

# %% ../01_imports.ipynb 6
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

# %% ../01_imports.ipynb 7
def gv(code=None): 
    if code is None:
        code = '''ordering=in
            problem[shape=cds width=1 height=1 label="1\nFrame business problem \ninto a ML problem"]
            data[shape=cylinder width=1 height=1 label="2\nCollect, and prepare \ndata, incl. labeling"]
            modeling[shape=box3d width=1 height=1 label="3\nBuild model \nand train it"]
            evaluate[shape=component width=1 height=1 label="4\nEvaluate and \nvalidate model"]
            improve[shape=rarrow width=1 height=1 label="5\nImprove model to \nreach expected standard"]
            problem->data->modeling->evaluate->improve'''
        
        return graphviz.Source('digraph G{ rankdir="LR"' + code + '; }')

# %% ../01_imports.ipynb 8
def clean_image_directory(path, verbose=False):
    def check_img(img):
        try: _ = Image.open(img)
        except Exception as e:
            img = str(img).replace(" ","\ ")
            os.system(f"rm -f {img}");
            print(f"removing error img:{img}")

    for cls in path.iterdir():
        for i, img in enumerate(cls.iterdir()):
            if verbose: print(i, end=' - ')
            check_img(img)
            print('\n')
