#!/usr/bin/env python3
"""Reusable matplotlib helpers for polished IEEE-style manuscript figures.

The module imports matplotlib lazily so the skill can be installed on machines
without plotting dependencies. Plotting functions raise a clear error when
matplotlib or numpy is missing.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


IEEE_ONE_COL_IN = 3.5
IEEE_TWO_COL_IN = 7.16

PALETTE = {
    "proposed": "#0B5CAD",
    "proposed_light": "#8EC3F5",
    "recent_baseline": "#0F766E",
    "traditional_baseline": "#B64040",
    "cost": "#B7791F",
    "neutral": "#6B7280",
    "neutral_light": "#AAB4C3",
    "grid": "#D7DEE8",
    "text": "#172033",
    "background": "#FFFFFF",
}

ROLE_STYLE = {
    "proposed": {"color": PALETTE["proposed"], "marker": "o", "linestyle": "-", "linewidth": 1.8},
    "recent": {"color": PALETTE["recent_baseline"], "marker": "s", "linestyle": "--", "linewidth": 1.6},
    "traditional": {"color": PALETTE["traditional_baseline"], "marker": "^", "linestyle": "-.", "linewidth": 1.6},
    "cost": {"color": PALETTE["cost"], "marker": "D", "linestyle": ":", "linewidth": 1.6},
    "neutral": {"color": PALETTE["neutral"], "marker": "v", "linestyle": (0, (2, 2)), "linewidth": 1.4},
}

HATCHES = ("", "//", "\\\\", "xx", "..", "--")
SUPPORTED_FORMATS = {"svg", "pdf", "eps", "png", "jpg", "jpeg", "tif", "tiff"}


@dataclass(frozen=True)
class IEEEFigureStyle:
    width: str = "one-column"
    font_size: float = 8.0
    axes_linewidth: float = 0.9
    tick_size: float | None = None
    legend_size: float | None = None
    use_tex: bool = False
    dpi: int = 600
    font_family: tuple[str, ...] = ("Arial", "Helvetica", "DejaVu Sans", "sans-serif")


def _require_plotting():
    try:
        import matplotlib as mpl

        mpl.use("Agg", force=True)
        import matplotlib.pyplot as plt
        import numpy as np
    except Exception as exc:  # pragma: no cover - environment dependent
        raise RuntimeError(
            "matplotlib and numpy are required for IEEE figure rendering. "
            "Install them or copy the style contract without running plots."
        ) from exc
    return mpl, plt, np


def figure_size(width: str = "one-column", aspect: float = 0.68, height: float | None = None) -> tuple[float, float]:
    if width in {"one", "one-column", "single"}:
        w = IEEE_ONE_COL_IN
    elif width in {"two", "two-column", "double"}:
        w = IEEE_TWO_COL_IN
    else:
        w = float(width)
    return (w, height if height is not None else w * aspect)


def apply_ieee_style(style: IEEEFigureStyle | None = None) -> IEEEFigureStyle:
    style = style or IEEEFigureStyle()
    mpl, _, _ = _require_plotting()
    tick_size = style.tick_size or max(style.font_size - 0.5, 6.5)
    legend_size = style.legend_size or style.font_size
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": list(style.font_family),
            "font.size": style.font_size,
            "axes.labelsize": style.font_size,
            "axes.titlesize": style.font_size + 0.5,
            "axes.linewidth": style.axes_linewidth,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.edgecolor": PALETTE["text"],
            "axes.labelcolor": PALETTE["text"],
            "xtick.labelsize": tick_size,
            "ytick.labelsize": tick_size,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "legend.fontsize": legend_size,
            "legend.frameon": False,
            "grid.color": PALETTE["grid"],
            "grid.linewidth": 0.55,
            "grid.alpha": 0.85,
            "figure.facecolor": PALETTE["background"],
            "axes.facecolor": PALETTE["background"],
            "savefig.facecolor": PALETTE["background"],
            "savefig.edgecolor": PALETTE["background"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "text.usetex": style.use_tex,
        }
    )
    return style


def create_figure(
    width: str = "one-column",
    aspect: float = 0.68,
    nrows: int = 1,
    ncols: int = 1,
    **kwargs,
):
    _, plt, _ = _require_plotting()
    figsize = kwargs.pop("figsize", figure_size(width, aspect))
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, constrained_layout=True, **kwargs)
    return fig, axes


def role_style(role: str | None, index: int = 0) -> dict:
    if role in ROLE_STYLE:
        return dict(ROLE_STYLE[role])
    roles = ("proposed", "recent", "traditional", "cost", "neutral")
    return dict(ROLE_STYLE[roles[index % len(roles)]])


def _role_at(roles: Sequence[str] | None, index: int, total: int) -> str | None:
    if roles is None:
        return None
    if len(roles) != total:
        raise ValueError("roles must match number of plotted series/items")
    return roles[index]


def _as_1d(values: Sequence[float], name: str):
    _, _, np = _require_plotting()
    arr = np.asarray(values, dtype=float)
    if arr.ndim != 1:
        raise ValueError(f"{name} must be 1D")
    return arr


def _normalise_series(series: Sequence[Sequence[float]], expected_len: int):
    _, _, np = _require_plotting()
    arr = np.asarray(series, dtype=float)
    if arr.ndim != 2:
        raise ValueError("series must be a 2D sequence: one row per method")
    if arr.shape[1] != expected_len:
        raise ValueError("each series row must match the number of categories")
    return arr


def add_panel_label(ax, label: str, x: float = -0.12, y: float = 1.05) -> None:
    ax.text(x, y, f"({label})", transform=ax.transAxes, fontweight="bold", va="bottom", ha="left")


def set_metric_axis(ax, xlabel: str | None = None, ylabel: str | None = None, grid_axis: str = "y") -> None:
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    ax.grid(True, axis=grid_axis, zorder=0)


def plot_grouped_bars(
    ax,
    categories: Sequence[str],
    series: Sequence[Sequence[float]],
    labels: Sequence[str],
    roles: Sequence[str] | None = None,
    ylabel: str | None = None,
    annotate: bool = False,
    start_at_zero: bool = True,
):
    _, _, np = _require_plotting()
    data = _normalise_series(series, len(categories))
    if len(labels) != data.shape[0]:
        raise ValueError("labels must match number of series")
    x = np.arange(len(categories))
    width = min(0.78 / data.shape[0], 0.24)
    containers = []
    for i, values in enumerate(data):
        style = role_style(_role_at(roles, i, data.shape[0]), i)
        offset = (i - (data.shape[0] - 1) / 2) * width
        bars = ax.bar(
            x + offset,
            values,
            width,
            label=labels[i],
            color=style["color"],
            edgecolor=PALETTE["text"],
            linewidth=0.55,
            hatch=HATCHES[i % len(HATCHES)],
            zorder=3,
        )
        containers.append(bars)
        if annotate:
            for bar in bars:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height(),
                    f"{bar.get_height():.2g}",
                    ha="center",
                    va="bottom",
                    fontsize=6.5,
                )
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    if ylabel:
        ax.set_ylabel(ylabel)
    if start_at_zero:
        ax.set_ylim(bottom=0)
    ax.grid(True, axis="y", zorder=0)
    return containers


def plot_trend(
    ax,
    x: Sequence[float],
    y_series: Sequence[Sequence[float]],
    labels: Sequence[str],
    roles: Sequence[str] | None = None,
    intervals: Sequence[Sequence[float]] | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    logy: bool = False,
):
    _, _, np = _require_plotting()
    x_arr = _as_1d(x, "x")
    data = _normalise_series(y_series, len(x_arr))
    if len(labels) != data.shape[0]:
        raise ValueError("labels must match number of series")
    interval_arr = None
    if intervals is not None:
        interval_arr = _normalise_series(intervals, len(x_arr))
        if interval_arr.shape != data.shape:
            raise ValueError("intervals must match y_series shape")
    for i, values in enumerate(data):
        style = role_style(_role_at(roles, i, data.shape[0]), i)
        ax.plot(
            x_arr,
            values,
            label=labels[i],
            color=style["color"],
            marker=style["marker"],
            linestyle=style["linestyle"],
            linewidth=style["linewidth"],
            markersize=4.2,
            zorder=3,
        )
        if interval_arr is not None:
            spread = interval_arr[i]
            ax.fill_between(x_arr, values - spread, values + spread, color=style["color"], alpha=0.12, linewidth=0)
    if logy:
        ax.set_yscale("log")
    set_metric_axis(ax, xlabel=xlabel, ylabel=ylabel)


def plot_pareto(
    ax,
    cost: Sequence[float],
    score: Sequence[float],
    labels: Sequence[str],
    roles: Sequence[str] | None = None,
    size: Sequence[float] | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
):
    _, _, np = _require_plotting()
    cost_arr = _as_1d(cost, "cost")
    score_arr = _as_1d(score, "score")
    if len(cost_arr) != len(score_arr) or len(labels) != len(cost_arr):
        raise ValueError("cost, score, and labels must have matching lengths")
    if size is None:
        size_arr = np.full_like(cost_arr, 42.0, dtype=float)
    else:
        size_arr = _as_1d(size, "size")
        if len(size_arr) != len(cost_arr):
            raise ValueError("size must match cost length")
        size_arr = 32 + 72 * (size_arr - size_arr.min()) / max(np.ptp(size_arr), 1e-9)
    for i, (cx, sy, label) in enumerate(zip(cost_arr, score_arr, labels)):
        style = role_style(_role_at(roles, i, len(labels)), i)
        ax.scatter(cx, sy, s=size_arr[i], color=style["color"], edgecolor=PALETTE["text"], linewidth=0.55, zorder=4)
        ax.annotate(label, (cx, sy), xytext=(4, 4), textcoords="offset points")
    set_metric_axis(ax, xlabel=xlabel, ylabel=ylabel, grid_axis="both")


def save_ieee_figure(
    fig,
    stem: str | Path,
    formats: Iterable[str] = ("svg", "pdf", "png", "tiff"),
    dpi: int = 600,
    pad_inches: float = 0.035,
) -> list[Path]:
    stem_path = Path(stem)
    stem_path.parent.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []
    for fmt in formats:
        clean = fmt.lower().lstrip(".")
        if clean not in SUPPORTED_FORMATS:
            raise ValueError(f"unsupported format: {fmt}")
        path = stem_path.with_suffix(f".{clean}")
        fig.savefig(path, dpi=dpi if clean in {"png", "jpg", "jpeg", "tif", "tiff"} else None, bbox_inches="tight", pad_inches=pad_inches)
        saved.append(path)
    return saved


def _self_test() -> int:
    assert abs(figure_size("one-column")[0] - IEEE_ONE_COL_IN) < 1e-9
    assert abs(figure_size("two-column")[0] - IEEE_TWO_COL_IN) < 1e-9
    assert "proposed" in PALETTE
    try:
        _, plt, _ = _require_plotting()
    except RuntimeError:
        print("Core style checks passed; matplotlib is not installed, so render test skipped.")
        return 0
    apply_ieee_style()
    fig, ax = create_figure()
    plot_trend(ax, [0, 1, 2], [[0.2, 0.4, 0.55], [0.25, 0.35, 0.5]], ["Ours", "Baseline"], roles=["proposed", "traditional"])
    ax.legend(loc="best")
    plt.close(fig)
    print("Core style checks and matplotlib render smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(_self_test())
