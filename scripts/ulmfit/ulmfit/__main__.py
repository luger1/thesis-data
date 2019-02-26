from functools import wraps

import fire
from .pretrain_lm import LMHyperParams
from .train_clas import CLSHyperParams
from .train_lowshot import CLSHyperParams as LOWHyperParams

class FireView:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

class ULMFiT:
    @wraps(LMHyperParams)
    def lm(self, dataset_path,  **changes):
        changes['dataset_path'] = dataset_path
        params = LMHyperParams(**changes)
        return FireView(train=params.train_lm)

    lm2 = LMHyperParams
    @wraps(CLSHyperParams)
    def cls(self, dataset_path, base_lm_path, **changes):
        params = CLSHyperParams.from_lm(dataset_path, base_lm_path, **changes)
        return FireView(train=params.train_cls)

    lm2 = LMHyperParams
    @wraps(LOWHyperParams)
    def lowshot(self, dataset_path, base_lm_path, **changes):
        params = LOWHyperParams.from_lm(dataset_path, base_lm_path, **changes)
        return FireView(train=params.train_cls)

if __name__ == '__main__':
    fire.Fire(ULMFiT())
