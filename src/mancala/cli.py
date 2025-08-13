import numpy as np
import matplotlib.pyplot as plt
import typer
from typing_extensions import Annotated

from .ctransform import transformed, transformed_dv

app = typer.Typer()

@app.command()
def show(cmaps: list[str], space: Annotated[str, typer.Option(help="Colour space to use for plotting.")] = "OKLab"):
    fig, ax = plt.subplots(1, 1, figsize=(6, 6), subplot_kw={'projection': '3d'})

    ax.plot([0, 0], [0, 0], [0, 1], color='black')
    for cmap_name in cmaps:
        cmap = plt.get_cmap(cmap_name)
        q, srgb, osc = transformed(cmap, output_space=space)
        ax.scatter(osc[:, 1], osc[:, 2], osc[:, 0], color=srgb, label=cmap_name)

    ax.set_title(f"Colormaps in {space} space")
    ax.set_xlabel("a")
    ax.set_ylabel("b")
    ax.set_zlabel("L")
    ax.legend()

    plt.tight_layout()
    plt.show()

@app.command()
def lightness(cmaps: list[str], space: Annotated[str, typer.Option(help="Colour space to use for plotting.")] = "OKLab"):
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))

    for cmap_name in cmaps:
        cmap = plt.get_cmap(cmap_name)
        q, srgb, osc = transformed(cmap, output_space=space)
        ax.scatter(q, osc[:, 0], color=srgb, label=cmap_name)

    ax.set_title(f"Colormaps in {space} space")
    ax.set_xlabel("q")
    ax.set_ylabel("lightness")
    ax.legend()

    plt.tight_layout()
    plt.show()

@app.command()
def chroma(cmaps: list[str], space: Annotated[str, typer.Option(help="Colour space to use for plotting.")] = "OKLab"):
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))

    for cmap_name in cmaps:
        cmap = plt.get_cmap(cmap_name)
        q, srgb, osc = transformed(cmap, output_space=space)
        chroma = (osc[:, 1]**2 + osc[:, 2]**2)**0.5
        ax.scatter(q, chroma, color=srgb, label=cmap_name)

    ax.set_title(f"Colormaps in {space} space")
    ax.set_xlabel("q")
    ax.set_ylabel("chroma")
    ax.legend()

    plt.tight_layout()
    plt.show()

@app.command()
def hue(cmaps: list[str], space: Annotated[str, typer.Option(help="Colour space to use for plotting.")] = "OKLab"):
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))

    for cmap_name in cmaps:
        cmap = plt.get_cmap(cmap_name)
        q, srgb, osc = transformed(cmap, output_space=space)
        hue = np.atan2(osc[:, 2], osc[:, 1])
        ax.scatter(q, hue, color=srgb, label=cmap_name)

    ax.set_title(f"Colormaps in {space} space")
    ax.set_xlabel("q")
    ax.set_ylabel("hue (degrees)")
    ax.legend()

    plt.tight_layout()
    plt.show()

@app.command()
def dv(cmaps: list[str], space: Annotated[str, typer.Option(help="Colour space to use for plotting.")] = "OKLab"):
    fig, ax = plt.subplots(1, 1, figsize=(6, 6), subplot_kw={'projection': '3d'})

    ax.plot([0], [0], [0], 'k^')
    for cmap_name in cmaps:
        cmap = plt.get_cmap(cmap_name)
        q, srgb, osc = transformed_dv(cmap, output_space=space)
        ax.scatter(osc[:, 1], osc[:, 2], osc[:, 0], color=srgb, label=cmap_name)

    ax.set_title(f"Colormaps in {space} space")
    ax.set_xlabel("a")
    ax.set_ylabel("b")
    ax.set_zlabel("L")
    ax.legend()

    plt.tight_layout()
    plt.show()

@app.command()
def absdv(cmaps: list[str], space: Annotated[str, typer.Option(help="Colour space to use for plotting.")] = "OKLab"):
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))

    for cmap_name in cmaps:
        cmap = plt.get_cmap(cmap_name)
        q, srgb, osc = transformed_dv(cmap, output_space=space)
        ax.scatter(q, np.linalg.norm(osc, axis=1), color=srgb, label=cmap_name)

    ax.set_title(f"Colormaps in {space} space")
    ax.set_xlabel("q")
    ax.set_ylabel("|dv|")
    ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    app()