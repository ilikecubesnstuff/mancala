import numpy as np
import colour

def transformed(cmap, output_space='OKLab', q=np.linspace(0, 1, 10000)):
    srgb = cmap(q)
    if srgb.shape[1] == 4:
        srgb = srgb[:, :-1]

    # unfortunately, we have to deal with repeats
    # since these colormaps only return pixel-displayable colors
    # so having too smooth a free paramater will run into
    # discretization issues.
    # NOTE: this may affect the derivatives? investigate in the future
    d_srgb = np.linalg.norm(srgb[1:] - srgb[:-1], axis=1)
    zeros = np.array([True, *np.isclose(d_srgb, 0)])
    q = q[~zeros]
    srgb = srgb[~zeros]

    osc = colour.convert(srgb, source='sRGB', target=output_space)
    return q, srgb, osc

def transformed_dv(cmap, output_space="OKLab"):
    q, srgb, osc = transformed(cmap, output_space=output_space)

    # compute derivatives
    dq = q[1:] - q[:-1]
    dv = (osc[1:] - osc[:-1]) / np.column_stack([dq, dq, dq])
    q_interp = (q[1:] + q[:-1]) / 2
    srgb_interp = (srgb[1:] + srgb[:-1]) / 2

    return q_interp, srgb_interp, dv
