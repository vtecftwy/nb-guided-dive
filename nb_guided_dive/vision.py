# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_vision.ipynb.

# %% auto 0
__all__ = ['imported_objects', 'mount_gdrive', 'config_fastai_for_colab', 'gv', 'ml_process', 'clean_image_directory',
           'count_files', 'print_metrics']

# %% ../01_vision.ipynb 3
imported_objects  = ['np', 'pd','shutil', 'Path', 'duckduckgo_search', 'display_image_cleaner']
try:
    __all__.extend(imported_objects)
except:
    __all__ = imported_objects

# %% ../01_vision.ipynb 4
import numpy as np
import pandas as pd
import graphviz
import matplotlib as mpl
import shutil
import torch
import warnings

from fastai.vision.all import set_seed
from jmd_imagescraper.core import duckduckgo_search
from jmd_imagescraper.imagecleaner import display_image_cleaner
from pathlib import Path
from PIL import Image

from pandas.api.types import CategoricalDtype
from scipy.cluster import hierarchy as hc

# %% ../01_vision.ipynb 5
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

# %% ../01_vision.ipynb 6
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

# %% ../01_vision.ipynb 7
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

# %% ../01_vision.ipynb 8
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
            if verbose: print('\n')

# %% ../01_vision.ipynb 9
def count_files(path):
    """Count the number if files in the folder pointed as path, and its subfolders"""
    if isinstance(path, str): path = Path(path)
    nb_img = len([f for f in path.iterdir() if f.is_file()])
    if nb_img > 0:
        print(f"{nb_img:,d} in folder {path.name}")
    for d in [d for d in path.iterdir() if d.is_dir()]:
        nb_img = len([f for f in d.iterdir() if f.is_file()])
        print(f"{nb_img:,d} in folder {d.name}")

# %% ../01_vision.ipynb 10
def print_metrics(cm):
    """Print FP, FN, Accuracy, Precision  and Recall"""
    nb_val_im = cm.sum()
    true_nb_im_per_class = cm.sum(axis=1)
    pred_nb_im_per_class = cm.sum(axis=0)

    print(f"Accurate predictions:               {cm[0,0] + cm[1,1]:3d} out of {nb_val_im:,d} validation images") 
    print(f"False Positive preds:               {cm[0,1]:3d} images classified as 'without_mask' but actually should be `with_mask`)")   
    print(f"False Negative preds:               {cm[1,0]:3d} images classified as `with_mask` but actually should be `without_mask`)")
    print()
    print(f"Accuracy:                           {cm.diagonal().sum()/nb_val_im * 100:6.2f} %") 
    print(f"Precision for 'without_mask' preds: {cm[1, 1]/pred_nb_im_per_class[1] * 100:6.2f} %")   
    print(f"Recall for 'without_mask' preds:    {cm[1,1]/true_nb_im_per_class[1] * 100:6.2f} %")
    
