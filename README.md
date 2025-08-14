# mancala

A command-line tool for visualizing color maps in a uniform color space.

```
mancala viridis
```
![mancala example with viridis](https://i.imgur.com/uawQZGC.png)

By default, color maps are transformed into [Oklab](https://bottosson.github.io/posts/oklab/) space.
mancala uses [colour](https://www.colour-science.org/) to perform the color model transformations.
The CLI is constructed using the [Typer](https://typer.tiangolo.com/) library.

## Installation

Make sure to install this package with Python **3.11** or **3.12**.

### Using [`pipx`](https://pipx.pypa.io/latest/) (recommended for *CLI only*)

`pipx` installs the package into an isolated environment, only exposing the project scripts (if added to PATH).

```
pipx install git+https://github.com/ilikecubesnstuff/mancala
```

### Using `pip`

```
pip install git+https://github.com/ilikecubesnstuff/mancala
```

## CLI Usage

Depending on your installation method, you can use mancala by either doing `mancala` or `python -m mancala` on the command line.

The arguments are color map names as recognized by [Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html) (including those from [CMasher](https://cmasher.readthedocs.io/)).
To visualize a particular axis of lightness, chroma, or hue, the optional flags `-l`, `-c`, and `-h` can be used respectively. If none are provided, the default is to display a 3D plot with all three (`-lch`).
To use a different color model, the optional `--model` flag can be used to specify any of the color models available in the [colour](https://www.colour-science.org/) library.

```
mancala viridis -ch --model CAM16UCS
```
![mancala example with viridis](https://i.imgur.com/BJFhecR.png)

## Custom Color Maps

To plot a custom color map, the `mancala.visualize` module contains all the relevant plotting methods for any combination of lightness, chroma, and hue.

A color map is a function that takes one argument (a value between 0 and 1) and returns a corresponding RGB color. This output color is interpreted as belonging in the sRGB color space.

```py
import numpy as np

def custom_cmap(q):
    return np.array([q, q**2 * 2/3 + 1/6, abs(q - 0.5) + 1/3]).T
```

This color map can then be visualized with mancala:

```py
from mancala.visualize import plot_LCH
plot_LCH(custom_cmap)
```
![mancala example with custom color map](https://i.imgur.com/PsnwYOf.png)
