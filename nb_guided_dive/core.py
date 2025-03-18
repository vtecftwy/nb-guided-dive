"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs-dev/00_core.ipynb.

# %% auto 0
__all__ = ['imported_objects', 'mount_gdrive', 'config_fastai_for_colab']

# %% ../nbs-dev/00_core.ipynb 2
imported_objects  = ['np', 'pd','shutil', 'Path']
try:
    __all__.extend(imported_objects)
except:
    __all__ = imported_objects

# %% ../nbs-dev/00_core.ipynb 3
from nbdev import showdoc
import numpy as np
import pandas as pd
import shutil
from pathlib import Path

# %% ../nbs-dev/00_core.ipynb 4
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

# %% ../nbs-dev/00_core.ipynb 5
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
