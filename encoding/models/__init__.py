from .model_zoo import get_model
from .model_store import get_model_file
from .base import *
from .fcn import *
from .psp import *
from .psp_att import *
from .encnet import *
from .deeplabv3 import *
from .deeplabv3plus import*
from .gsnet import *
from .gsnet_noatt import *

def get_segmentation_model(name, **kwargs):
    from .fcn import get_fcn
    models = {
        'fcn': get_fcn,
        'encnet': get_encnet,
        'deeplab': get_deeplab,
        'deeplabv3plus': get_deeplabv3plus,
        'deeplabv3': get_deeplabv3,
        'deeplabv3_att': get_deeplabv3_att,
        'psp': get_psp,
        'psp_att': get_psp_att,
        'gsnet': get_gsnet,
        'gsnet_noatt': get_gsnet_noatt,
    }
    return models[name.lower()](**kwargs)
