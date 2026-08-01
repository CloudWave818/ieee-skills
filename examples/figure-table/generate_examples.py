#!/usr/bin/env python3
"""Generate polished, zero-dependency IEEE figure/table example SVGs.

The examples are synthetic. They demonstrate IEEE figure contracts and visual
style, not real experimental results.
"""

from __future__ import annotations

import csv
import html
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FIGURES = ROOT / "figures"

BLUE = "#0B5CAD"
BLUE_2 = "#2F80C8"
BLUE_LIGHT = "#EAF4FF"
TEAL = "#0F766E"
TEAL_2 = "#59B3A9"
RED = "#B64040"
GOLD = "#B7791F"
DARK = "#172033"
GRAY = "#5F6B7A"
GRAY_2 = "#9AA6B5"
GRID = "#D8E0EA"
PANEL = "#F7FAFD"
PANEL_2 = "#F1F6FB"
LINE = "#D5DEE9"
WHITE = "#FFFFFF"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def text_width(value: object, size: float = 13.0, weight: str = "400") -> float:
    factor = 0.58 if weight == "400" else 0.62
    return len(str(value)) * size * factor


def text(
    x: float,
    y: float,
    value: object,
    cls: str = "",
    anchor: str = "start",
    fill: str | None = None,
    weight: str | None = None,
    size: float | None = None,
) -> str:
    attrs = [f'x="{x:.1f}"', f'y="{y:.1f}"', f'text-anchor="{anchor}"']
    if cls:
        attrs.append(f'class="{cls}"')
    if fill:
        attrs.append(f'fill="{fill}"')
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if size:
        attrs.append(f'font-size="{size:.1f}"')
    return f'  <text {" ".join(attrs)}>{esc(value)}</text>'


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str = "none", rx: float = 0, opacity: float = 1.0) -> str:
    return (
        f'  <rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{rx:.1f}" fill="{fill}" stroke="{stroke}" opacity="{opacity:.3f}"/>'
    )


def line(x1: float, y1: float, x2: float, y2: float, stroke: str = DARK, width: float = 1.2, dash: str = "") -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{width:.2f}"{dash_attr}/>'


def marker(x: float, y: float, color: str, shape: str, r: float = 5.0) -> str:
    if shape == "circle":
        return f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" stroke="{WHITE}" stroke-width="1.4"/>'
    if shape == "square":
        return f'  <rect x="{x-r:.1f}" y="{y-r:.1f}" width="{2*r:.1f}" height="{2*r:.1f}" fill="{color}" stroke="{WHITE}" stroke-width="1.4"/>'
    if shape == "diamond":
        return f'  <path d="M{x:.1f},{y-r-1:.1f} L{x+r+1:.1f},{y:.1f} L{x:.1f},{y+r+1:.1f} L{x-r-1:.1f},{y:.1f} Z" fill="{color}" stroke="{WHITE}" stroke-width="1.4"/>'
    return f'  <path d="M{x:.1f},{y-r-1:.1f} L{x+r:.1f},{y+r:.1f} L{x-r:.1f},{y+r:.1f} Z" fill="{color}" stroke="{WHITE}" stroke-width="1.4"/>'


def pill(x: float, y: float, value: str, color: str, fill: str = WHITE) -> str:
    w = max(76, text_width(value, 12, "700") + 24)
    return "\n".join(
        [
            rect(x, y, w, 28, fill, color, rx=14),
            text(x + w / 2, y + 18, value, "pill", "middle", color, "700"),
        ]
    )


def svg_wrap(width: int, height: int, title: str, subtitle: str, tags: list[tuple[str, str]], body: str) -> str:
    tag_svg = []
    cursor = width - 58
    for label, color in reversed(tags):
        w = max(76, text_width(label, 12, "700") + 24)
        cursor -= w
        tag_svg.append(pill(cursor, 35, label, color))
        cursor -= 10
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">
  <rect width="{width}" height="{height}" fill="{WHITE}"/>
  <style>
    text {{ font-family: Arial, Helvetica, sans-serif; fill: {DARK}; }}
    .title {{ font-size: 25px; font-weight: 700; }}
    .subtitle {{ font-size: 14px; fill: {GRAY}; }}
    .axislabel {{ font-size: 14px; font-weight: 700; }}
    .tick {{ font-size: 12px; fill: {GRAY}; }}
    .tiny {{ font-size: 11px; fill: {GRAY}; }}
    .small {{ font-size: 12px; fill: {GRAY}; }}
    .legend {{ font-size: 13px; fill: {DARK}; }}
    .paneltitle {{ font-size: 15px; font-weight: 700; }}
    .method {{ font-size: 13px; font-weight: 700; }}
    .metric {{ font-size: 24px; font-weight: 700; }}
    .pill {{ font-size: 12px; }}
    .header {{ font-size: 13px; font-weight: 700; fill: {WHITE}; }}
    .cell {{ font-size: 13px; }}
  </style>
  <text x="56" y="43" class="title">{esc(title)}</text>
  <text x="56" y="68" class="subtitle">{esc(subtitle)}</text>
{chr(10).join(tag_svg)}
{body}
</svg>
"""


def legend_line(x: float, y: float, name: str, color: str, shape: str, dash: str = "") -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return "\n".join(
        [
            f'  <line x1="{x:.1f}" y1="{y:.1f}" x2="{x+36:.1f}" y2="{y:.1f}" stroke="{color}" stroke-width="2.7"{dash_attr}/>',
            marker(x + 18, y, color, shape, 4.4),
            text(x + 48, y + 4, name, "legend"),
        ]
    )


def robustness_snr_curve() -> None:
    rows = [
        {"snr_db": -10, "MMSE": 0.180, "CNN": 0.145, "Transformer": 0.116, "Ours": 0.071},
        {"snr_db": -5, "MMSE": 0.112, "CNN": 0.082, "Transformer": 0.060, "Ours": 0.031},
        {"snr_db": 0, "MMSE": 0.064, "CNN": 0.039, "Transformer": 0.026, "Ours": 0.012},
        {"snr_db": 5, "MMSE": 0.031, "CNN": 0.017, "Transformer": 0.010, "Ours": 0.0047},
        {"snr_db": 10, "MMSE": 0.014, "CNN": 0.0069, "Transformer": 0.0038, "Ours": 0.0015},
        {"snr_db": 15, "MMSE": 0.0062, "CNN": 0.0028, "Transformer": 0.0014, "Ours": 0.00053},
        {"snr_db": 20, "MMSE": 0.0029, "CNN": 0.0011, "Transformer": 0.00048, "Ours": 0.00019},
    ]
    write_csv(DATA / "robustness-snr-curve.csv", rows)

    width, height = 1280, 720
    left, right, top, bottom = 104, 856, 132, 570
    side_x, side_w = 910, 300
    x_min, x_max = -10, 20
    y_min, y_max = 1e-4, 2.2e-1

    def xmap(x: float) -> float:
        return left + (x - x_min) / (x_max - x_min) * (right - left)

    def ymap(y: float) -> float:
        lo, hi = math.log10(y_min), math.log10(y_max)
        return bottom - (math.log10(y) - lo) / (hi - lo) * (bottom - top)

    methods = [
        ("Ours", BLUE, "circle", ""),
        ("Transformer", TEAL, "diamond", "2,4"),
        ("CNN", RED, "square", "7,4"),
        ("MMSE", GRAY, "triangle", "3,4"),
    ]

    body: list[str] = [
        rect(52, 96, 1176, 574, PANEL, "none", 18),
        rect(left, top, right - left, bottom - top, WHITE, LINE),
        rect(xmap(-10), top, xmap(0) - xmap(-10), bottom - top, BLUE_LIGHT, "none", opacity=0.72),
        text(xmap(-5), top + 24, "low-SNR stress", "tiny", "middle", GRAY),
    ]

    for tick_value in [-10, -5, 0, 5, 10, 15, 20]:
        x = xmap(tick_value)
        body.append(line(x, top, x, bottom, GRID, 1.0))
        body.append(line(x, bottom, x, bottom + 6, DARK, 1.2))
        body.append(text(x, bottom + 25, tick_value, "tick", "middle"))
    for tick_value, label in [(1e-1, "10^-1"), (1e-2, "10^-2"), (1e-3, "10^-3"), (1e-4, "10^-4")]:
        y = ymap(tick_value)
        body.append(line(left, y, right, y, GRID, 1.0))
        body.append(line(left - 6, y, left, y, DARK, 1.2))
        body.append(text(left - 14, y + 4, label, "tick", "end"))

    body.append(line(left, bottom, right, bottom, DARK, 1.35))
    body.append(line(left, top, left, bottom, DARK, 1.35))

    for name, color, shape, dash in reversed(methods):
        points = [(xmap(r["snr_db"]), ymap(r[name])) for r in rows]
        path = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        stroke_w = 3.3 if name == "Ours" else 2.35
        opacity = 1.0 if name == "Ours" else 0.88
        body.append(f'  <polyline points="{path}" fill="none" stroke="{color}" stroke-width="{stroke_w:.1f}" opacity="{opacity:.2f}"{dash_attr}/>')
        for x, y in points:
            body.append(marker(x, y, color, shape, 5.2 if name == "Ours" else 4.7))

    body.append(text(right - 6, ymap(rows[-1]["Ours"]) - 15, "Ours", "method", "end", BLUE, "700"))
    body.append(text((left + right) / 2, 624, "SNR (dB)", "axislabel", "middle"))
    body.append(
        f'  <text x="28.0" y="{(top+bottom)/2:.1f}" transform="rotate(-90 28.0 {(top+bottom)/2:.1f})" text-anchor="middle" class="axislabel">'
        "Bit error rate, BER (log scale; lower is better)</text>"
    )

    body.extend(
        [
            rect(side_x, top, side_w, 438, WHITE, LINE, 14),
            text(side_x + 24, top + 34, "Evidence map", "paneltitle"),
            text(side_x + 24, top + 58, "same channel, same metric", "small"),
            line(side_x + 24, top + 78, side_x + side_w - 24, top + 78, LINE, 1.0),
        ]
    )
    for i, item in enumerate(methods):
        body.append(legend_line(side_x + 28, top + 114 + i * 36, *item))

    summary = sorted([(name, next(r[name] for r in rows if r["snr_db"] == -5), color) for name, color, _, _ in methods], key=lambda x: x[1])
    bar_x, bar_y, bar_w = side_x + 112, top + 290, 142
    body.append(text(side_x + 24, top + 260, "BER @ -5 dB", "method"))
    body.append(text(side_x + 24, top + 281, "shorter is better", "small"))
    max_ber = max(v for _, v, _ in summary)
    for i, (name, value, color) in enumerate(summary):
        y = bar_y + i * 28
        body.append(text(side_x + 24, y + 16, name, "small"))
        body.append(rect(bar_x, y, bar_w, 14, "#E8EEF5", "none", 5))
        body.append(rect(bar_x, y, bar_w * value / max_ber, 14, color, "none", 5, 0.85))
        body.append(text(bar_x + bar_w + 10, y + 13, f"{value:.3f}", "tiny"))

    body.append(text(side_x + 24, top + 418, "Reviewer cue", "method", fill=BLUE))
    body.append(text(side_x + 24, top + 441, "stress condition is visible;", "small"))
    body.append(text(side_x + 24, top + 461, "baselines remain readable.", "small"))

    svg = svg_wrap(
        width,
        height,
        "Robustness evidence under low-SNR conditions",
        "Synthetic demo. Stress condition, baseline fairness, and method separation are visible in one view.",
        [("two-column", BLUE), ("log metric", TEAL)],
        "\n".join(body),
    )
    (FIGURES / "robustness-snr-curve.svg").write_text(svg, encoding="utf-8")


def accuracy_latency_pareto() -> None:
    rows = [
        {"method": "TinyCNN", "latency_ms": 5.4, "f1": 0.812, "params_m": 0.48, "role": "traditional"},
        {"method": "MobileNet", "latency_ms": 8.8, "f1": 0.872, "params_m": 1.10, "role": "recent"},
        {"method": "LSTM", "latency_ms": 21.0, "f1": 0.858, "params_m": 2.70, "role": "traditional"},
        {"method": "ResNet", "latency_ms": 31.0, "f1": 0.905, "params_m": 5.40, "role": "recent"},
        {"method": "Transformer", "latency_ms": 43.0, "f1": 0.918, "params_m": 8.20, "role": "recent"},
        {"method": "Ours", "latency_ms": 13.5, "f1": 0.923, "params_m": 2.10, "role": "proposed"},
    ]
    write_csv(DATA / "accuracy-latency-pareto.csv", rows)

    width, height = 1280, 720
    left, right, top, bottom = 104, 884, 132, 570
    side_x, side_w = 932, 276
    x_min, x_max = 0, 48
    y_min, y_max = 0.78, 0.94

    def xmap(x: float) -> float:
        return left + (x - x_min) / (x_max - x_min) * (right - left)

    def ymap(y: float) -> float:
        return bottom - (y - y_min) / (y_max - y_min) * (bottom - top)

    def nondominated(data: list[dict[str, object]]) -> list[dict[str, object]]:
        frontier = []
        for p in data:
            dominated = any(
                q["latency_ms"] <= p["latency_ms"]
                and q["f1"] >= p["f1"]
                and (q["latency_ms"] < p["latency_ms"] or q["f1"] > p["f1"])
                for q in data
            )
            if not dominated:
                frontier.append(p)
        return sorted(frontier, key=lambda r: r["latency_ms"])

    role_color = {"proposed": BLUE, "recent": TEAL, "traditional": RED}
    role_fill = {"proposed": BLUE, "recent": TEAL_2, "traditional": WHITE}
    body: list[str] = [
        rect(52, 96, 1176, 574, PANEL, "none", 18),
        rect(left, top, right - left, bottom - top, WHITE, LINE),
        rect(left, top, 334, 176, BLUE_LIGHT, "none", opacity=0.78),
        text(left + 22, top + 28, "preferred region", "method", fill=BLUE),
        text(left + 22, top + 50, "higher F1, lower latency", "small"),
    ]

    for tick_value in [0, 10, 20, 30, 40]:
        x = xmap(tick_value)
        body.append(line(x, top, x, bottom, GRID, 1.0))
        body.append(text(x, bottom + 25, tick_value, "tick", "middle"))
    for tick_value in [0.80, 0.84, 0.88, 0.92]:
        y = ymap(tick_value)
        body.append(line(left, y, right, y, GRID, 1.0))
        body.append(text(left - 14, y + 4, f"{tick_value:.2f}", "tick", "end"))
    body.append(line(left, bottom, right, bottom, DARK, 1.35))
    body.append(line(left, top, left, bottom, DARK, 1.35))

    path = " ".join(f"{xmap(r['latency_ms']):.1f},{ymap(r['f1']):.1f}" for r in nondominated(rows))
    body.append(f'  <polyline points="{path}" fill="none" stroke="{BLUE}" stroke-width="2.4" stroke-dasharray="8,5" opacity="0.9"/>')

    label_offsets = {
        "TinyCNN": (12, 25),
        "MobileNet": (12, -14),
        "LSTM": (14, 23),
        "ResNet": (13, -12),
        "Transformer": (-118, -12),
        "Ours": (14, -22),
    }
    for r in rows:
        x, y = xmap(r["latency_ms"]), ymap(r["f1"])
        radius = 7.5 + r["params_m"] * 1.25
        color = role_color[r["role"]]
        fill = role_fill[r["role"]]
        opacity = 1.0 if r["role"] == "proposed" else 0.76
        body.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" fill="{fill}" fill-opacity="{opacity:.2f}" stroke="{color}" stroke-width="2.2"/>')
        dx, dy = label_offsets[r["method"]]
        label_weight = "700" if r["role"] == "proposed" else "400"
        body.append(text(x + dx, y + dy, r["method"], "legend", fill=DARK, weight=label_weight))

    body.append(text((left + right) / 2, 624, "Inference latency (ms; lower is better)", "axislabel", "middle"))
    body.append(
        f'  <text x="28.0" y="{(top+bottom)/2:.1f}" transform="rotate(-90 28.0 {(top+bottom)/2:.1f})" text-anchor="middle" class="axislabel">'
        "Macro-F1 (higher is better)</text>"
    )

    body.extend(
        [
            rect(side_x, top, side_w, 438, WHITE, LINE, 14),
            text(side_x + 24, top + 34, "Tradeoff evidence", "paneltitle"),
            text(side_x + 24, top + 58, "Ours is on the frontier", "small"),
            line(side_x + 24, top + 78, side_x + side_w - 24, top + 78, LINE, 1.0),
            text(side_x + 24, top + 120, "0.923", "metric", fill=BLUE),
            text(side_x + 116, top + 120, "Macro-F1", "method"),
            text(side_x + 116, top + 142, "higher than large baselines", "small"),
            text(side_x + 24, top + 194, "13.5 ms", "metric", fill=TEAL),
            text(side_x + 128, top + 194, "latency", "method"),
            text(side_x + 128, top + 216, "deployment cost visible", "small"),
            text(side_x + 24, top + 268, "2.10 M", "metric", fill=GOLD),
            text(side_x + 128, top + 268, "params", "method"),
            text(side_x + 128, top + 290, "bubble size encodes cost", "small"),
            line(side_x + 24, top + 294, side_x + side_w - 24, top + 294, LINE, 1.0),
            text(side_x + 24, top + 330, "Encoding", "method"),
            f'  <circle cx="{side_x+34:.1f}" cy="{top+361:.1f}" r="8" fill="{BLUE}" stroke="{BLUE}" stroke-width="2"/>',
            text(side_x + 54, top + 365, "proposed", "legend"),
            f'  <circle cx="{side_x+34:.1f}" cy="{top+393:.1f}" r="8" fill="{TEAL_2}" stroke="{TEAL}" stroke-width="2"/>',
            text(side_x + 54, top + 397, "recent baseline", "legend"),
            f'  <circle cx="{side_x+34:.1f}" cy="{top+425:.1f}" r="8" fill="{WHITE}" stroke="{RED}" stroke-width="2"/>',
            text(side_x + 54, top + 429, "classical baseline", "legend"),
        ]
    )

    svg = svg_wrap(
        width,
        height,
        "Accuracy-latency tradeoff for deployment",
        "Synthetic demo. Accuracy, latency, and parameter cost are shown as one reviewer-facing claim.",
        [("Pareto", BLUE), ("cost visible", GOLD)],
        "\n".join(body),
    )
    (FIGURES / "accuracy-latency-pareto.svg").write_text(svg, encoding="utf-8")


def ablation_result_table() -> None:
    rows = [
        {"variant": "Base encoder", "accuracy": 88.3, "f1": 87.6, "params_m": 1.42, "latency_ms": 8.9},
        {"variant": "+ attention", "accuracy": 90.4, "f1": 89.7, "params_m": 1.78, "latency_ms": 10.7},
        {"variant": "+ temporal", "accuracy": 91.1, "f1": 90.5, "params_m": 1.63, "latency_ms": 9.8},
        {"variant": "+ physics", "accuracy": 91.8, "f1": 91.0, "params_m": 1.95, "latency_ms": 11.5},
        {"variant": "+ augmentation", "accuracy": 92.2, "f1": 91.5, "params_m": 2.10, "latency_ms": 12.9},
        {"variant": "Full model", "accuracy": 94.1, "f1": 93.6, "params_m": 2.10, "latency_ms": 13.2},
    ]
    write_csv(DATA / "ablation-result-table.csv", rows)

    width, height = 1280, 720
    table_x, table_y = 58, 130
    table_w = 724
    row_h = 48
    col_w = [244, 112, 112, 126, 130]
    headers = ["Variant", "Acc. (%)", "F1 (%)", "Params (M)", "Latency (ms)"]
    best_accuracy = max(r["accuracy"] for r in rows)
    best_f1 = max(r["f1"] for r in rows)

    body: list[str] = [
        rect(52, 96, 1176, 574, PANEL, "none", 18),
        rect(table_x, table_y, table_w, row_h, DARK, "none", 10),
    ]
    cx = table_x
    for i, header in enumerate(headers):
        anchor = "start" if i == 0 else "middle"
        tx = cx + 20 if i == 0 else cx + col_w[i] / 2
        body.append(text(tx, table_y + 31, header, "header", anchor, WHITE, "700"))
        cx += col_w[i]

    for ridx, r in enumerate(rows):
        y = table_y + row_h * (ridx + 1)
        is_full = r["variant"] == "Full model"
        fill = BLUE_LIGHT if is_full else (WHITE if ridx % 2 else PANEL_2)
        body.append(rect(table_x, y, table_w, row_h, fill, LINE))
        values = [r["variant"], f'{r["accuracy"]:.1f}', f'{r["f1"]:.1f}', f'{r["params_m"]:.2f}', f'{r["latency_ms"]:.1f}']
        cx = table_x
        for i, value in enumerate(values):
            anchor = "start" if i == 0 else "middle"
            tx = cx + 20 if i == 0 else cx + col_w[i] / 2
            is_best = (i == 1 and r["accuracy"] == best_accuracy) or (i == 2 and r["f1"] == best_f1)
            bold = is_full or is_best
            fill_color = BLUE if is_best else DARK
            body.append(text(tx, y + 30, value, "cell", anchor, fill_color, "700" if bold else "400"))
            cx += col_w[i]

    panel_x, panel_y = 830, 130
    panel_w, panel_h = 374, 384
    body.extend(
        [
            rect(panel_x, panel_y, panel_w, panel_h, WHITE, LINE, 14),
            text(panel_x + 24, panel_y + 34, "Component contribution", "paneltitle"),
            text(panel_x + 24, panel_y + 57, "delta accuracy points over base", "small"),
            line(panel_x + 24, panel_y + 78, panel_x + panel_w - 24, panel_y + 78, LINE, 1.0),
        ]
    )
    base_acc = rows[0]["accuracy"]
    deltas = [(r["variant"].replace("+ ", ""), r["accuracy"] - base_acc, r["variant"] == "Full model") for r in rows[1:]]
    max_delta = max(delta for _, delta, _ in deltas)
    bar_x, bar_w = panel_x + 126, 194
    for i, (label, delta, is_full) in enumerate(deltas):
        y = panel_y + 112 + i * 44
        color = BLUE if is_full else TEAL
        label_text = {"temporal": "temporal", "physics": "physics", "augmentation": "augment"}.get(label, label)
        body.append(text(panel_x + 24, y + 16, label_text, "small"))
        body.append(rect(bar_x, y, bar_w, 18, "#E8EEF5", "none", 6))
        body.append(rect(bar_x, y, bar_w * delta / max_delta, 18, color, "none", 6, 0.92))
        body.append(text(bar_x + bar_w + 10, y + 15, f"+{delta:.1f}", "tiny"))

    chip_y = 548
    body.extend(
        [
            rect(table_x, chip_y, 244, 44, WHITE, LINE, 10),
            text(table_x + 18, chip_y + 19, "What this table proves", "method", fill=BLUE),
            text(table_x + 18, chip_y + 37, "each module supports the final claim", "small"),
            rect(table_x + 268, chip_y, 252, 44, WHITE, LINE, 10),
            text(table_x + 286, chip_y + 19, "What it does not hide", "method", fill=TEAL),
            text(table_x + 286, chip_y + 37, "params and latency stay visible", "small"),
            rect(table_x + 544, chip_y, 238, 44, WHITE, LINE, 10),
            text(table_x + 562, chip_y + 19, "Missing in real papers", "method", fill=RED),
            text(table_x + 562, chip_y + 37, "variance, seeds, significance", "small"),
            rect(panel_x, chip_y, 374, 44, WHITE, LINE, 10),
            text(panel_x + 20, chip_y + 19, "IEEE reviewer cue", "method", fill=GOLD),
            text(panel_x + 20, chip_y + 37, "performance gain is tied to component evidence", "small"),
        ]
    )

    svg = svg_wrap(
        width,
        height,
        "Ablation table with visible engineering cost",
        "Synthetic demo. Component gains, full-model result, and deployment cost stay in the same view.",
        [("ablation", BLUE), ("cost kept", GOLD)],
        "\n".join(body),
    )
    (FIGURES / "ablation-result-table.svg").write_text(svg, encoding="utf-8")


def write_captions() -> None:
    text = """# Captions and QA Notes

## Robustness SNR Curve

Caption draft: Bit error rate under decreasing SNR. The proposed method shows lower BER than MMSE, CNN, and Transformer baselines across all tested channel conditions, supporting the robustness claim under low-SNR operation.

QA: The figure uses a dedicated evidence panel, a visible stress-condition band, log-scale labeling, and marker/line-style redundancy. The legend is outside the data area.

## Accuracy-Latency Pareto

Caption draft: Accuracy-latency tradeoff for deployment-oriented comparison. The proposed method lies on the Pareto frontier by improving macro-F1 while keeping inference latency lower than larger neural baselines.

QA: The figure shows accuracy, latency, and parameter cost in one claim-facing view. Labels are short, the role encoding is separated from the scatter area, and deployment cost is not hidden in text.

## Ablation Result Table

Caption draft: Ablation study of the proposed model components. Adding attention, temporal modeling, physics guidance, and augmentation improves accuracy and F1, while the table keeps parameter count and latency visible.

QA: The table uses consistent precision, highlights only the full-model/best metrics, keeps cost metrics visible, and states missing real-manuscript requirements such as variance, seeds, and significance testing.
"""
    (ROOT / "captions.md").write_text(text, encoding="utf-8")


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    robustness_snr_curve()
    accuracy_latency_pareto()
    ablation_result_table()
    write_captions()
    print(f"Wrote refreshed examples under {ROOT}")


if __name__ == "__main__":
    main()
