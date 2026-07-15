#!/usr/bin/env python3
"""Generate zero-dependency IEEE figure/table example SVGs.

The examples are intentionally synthetic. They demonstrate figure contracts,
not real experimental results.
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
TEAL = "#0F766E"
CYAN = "#20B7A6"
RED = "#B64040"
GRAY = "#596579"
DARK = "#172033"
LIGHT = "#E7EDF4"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def svg_wrap(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
  <rect width="{width}" height="{height}" fill="#ffffff"/>
  <style>
    text {{ font-family: Arial, Helvetica, sans-serif; }}
    .title {{ font-size: 24px; font-weight: 700; }}
    .subtitle {{ font-size: 15px; fill: {GRAY}; }}
    .axis {{ stroke: {DARK}; stroke-width: 1.4; }}
    .grid {{ stroke: #D8E0EA; stroke-width: 1; }}
    .tick {{ font-size: 13px; fill: {GRAY}; }}
    .label {{ font-size: 15px; font-weight: 700; }}
    .small {{ font-size: 12px; fill: {GRAY}; }}
    .legend {{ font-size: 14px; }}
    .panel {{ font-size: 16px; font-weight: 700; }}
  </style>
{body}
</svg>
"""


def marker(x: float, y: float, color: str, shape: str) -> str:
    if shape == "circle":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.8" fill="{color}" stroke="#ffffff" stroke-width="1.2"/>'
    if shape == "square":
        return f'<rect x="{x-4.5:.1f}" y="{y-4.5:.1f}" width="9" height="9" fill="{color}" stroke="#ffffff" stroke-width="1.2"/>'
    if shape == "diamond":
        return f'<path d="M{x:.1f},{y-6:.1f} L{x+6:.1f},{y:.1f} L{x:.1f},{y+6:.1f} L{x-6:.1f},{y:.1f} Z" fill="{color}" stroke="#ffffff" stroke-width="1.2"/>'
    return f'<path d="M{x:.1f},{y-6:.1f} L{x+5.5:.1f},{y+5:.1f} L{x-5.5:.1f},{y+5:.1f} Z" fill="{color}" stroke="#ffffff" stroke-width="1.2"/>'


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

    width, height = 1120, 650
    left, right, top, bottom = 110, 1040, 118, 540
    x_min, x_max = -10, 20
    y_min, y_max = 1e-4, 2e-1

    def xmap(x: float) -> float:
        return left + (x - x_min) / (x_max - x_min) * (right - left)

    def ymap(y: float) -> float:
        lo, hi = math.log10(y_min), math.log10(y_max)
        return bottom - (math.log10(y) - lo) / (hi - lo) * (bottom - top)

    methods = [
        ("MMSE", GRAY, "circle", "6,5"),
        ("CNN", RED, "square", ""),
        ("Transformer", TEAL, "diamond", "2,4"),
        ("Ours", BLUE, "triangle", ""),
    ]

    body = [
        '<text x="54" y="48" class="title">Robustness under low-SNR operating conditions</text>',
        '<text x="54" y="76" class="subtitle">Lower BER is better. Markers and line styles remain distinguishable in grayscale.</text>',
        f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" class="axis"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" class="axis"/>',
    ]

    for tick in [-10, -5, 0, 5, 10, 15, 20]:
        x = xmap(tick)
        body.append(f'<line x1="{x:.1f}" y1="{bottom}" x2="{x:.1f}" y2="{bottom+6}" class="axis"/>')
        body.append(f'<text x="{x:.1f}" y="{bottom+26}" text-anchor="middle" class="tick">{tick}</text>')
    for tick, label in [(1e-1, "10^-1"), (1e-2, "10^-2"), (1e-3, "10^-3"), (1e-4, "10^-4")]:
        y = ymap(tick)
        body.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" class="grid"/>')
        body.append(f'<line x1="{left-6}" y1="{y:.1f}" x2="{left}" y2="{y:.1f}" class="axis"/>')
        body.append(f'<text x="{left-14}" y="{y+4:.1f}" text-anchor="end" class="tick">{label}</text>')

    for name, color, shape, dash in methods:
        points = [(xmap(r["snr_db"]), ymap(r[name])) for r in rows]
        path = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        body.append(f'<polyline points="{path}" fill="none" stroke="{color}" stroke-width="3"{dash_attr}/>')
        for x, y in points:
            body.append(marker(x, y, color, shape))

    body.append(f'<text x="{(left+right)/2:.1f}" y="{height-44}" text-anchor="middle" class="label">SNR (dB)</text>')
    body.append(f'<text x="28" y="{(top+bottom)/2:.1f}" transform="rotate(-90 28 {(top+bottom)/2:.1f})" text-anchor="middle" class="label">Bit error rate (log scale)</text>')

    lx, ly = 710, 132
    body.append(f'<rect x="{lx-18}" y="{ly-28}" width="318" height="122" rx="8" fill="#ffffff" stroke="{LIGHT}"/>')
    for i, (name, color, shape, dash) in enumerate(methods):
        y = ly + i * 27
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        body.append(f'<line x1="{lx}" y1="{y}" x2="{lx+46}" y2="{y}" stroke="{color}" stroke-width="3"{dash_attr}/>')
        body.append(marker(lx + 23, y, color, shape))
        body.append(f'<text x="{lx+62}" y="{y+5}" class="legend">{esc(name)}</text>')
    body.append(f'<text x="{right}" y="{top-26}" text-anchor="end" class="small">Claim: robust performance persists as channel quality degrades.</text>')

    (FIGURES / "robustness-snr-curve.svg").write_text(svg_wrap(width, height, "\n".join(body)), encoding="utf-8")


def accuracy_latency_pareto() -> None:
    rows = [
        {"method": "TinyCNN", "latency_ms": 5.4, "f1": 0.812, "params_m": 0.48},
        {"method": "MobileNet", "latency_ms": 8.8, "f1": 0.872, "params_m": 1.10},
        {"method": "LSTM", "latency_ms": 21.0, "f1": 0.858, "params_m": 2.70},
        {"method": "ResNet", "latency_ms": 31.0, "f1": 0.905, "params_m": 5.40},
        {"method": "Transformer", "latency_ms": 43.0, "f1": 0.918, "params_m": 8.20},
        {"method": "Ours", "latency_ms": 13.5, "f1": 0.923, "params_m": 2.10},
    ]
    write_csv(DATA / "accuracy-latency-pareto.csv", rows)

    width, height = 980, 620
    left, right, top, bottom = 110, 870, 112, 510
    x_min, x_max = 0, 48
    y_min, y_max = 0.78, 0.94

    def xmap(x: float) -> float:
        return left + (x - x_min) / (x_max - x_min) * (right - left)

    def ymap(y: float) -> float:
        return bottom - (y - y_min) / (y_max - y_min) * (bottom - top)

    def nondominated(data: list[dict[str, object]]) -> list[dict[str, object]]:
        out = []
        for p in data:
            dominated = any(
                q["latency_ms"] <= p["latency_ms"]
                and q["f1"] >= p["f1"]
                and (q["latency_ms"] < p["latency_ms"] or q["f1"] > p["f1"])
                for q in data
            )
            if not dominated:
                out.append(p)
        return sorted(out, key=lambda r: r["latency_ms"])

    body = [
        '<text x="54" y="48" class="title">Accuracy-latency Pareto evidence for deployment</text>',
        '<text x="54" y="76" class="subtitle">Upper-left is better: higher F1 with lower inference latency.</text>',
        f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" class="axis"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" class="axis"/>',
    ]
    for tick in [0, 10, 20, 30, 40]:
        x = xmap(tick)
        body.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{bottom}" class="grid"/>')
        body.append(f'<text x="{x:.1f}" y="{bottom+25}" text-anchor="middle" class="tick">{tick}</text>')
    for tick in [0.80, 0.84, 0.88, 0.92]:
        y = ymap(tick)
        body.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" class="grid"/>')
        body.append(f'<text x="{left-12}" y="{y+4:.1f}" text-anchor="end" class="tick">{tick:.2f}</text>')

    pareto = nondominated(rows)
    path = " ".join(f"{xmap(r['latency_ms']):.1f},{ymap(r['f1']):.1f}" for r in pareto)
    body.append(f'<polyline points="{path}" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="7,5"/>')

    for r in rows:
        is_ours = r["method"] == "Ours"
        x, y = xmap(r["latency_ms"]), ymap(r["f1"])
        size = 7 + r["params_m"] * 2.2
        color = BLUE if is_ours else "#A8B3C2"
        stroke = DARK if is_ours else "#697789"
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" fill="{color}" fill-opacity="0.82" stroke="{stroke}" stroke-width="1.4"/>')
        dy = -16 if is_ours else -12
        weight = ' font-weight="700"' if is_ours else ""
        body.append(f'<text x="{x+10:.1f}" y="{y+dy:.1f}" class="legend"{weight}>{esc(r["method"])}</text>')

    body.append(f'<text x="{(left+right)/2:.1f}" y="{height-44}" text-anchor="middle" class="label">Inference latency (ms, lower is better)</text>')
    body.append(f'<text x="28" y="{(top+bottom)/2:.1f}" transform="rotate(-90 28 {(top+bottom)/2:.1f})" text-anchor="middle" class="label">F1 score (higher is better)</text>')
    body.append(f'<text x="{right}" y="{top-24}" text-anchor="end" class="small">Circle size encodes parameter count. Dashed line marks the Pareto frontier.</text>')

    (FIGURES / "accuracy-latency-pareto.svg").write_text(svg_wrap(width, height, "\n".join(body)), encoding="utf-8")


def ablation_result_table() -> None:
    rows = [
        {"variant": "Base encoder", "accuracy": 88.3, "f1": 87.6, "params_m": 1.42, "latency_ms": 8.9},
        {"variant": "w/o attention", "accuracy": 90.4, "f1": 89.7, "params_m": 1.78, "latency_ms": 10.7},
        {"variant": "w/o temporal module", "accuracy": 91.1, "f1": 90.5, "params_m": 1.63, "latency_ms": 9.8},
        {"variant": "w/o physics constraint", "accuracy": 91.8, "f1": 91.0, "params_m": 1.95, "latency_ms": 11.5},
        {"variant": "w/o augmentation", "accuracy": 92.2, "f1": 91.5, "params_m": 2.10, "latency_ms": 12.9},
        {"variant": "Full model", "accuracy": 94.1, "f1": 93.6, "params_m": 2.10, "latency_ms": 13.2},
    ]
    write_csv(DATA / "ablation-result-table.csv", rows)

    width, height = 1120, 610
    x0, y0 = 64, 124
    col_w = [320, 150, 150, 150, 160]
    row_h = 54
    headers = ["Variant", "Accuracy (%)", "F1 (%)", "Params (M)", "Latency (ms)"]
    body = [
        '<text x="54" y="48" class="title">Ablation table linking modules to evidence</text>',
        '<text x="54" y="76" class="subtitle">Best performance is bolded; deployability metrics remain visible instead of hidden in text.</text>',
    ]

    total_w = sum(col_w)
    body.append(f'<rect x="{x0}" y="{y0}" width="{total_w}" height="{row_h}" fill="#10233C" rx="7"/>')
    cx = x0
    for i, h in enumerate(headers):
        anchor = "start" if i == 0 else "middle"
        tx = cx + 18 if i == 0 else cx + col_w[i] / 2
        body.append(f'<text x="{tx:.1f}" y="{y0+34}" text-anchor="{anchor}" fill="#ffffff" font-size="15" font-weight="700">{esc(h)}</text>')
        cx += col_w[i]

    best_accuracy = max(r["accuracy"] for r in rows)
    best_f1 = max(r["f1"] for r in rows)
    min_latency = min(r["latency_ms"] for r in rows)

    for ridx, r in enumerate(rows):
        y = y0 + row_h * (ridx + 1)
        fill = "#EAF4FF" if r["variant"] == "Full model" else ("#F8FAFC" if ridx % 2 == 0 else "#FFFFFF")
        body.append(f'<rect x="{x0}" y="{y}" width="{total_w}" height="{row_h}" fill="{fill}" stroke="#D8E0EA"/>')
        values = [
            r["variant"],
            f'{r["accuracy"]:.1f}',
            f'{r["f1"]:.1f}',
            f'{r["params_m"]:.2f}',
            f'{r["latency_ms"]:.1f}',
        ]
        cx = x0
        for i, value in enumerate(values):
            anchor = "start" if i == 0 else "middle"
            tx = cx + 18 if i == 0 else cx + col_w[i] / 2
            bold = (
                r["variant"] == "Full model"
                or (i == 1 and r["accuracy"] == best_accuracy)
                or (i == 2 and r["f1"] == best_f1)
                or (i == 4 and r["latency_ms"] == min_latency)
            )
            color = BLUE if bold and i in {1, 2} else (TEAL if i == 4 and r["latency_ms"] == min_latency else DARK)
            weight = "700" if bold else "400"
            body.append(f'<text x="{tx:.1f}" y="{y+34}" text-anchor="{anchor}" font-size="15" font-weight="{weight}" fill="{color}">{esc(value)}</text>')
            cx += col_w[i]

    note_y = y0 + row_h * (len(rows) + 1) + 46
    body.append(f'<text x="{x0}" y="{note_y}" class="small">Claim: attention, temporal modeling, physics guidance, and augmentation each improve predictive evidence; latency remains within the deployment budget.</text>')
    body.append(f'<text x="{x0}" y="{note_y+25}" class="small">Missing in real manuscripts: repeat definition, variance or confidence interval, statistical test if wins are claimed as significant.</text>')

    (FIGURES / "ablation-result-table.svg").write_text(svg_wrap(width, height, "\n".join(body)), encoding="utf-8")


def write_captions() -> None:
    text = """# Captions and QA Notes

## Robustness SNR Curve

Caption draft: Bit error rate under decreasing SNR. The proposed method shows lower BER than MMSE, CNN, and Transformer baselines across all tested channel conditions, supporting the robustness claim under low-SNR operation.

QA: The x-axis is an engineering operating condition, the y-axis uses a labeled log scale, and marker/line-style redundancy supports grayscale readability.

## Accuracy-Latency Pareto

Caption draft: Accuracy-latency tradeoff for deployment-oriented comparison. The proposed method lies on the Pareto frontier by improving F1 while keeping inference latency lower than larger neural baselines.

QA: The figure makes the cost metric visible, labels both optimization directions, and avoids claiming accuracy improvement without deployment cost.

## Ablation Result Table

Caption draft: Ablation study of the proposed model components. Removing attention, temporal modeling, physics guidance, or augmentation reduces accuracy and F1, indicating that each component contributes to the final model.

QA: The table keeps performance and deployability metrics together. Real manuscripts should add repeat definitions, variability, and significance testing where appropriate.
"""
    (ROOT / "captions.md").write_text(text, encoding="utf-8")


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    robustness_snr_curve()
    accuracy_latency_pareto()
    ablation_result_table()
    write_captions()
    print(f"Wrote examples under {ROOT}")


if __name__ == "__main__":
    main()
