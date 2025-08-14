import numpy as np
import matplotlib.pyplot as plt
import typer
from typing_extensions import Annotated

from .utils import get_cmaps
from .visualize import plot_LCH, plot_CH, plot_LC, plot_LH, plot_L, plot_C, plot_H

app = typer.Typer()


@app.command()
def show(cmap_names: list[str],
        lightness: Annotated[bool, typer.Option("-l", help="Plot lightness.")] = False,
        chroma: Annotated[bool, typer.Option("-c", help="Plot chroma.")] = False,
        hue: Annotated[bool, typer.Option("-h", help="Plot hue.")] = False,
        model: Annotated[str, typer.Option(help="Colour model to use for plotting.")] = "OKLab"):
    cmaps = get_cmaps(*cmap_names)

    flags = [lightness, chroma, hue]

    if sum(flags) == 3:
        plot_LCH(*cmaps, model=model)
    elif sum(flags) == 2:
        if lightness and chroma:
            plot_LC(*cmaps, model=model)
        elif lightness and hue:
            plot_LH(*cmaps, model=model)
        elif chroma and hue:
            plot_CH(*cmaps, model=model)
    elif sum(flags) == 1:
        if lightness:
            plot_L(*cmaps, model=model)
        elif chroma:
            plot_C(*cmaps, model=model)
        elif hue:
            plot_H(*cmaps, model=model)
    else:
        plot_LCH(*cmaps, model=model)


if __name__ == "__main__":
    app()