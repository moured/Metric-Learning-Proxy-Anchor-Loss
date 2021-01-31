from .cars import Cars
from .cub import CUBirds
from .SOP import SOP
from .import utils
from .base import BaseDataset

# ADDED DATASETS
from .caltech101 import Caltech101
from .caltech256 import Caltech256
from .caltechdog import Caltechdog

_type = {
    'cars': Cars,
    'cub': CUBirds,
    'SOP': SOP,
    'caltech101': Caltech101,
    'caltech256': Caltech256,
    'caltechdog': Caltechdog
}

def load(name, root, mode, transform = None):
    return _type[name](root = root, mode = mode, transform = transform)
    
