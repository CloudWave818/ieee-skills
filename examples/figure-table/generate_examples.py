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
BLUE_LIGHT = "#D9ECFF"
TEAL = "#0F766E"
RED = "#B64040"
COST = "#B7791F"
GRAY = "#6B7280"
GRAY_2 = "#AAB4C3"
DARK = "#172033"
GRID = "#D7DEE8"
PANEL = "#F7FAFD"
LINE = "#DCE3EC"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def svg_wrap(width: int, height: int, title: str, subtitle: str, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">
  <rect width="{width}" height="{height}" fill="#ffffff"/>
  <style>
    text {{ font-family: Arial, Helvetica, sans-serif; fill: {DARK}; }}
    .title {{ font-size: 25px; font-weight: 700; }}
    .subtitle {{ font-size: 14px; fill: {GRAY}; }}
    .axis {{ stroke: {DARK}; stroke-width: 1.35; }}
    .grid {{ stroke: {GRID}; stroke-width: 1; }}
    .tick {{ font-size: 12.5px; fill: {GRAY}; }}
    .label {{ font-size: 14.5px; font-weight: 700; }}
    .small {{ font-size: 12px; fill: {GRAY}; }}
    .legend {{ font-size: 13.5px; fill: {DARK}; }}
    .note {{ font-size: 12px; fill: {GRAY}; }}
    .panel {{ font-size: 16px; font-weight: 700; }}
    .method {{ font-size: 13px; font-weight: 700; }}
  </style>
  <text x="54" y="46" class="title">{esc(title)}</text>
  <text x="54" y="72" class="subtitle">{esc(subtitle)}</text>
{body}
</svg>
"""


def marker(x: float, y: float, color: str, shape: str, r: float = 5.0) -> str:
    if shape == "circle":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" stroke="#ffffff" stroke-width="1.4"/>'
    if shape == "square":
        return f'<rect x="{x-r:.1f}" y="{y-r:.1f}" width="{2*r:.1f}" height="{2*r:.1f}" fill="{color}" stroke="#ffffff" stroke-width="1.4"/>'
    if shape == "diamond":
        return f'<path d="M{x:.1f},{y-r-1:.1f} L{x+r+1:.1f},{y:.1f} L{x:.1f},{y+r+1:.1f} L{x-r-1:.1f},{y:.1f} Z" fill="{color}" stroke="#ffffff" stroke-width="1.4"/>'
    return f'<path d="M{x:.1f},{y-r-1:.1f} L{x+r:.1f},{y+r:.1f} L{x-r:.1f},{y+r:.1f} Z" fill="{color}" stroke="#ffffff" stroke-width="1.4"/>'


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

    width, height = 1180, 680
    left, right, top, bottom = 116, 1070, 132, 548
    x_min, x_max = -10, 20
    y_min, y_max = 1e-4, 2e-1

    def xmap(x: float) -> float:
        return left + (x - x_min) / (x_max - x_min) * (right - left)

    def ymap(y: float) -> float:
        lo, hi = math.log10(y_min), math.log10(y_max)
        return bottom - (math.log10(y) - lo) / (hi - lo) * (bottom - top)

    methods = [
        ("MMSE", GRAY, "triangle", "3,4"),
        ("CNN", RED, "square", "7,4"),
        ("Transformer", TEAL, "diamond", "2,3"),
        ("Ours", BLUE, "circle", ""),
    ]

    low_snr_x0 = xmap(-10)
    low_snr_x1 = xmap(0)
    body = [
        f'  <rect x="{left}" y="{top}" width="{right-left}" height="{bottom-top}" fill="#ffffff" stroke="{LINE}"/>',
        f'  <rect x="{low_snr_x0:.1f}" y="{top}" width="{low_snr_x1-low_snr_x0:.1f}" height="{bottom-top}" fill="{BLUE_LIGHT}" opacity="0.42"/>',
        f'  <text x="{(low_snr_x0+low_snr_x1)/2:.1f}" y="{top+24}" text-anchor="middle" class="note">low-SNR stress region</text>',
    ]

    for tick in [-10, -5, 0, 5, 10, 15, 20]:
        x = xmap(tick)
        body.append(f'  <line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{bottom}" class="grid"/>')
        body.append(f'  <line x1="{x:.1f}" y1="{bottom}" x2="{x:.1f}" y2="{bottom+6}" class="axis"/>')
        body.append(f'  <text x="{x:.1f}" y="{bottom+26}" text-anchor="middle" class="tick">{tick}</text>')
    for tick, label in [(1e-1, "10^-1"), (1e-2, "10^-2"), (1e-3, "10^-3"), (1e-4, "10^-4")]:
        y = ymap(tick)
        body.append(f'  <line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" class="grid"/>')
        body.append(f'  <line x1="{left-6}" y1="{y:.1f}" x2="{left}" y2="{y:.1f}" class="axis"/>')
        body.append(f'  <text x="{left-14}" y="{y+4:.1f}" text-anchor="end" class="tick">{label}</text>')

    body.append(f'  <line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" class="axis"/>')
    body.append(f'  <line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" class="axis"/>')

    for name, color, shape, dash in methods:
        points = [(xmap(r["snr_db"]), ymap(r[name])) for r in rows]
        path = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        width_attr = 3.6 if name == "Ours" else 2.5
        opacity = 1.0 if name == "Ours" else 0.86
        body.append(f'  <polyline points="{path}" fill="none" stroke="{color}" stroke-width="{width_attr}" opacity="{opacity}"{dash_attr}/>')
        for x, y in points:
            body.append("  " + marker(x, y, color, shape, 5.2 if name == "Ours" else 4.8))

    lx, ly = 640, 99
    for i, (name, color, shape, dash) in enumerate(methods):
        x = lx + i * 124
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        body.append(f'  <line x1="{x}" y1="{ly}" x2="{x+38}" y2="{ly}" stroke="{color}" stroke-width="2.8"{dash_attr}/>')
        body.append("  " + marker(x + 19, ly, color, shape, 4.5))
        body.append(f'  <text x="{x+48}" y="{ly+4}" class="legend">{esc(name)}</text>')

    ours_last = (xmap(20), ymap(rows[-1]["Ours"]))
    body.extend(
        [
            f'  <rect x="{ours_last[0]-300:.1f}" y="{ours_last[1]-104:.1f}" width="218" height="52" rx="7" fill="#ffffff" stroke="{LINE}"/>',
            f'  <path d="M{ours_last[0]-82:.1f},{ours_last[1]-78:.1f} C{ours_last[0]-52:.1f},{ours_last[1]-54:.1f} {ours_last[0]-34:.1f},{ours_last[1]-26:.1f} {ours_last[0]-12:.1f},{ours_last[1]-8:.1f}" fill="none" stroke="{BLUE}" stroke-width="1.4" marker-end="url(#arrow-blue)"/>',
            f'  <defs><marker id="arrow-blue" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto"><path d="M0,0 L8,3.5 L0,7 Z" fill="{BLUE}"/></marker></defs>',
            f'  <text x="{ours_last[0]-282:.1f}" y="{ours_last[1]-82:.1f}" class="method" style="fill:{BLUE}">Ours keeps the lowest BER</text>',
            f'  <text x="{ours_last[0]-282:.1f}" y="{ours_last[1]-62:.1f}" class="small">claim evidence across all SNR levels</text>',
        ]
    )

    body.append(f'  <text x="{(left+right)/2:.1f}" y="{height-43}" text-anchor="middle" class="label">SNR (dB)</text>')
    body.append(f'  <text x="30" y="{(top+bottom)/2:.1f}" transform="rotate(-90 30 {(top+bottom)/2:.1f})" text-anchor="middle" class="label">Bit error rate, BER (log scale; lower is better)</text>')
    body.append(f'  <text x="{right}" y="{height-20}" text-anchor="end" class="small">IEEE QA: condition axis, log scale label, marker/line-style redundancy, visible baselines.</text>')

    svg = svg_wrap(
        width,
        height,
        "Robustness evidence under low-SNR conditions",
        "Synthetic demo. Lower BER is better; the stress condition is visible instead of hidden in text.",
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

    width, height = 1120, 650
    left, right, top, bottom = 112, 940, 122, 532
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

    role_color = {"proposed": BLUE, "recent": TEAL, "traditional": RED}
    role_fill = {"proposed": BLUE, "recent": TEAL, "traditional": "#FFFFFF"}
    body = [
        f'  <rect x="{left}" y="{top}" width="{right-left}" height="{bottom-top}" fill="#ffffff" stroke="{LINE}"/>',
        f'  <rect x="{left}" y="{top}" width="{(right-left)*0.40:.1f}" height="{(bottom-top)*0.42:.1f}" fill="{BLUE_LIGHT}" opacity="0.36"/>',
        f'  <text x="{left+22}" y="{top+28}" class="note">preferred region: high F1 + low latency</text>',
    ]

    for tick in [0, 10, 20, 30, 40]:
        x = xmap(tick)
        body.append(f'  <line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{bottom}" class="grid"/>')
        body.append(f'  <text x="{x:.1f}" y="{bottom+25}" text-anchor="middle" class="tick">{tick}</text>')
    for tick in [0.80, 0.84, 0.88, 0.92]:
        y = ymap(tick)
        body.append(f'  <line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" class="grid"/>')
        body.append(f'  <text x="{left-12}" y="{y+4:.1f}" text-anchor="end" class="tick">{tick:.2f}</text>')

    body.append(f'  <line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" class="axis"/>')
    body.append(f'  <line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" class="axis"/>')

    pareto = nondominated(rows)
    path = " ".join(f"{xmap(r['latency_ms']):.1f},{ymap(r['f1']):.1f}" for r in pareto)
    body.append(f'  <polyline points="{path}" fill="none" stroke="{BLUE}" stroke-width="2.2" stroke-dasharray="8,5" opacity="0.9"/>')

    label_offsets = {
        "TinyCNN": (9, 20),
        "MobileNet": (10, -13),
        "LSTM": (10, 22),
        "ResNet": (10, -10),
        "Transformer": (-122, -13),
        "Ours": (12, -18),
    }
    for r in rows:
        x, y = xmap(r["latency_ms"]), ymap(r["f1"])
        radius = 7.5 + r["params_m"] * 1.35
        color = role_color[r["role"]]
        fill = role_fill[r["role"]]
        opacity = 0.95 if r["role"] == "proposed" else 0.72
        body.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" fill="{fill}" fill-opacity="{opacity}" stroke="{color}" stroke-width="2"/>')
        dx, dy = label_offsets[r["method"]]
        weight = "700" if r["role"] == "proposed" else "400"
        body.append(f'  <text x="{x+dx:.1f}" y="{y+dy:.1f}" class="legend" font-weight="{weight}">{esc(r["method"])}</text>')

    side_x, side_y = 973, 158
    body.extend(
        [
            f'  <rect x="{side_x}" y="{side_y}" width="104" height="242" rx="8" fill="{PANEL}" stroke="{LINE}"/>',
            f'  <text x="{side_x+18}" y="{side_y+34}" class="method">Encoding</text>',
            f'  <circle cx="{side_x+24}" cy="{side_y+66}" r="8" fill="{BLUE}" stroke="{BLUE}" stroke-width="2"/>',
            f'  <text x="{side_x+42}" y="{side_y+70}" class="legend">proposed</text>',
            f'  <circle cx="{side_x+24}" cy="{side_y+102}" r="8" fill="{TEAL}" fill-opacity="0.72" stroke="{TEAL}" stroke-width="2"/>',
            f'  <text x="{side_x+42}" y="{side_y+106}" class="legend">recent</text>',
            f'  <circle cx="{side_x+24}" cy="{side_y+138}" r="8" fill="#fff" stroke="{RED}" stroke-width="2"/>',
            f'  <text x="{side_x+42}" y="{side_y+142}" class="legend">classical</text>',
            f'  <line x1="{side_x+18}" y1="{side_y+170}" x2="{side_x+86}" y2="{side_y+170}" stroke="{LINE}"/>',
            f'  <text x="{side_x+18}" y="{side_y+198}" class="small">bubble size</text>',
            f'  <text x="{side_x+18}" y="{side_y+218}" class="small">= parameters</text>',
        ]
    )

    body.append(f'  <text x="{(left+right)/2:.1f}" y="{height-45}" text-anchor="middle" class="label">Inference latency (ms; lower is better)</text>')
    body.append(f'  <text x="30" y="{(top+bottom)/2:.1f}" transform="rotate(-90 30 {(top+bottom)/2:.1f})" text-anchor="middle" class="label">Macro-F1 (higher is better)</text>')
    body.append(f'  <text x="{right}" y="{height-20}" text-anchor="end" class="small">IEEE QA: accuracy and deployment cost are visible in the same evidence panel.</text>')

    svg = svg_wrap(
        width,
        height,
        "Accuracy-latency tradeoff for deployment",
        "Synthetic demo. Upper-left evidence supports a bounded deployment claim rather than accuracy-only reporting.",
        "\n".join(body),
    )
    (FIGURES / "accuracy-latency-pareto.svg").write_text(svg, encoding="utf-8")


def ablation_result_table() -> None:
    rows = [
        {"variant": "Base encoder", "accuracy": 88.3, "f1": 87.6, "params_m": 1.42, "latency_ms": 8.9},
        {"variant": "+ attention", "accuracy": 90.4, "f1": 89.7, "params_m": 1.78, "latency_ms": 10.7},
        {"variant": "+ temporal module", "accuracy": 91.1, "f1": 90.5, "params_m": 1.63, "latency_ms": 9.8},
        {"variant": "+ physics constraint", "accuracy": 91.8, "f1": 91.0, "params_m": 1.95, "latency_ms": 11.5},
        {"variant": "+ augmentation", "accuracy": 92.2, "f1": 91.5, "params_m": 2.10, "latency_ms": 12.9},
        {"variant": "Full model", "accuracy": 94.1, "f1": 93.6, "params_m": 2.10, "latency_ms": 13.2},
    ]
    write_csv(DATA / "ablation-result-table.csv", rows)

    width, height = 1180, 650
    x0, y0 = 62, 120
    table_w = 720
    row_h = 48
    col_w = [260, 116, 116, 116, 112]
    headers = ["Variant", "Acc. (%)", "F1 (%)", "Params", "Latency"]
    base_acc = rows[0]["accuracy"]
    best_accuracy = max(r["accuracy"] for r in rows)
    best_f1 = max(r["f1"] for r in rows)

    body = [
        f'  <rect x="{x0}" y="{y0}" width="{table_w}" height="{row_h}" rx="8" fill="{DARK}"/>',
    ]
    cx = x0
    for i, h in enumerate(headers):
        anchor = "start" if i == 0 else "middle"
        tx = cx + 20 if i == 0 else cx + col_w[i] / 2
        body.append(f'  <text x="{tx:.1f}" y="{y0+31}" text-anchor="{anchor}" style="fill:#ffffff" font-size="14" font-weight="700">{esc(h)}</text>')
        cx += col_w[i]

    for ridx, r in enumerate(rows):
        y = y0 + row_h * (ridx + 1)
        is_full = r["variant"] == "Full model"
        fill = BLUE_LIGHT if is_full else ("#FFFFFF" if ridx % 2 else PANEL)
        body.append(f'  <rect x="{x0}" y="{y}" width="{table_w}" height="{row_h}" fill="{fill}" stroke="{LINE}"/>')
        values = [
            r["variant"],
            f'{r["accuracy"]:.1f}',
            f'{r["f1"]:.1f}',
            f'{r["params_m"]:.2f}M',
            f'{r["latency_ms"]:.1f}ms',
        ]
        cx = x0
        for i, value in enumerate(values):
            anchor = "start" if i == 0 else "middle"
            tx = cx + 20 if i == 0 else cx + col_w[i] / 2
            bold = is_full or (i == 1 and r["accuracy"] == best_accuracy) or (i == 2 and r["f1"] == best_f1)
            color = BLUE if bold and i in {1, 2} else DARK
            weight = "700" if bold else "400"
            body.append(f'  <text x="{tx:.1f}" y="{y+30}" text-anchor="{anchor}" font-size="14" font-weight="{weight}" fill="{color}">{esc(value)}</text>')
            cx += col_w[i]

    chart_x, chart_y = 845, 143
    chart_w, chart_h = 258, 316
    body.extend(
        [
            f'  <rect x="{chart_x-24}" y="{chart_y-54}" width="{chart_w+68}" height="{chart_h+125}" rx="10" fill="{PANEL}" stroke="{LINE}"/>',
            f'  <text x="{chart_x-4}" y="{chart_y-24}" class="method">Contribution over base</text>',
            f'  <text x="{chart_x-4}" y="{chart_y-4}" class="small">delta accuracy points; higher is better</text>',
        ]
    )
    bar_max = max(r["accuracy"] - base_acc for r in rows)
    for i, r in enumerate(rows[1:]):
        y = chart_y + i * 48
        delta = r["accuracy"] - base_acc
        bw = chart_w * delta / bar_max
        is_full = r["variant"] == "Full model"
        color = BLUE if is_full else TEAL
        label_map = {
            "+ attention": "Attention",
            "+ temporal module": "Temporal",
            "+ physics constraint": "Physics",
            "+ augmentation": "Aug.",
            "Full model": "Full",
        }
        label = label_map.get(r["variant"], r["variant"].replace("+ ", ""))
        body.append(f'  <text x="{chart_x-8}" y="{y+18}" text-anchor="end" class="small">{esc(label)}</text>')
        body.append(f'  <rect x="{chart_x}" y="{y}" width="{chart_w}" height="24" rx="4" fill="#E9EEF5"/>')
        body.append(f'  <rect x="{chart_x}" y="{y}" width="{bw:.1f}" height="24" rx="4" fill="{color}" opacity="{1.0 if is_full else 0.78}"/>')
        body.append(f'  <text x="{chart_x+bw+7:.1f}" y="{y+17}" class="small">+{delta:.1f}</text>')

    note_y = 562
    body.extend(
        [
            f'  <text x="{x0}" y="{note_y}" class="small">Caption cue: Ablation on the same dataset and split. Full model improves Acc./F1 while keeping deployment metrics visible.</text>',
            f'  <text x="{x0}" y="{note_y+24}" class="small">Reviewer-risk placeholder: real manuscripts should add repeat definition, variance/CI, and statistical test when claiming significance.</text>',
        ]
    )

    svg = svg_wrap(
        width,
        height,
        "Ablation table with visible engineering cost",
        "Synthetic demo. Component evidence and deployability metrics stay in the same reviewer-facing view.",
        "\n".join(body),
    )
    (FIGURES / "ablation-result-table.svg").write_text(svg, encoding="utf-8")


def write_captions() -> None:
    text = """# Captions and QA Notes

## Robustness SNR Curve

Caption draft: Bit error rate under decreasing SNR. The proposed method shows lower BER than MMSE, CNN, and Transformer baselines across all tested channel conditions, supporting the robustness claim under low-SNR operation.

QA: The x-axis is an engineering operating condition, the y-axis uses a labeled log scale, and marker/line-style redundancy supports grayscale readability.

## Accuracy-Latency Pareto

Caption draft: Accuracy-latency tradeoff for deployment-oriented comparison. The proposed method lies on the Pareto frontier by improving macro-F1 while keeping inference latency lower than larger neural baselines.

QA: The figure makes the cost metric visible, labels both optimization directions, and avoids claiming accuracy improvement without deployment cost.

## Ablation Result Table

Caption draft: Ablation study of the proposed model components. Adding attention, temporal modeling, physics guidance, and augmentation improves accuracy and F1, while the table keeps parameter count and latency visible.

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
    print(f"Wrote refreshed examples under {ROOT}")


if __name__ == "__main__":
    main()
