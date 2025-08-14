from collections.abc import Callable

import numpy as np
import colour

from .utils import diff, interp


def extract_coordinates(cmap: Callable[[np.ndarray], np.ndarray], /, *, model: str = "OKLab", with_derivatives: bool = False) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    # assume cmap is a callable that is defined over a free parameter
    # q in [0, 1], and returns RGB values in the sRGB color space.
    q = np.linspace(0, 1, 10_000)  # 10k points for smoothness
    srgb = cmap(q)
    if srgb.shape[1] == 4:  # remove alpha channel if present
        srgb = srgb[:, :-1]

    # unfortunately, we have to deal with repeats
    # since these colormaps only return pixel-displayable colors
    # so having too smooth a free paramater will run into
    # discretization issues.
    # NOTE: this may affect the derivatives? investigate in the future
    d_srgb = np.linalg.norm(diff(srgb), axis=1)
    mask = ~np.isclose(d_srgb, 0)
    mask = np.concatenate([[True], mask])  # keep the first point
    q = q[mask]
    srgb = srgb[mask]

    # compute colour model transformation
    lab = colour.convert(srgb, source='sRGB', target=model)
    if not with_derivatives:
        return q, srgb, lab

    # compute derivatives
    d_q = diff(q)
    d_q = diff(q)
    d_lab = diff(lab) / np.column_stack([d_q, d_q, d_q])

    # interpolate original data
    q_interp = interp(q)
    srgb_interp = interp(srgb)
    return q, srgb, lab, q_interp, srgb_interp, d_lab
