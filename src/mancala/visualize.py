from collections.abc import Callable, Sequence

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from .ctransform import extract_coordinates
from .utils import diff


def plot_LCH(*cmaps: Callable[[np.ndarray], np.ndarray], model: str = "OKLab"):
    fig = plt.figure(figsize=(10, 6))
    ax_func = fig.add_subplot(121, projection='3d')
    ax_dv = fig.add_subplot(122, projection='3d')

    ax_func.plot([0, 0], [0, 0], [0, 1], 'k-')  # add zero-chroma reference line
    ax_dv.plot([0], [0], [0], 'k^')  # add zero-dv reference point

    for cmap in cmaps:
        q, c, lab, q_dv, c_dv, lab_dv = extract_coordinates(cmap, model=model, with_derivatives=True)

        l, a, b = lab.T
        ax_func.scatter(a, b, l, c=c)

        dl, da, db = lab_dv.T
        s = np.linalg.norm(c_dv, axis=1)
        s = 20 * s / np.median(s)
        ax_dv.scatter(da, db, dl, c=c_dv, s=s)

    ax_func.set_title(f"Colors in {model}")
    ax_func.set_xlabel("a")
    ax_func.set_ylabel("b")
    ax_func.set_zlabel("Lightness")

    ax_dv.set_title(f"Derivatives in {model}")
    ax_dv.set_xlabel("a")
    ax_dv.set_ylabel("b")
    ax_dv.set_zlabel("Lightness")

    plt.tight_layout()
    plt.show()


def plot_CH(*cmaps: Callable[[np.ndarray], np.ndarray], model: str = "OKLab"):
    fig = plt.figure(figsize=(10, 6))
    ax_func = fig.add_subplot(121, projection='polar')
    ax_dv = fig.add_subplot(122, projection='polar')

    ax_func.scatter([0], [0], c='black', marker='^')
    ax_dv.scatter([0], [0], c='black', marker='^')

    for cmap in cmaps:
        q, c, lab, q_dv, c_dv, lab_dv = extract_coordinates(cmap, model=model, with_derivatives=True)

        l, a, b = lab.T
        chr = np.sqrt(a**2 + b**2)
        hue = np.arctan2(b, a)
        ax_func.scatter(hue, chr, c=c)

        dl, da, db = lab_dv.T
        d_chr = np.sqrt(da**2 + db**2)
        d_hue = np.arctan2(db, da)
        s = np.linalg.norm(c_dv, axis=1)
        s = 20 * s / np.median(s)
        ax_dv.scatter(d_hue, d_chr, c=c_dv, s=s)

    ax_func.set_title(f"Colors in {model}")
    ax_func.set_xlabel("Hue")
    ax_func.set_ylabel("Chroma")

    ax_dv.set_title(f"Derivatives in {model}")
    ax_dv.set_xlabel("Hue")
    ax_dv.set_ylabel("Chroma")

    plt.tight_layout()
    plt.show()


def plot_LC(*cmaps: Callable[[np.ndarray], np.ndarray], model: str = "OKLab"):
    fig = plt.figure(figsize=(10, 6))
    ax_func = fig.add_subplot(121)
    ax_dv = fig.add_subplot(122)

    ax_func.scatter([0], [0], c='black', marker='^')
    ax_dv.scatter([0], [0], c='black', marker='^')

    for cmap in cmaps:
        q, c, lab, q_dv, c_dv, lab_dv = extract_coordinates(cmap, model=model, with_derivatives=True)

        l, a, b = lab.T
        chr = np.sqrt(a**2 + b**2)
        ax_func.scatter(chr, l, color=c)

        l_dv = lab_dv[:, 0]
        chr_dv = diff(chr) / diff(q)
        s = np.linalg.norm(c_dv, axis=1)
        s = 20 * s / np.median(s)
        ax_dv.scatter(chr_dv, l_dv, color=c_dv, s=s)

    ax_func.set_title(f"Colors in {model}")
    ax_func.set_xlabel("Chroma")
    ax_func.set_ylabel("Lightness")

    ax_dv.set_title(f"Derivatives in {model}")
    ax_dv.set_xlabel("Chroma")
    ax_dv.set_ylabel("Lightness")

    plt.tight_layout()
    plt.show()


def plot_LH(*cmaps: Callable[[np.ndarray], np.ndarray], model: str = "OKLab"):
    fig = plt.figure(figsize=(10, 6))
    ax_func = fig.add_subplot(121)
    ax_dv = fig.add_subplot(122)

    ax_func.scatter([0], [0], c='black', marker='^')
    ax_dv.scatter([0], [0], c='black', marker='^')

    for cmap in cmaps:
        q, c, lab, q_dv, c_dv, lab_dv = extract_coordinates(cmap, model=model, with_derivatives=True)

        l, a, b = lab.T
        hue = np.arctan2(b, a)
        ax_func.scatter(hue, l, color=c)

        l_dv = lab_dv[:, 0]
        hue_dv = diff(hue) / diff(q)
        s = np.linalg.norm(c_dv, axis=1)
        s = 20 * s / np.median(s)
        ax_dv.scatter(hue_dv, l_dv, color=c_dv, s=s)

    ax_func.set_title(f"Colors in {model}")
    ax_func.set_xlabel("Hue")
    ax_func.set_ylabel("Lightness")

    ax_dv.set_title(f"Derivatives in {model}")
    ax_dv.set_xlabel("Hue")
    ax_dv.set_ylabel("Lightness")

    plt.tight_layout()
    plt.show()


def plot_L(*cmaps: Callable[[np.ndarray], np.ndarray], model: str = "OKLab"):
    fig = plt.figure(figsize=(10, 6))
    ax_func = fig.add_subplot(121)
    ax_dv = fig.add_subplot(122)

    for cmap in cmaps:
        q, c, lab, q_dv, c_dv, lab_dv = extract_coordinates(cmap, model=model, with_derivatives=True)

        l, a, b = lab.T
        ax_func.scatter(q, l, color=c)

        l_dv = lab_dv[:, 0]
        s = np.linalg.norm(c_dv, axis=1)
        s = 20 * s / np.median(s)
        ax_dv.scatter(q_dv, l_dv, color=c_dv, s=s)

    ax_func.set_title(f"Colors in {model}")
    ax_func.set_xlabel("q")
    ax_func.set_ylabel("Lightness")

    ax_dv.set_title(f"Derivatives in {model}")
    ax_dv.set_xlabel("q")
    ax_dv.set_ylabel("Lightness")

    plt.tight_layout()
    plt.show()


def plot_C(*cmaps: Callable[[np.ndarray], np.ndarray], model: str = "OKLab"):
    fig = plt.figure(figsize=(10, 6))
    ax_func = fig.add_subplot(121)
    ax_dv = fig.add_subplot(122)

    for cmap in cmaps:
        q, c, lab, q_dv, c_dv, lab_dv = extract_coordinates(cmap, model=model, with_derivatives=True)

        l, a, b = lab.T
        chr = np.sqrt(a**2 + b**2)
        ax_func.scatter(q, chr, color=c)

        chr_dv = diff(chr) / diff(q)
        s = np.linalg.norm(c_dv, axis=1)
        s = 20 * s / np.median(s)
        ax_dv.scatter(q_dv, chr_dv, color=c_dv, s=s)

    ax_func.set_title(f"Colors in {model}")
    ax_func.set_xlabel("q")
    ax_func.set_ylabel("Chroma")

    ax_dv.set_title(f"Derivatives in {model}")
    ax_dv.set_xlabel("q")
    ax_dv.set_ylabel("Chroma")

    plt.tight_layout()
    plt.show()


def plot_H(*cmaps: Callable[[np.ndarray], np.ndarray], model: str = "OKLab"):
    fig = plt.figure(figsize=(10, 6))
    ax_func = fig.add_subplot(121)
    ax_dv = fig.add_subplot(122)

    for cmap in cmaps:
        q, c, lab, q_dv, c_dv, lab_dv = extract_coordinates(cmap, model=model, with_derivatives=True)

        l, a, b = lab.T
        hue = np.arctan2(b, a)
        ax_func.scatter(q, hue, color=c)

        hue_dv = diff(hue) / diff(q)
        s = np.linalg.norm(c_dv, axis=1)
        s = 20 * s / np.median(s)
        ax_dv.scatter(q_dv, hue_dv, color=c_dv, s=s)

    ax_func.set_title(f"Colors in {model}")
    ax_func.set_xlabel("q")
    ax_func.set_ylabel("Hue")

    ax_dv.set_title(f"Derivatives in {model}")
    ax_dv.set_xlabel("q")
    ax_dv.set_ylabel("Hue")

    plt.tight_layout()
    plt.show()
