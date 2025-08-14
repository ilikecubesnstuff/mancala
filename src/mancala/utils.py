from collections.abc import Callable

import numpy as np
import matplotlib.pyplot as plt


diff = lambda x: x[1:] - x[:-1]
interp = lambda x: (x[1:] + x[:-1]) / 2


def get_cmaps(*names: str) -> list[Callable[[np.ndarray], np.ndarray]]:
    cmaps = []
    for name in names:
        if name.startswith("cmr."):
            import cmasher
        cmap = plt.get_cmap(name)
        cmaps.append(cmap)
    return cmaps
