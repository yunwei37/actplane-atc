#!/usr/bin/env python3
"""Generate the OctoBench RQ3 reward figure used in the paper."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "octobench_rq3.png"

METRICS = [
    "Official\nreward",
    "User-query\nreward",
    "Impl/test\nreward",
    "Compliance\nreward",
]

SERIES = {
    "Baseline": [0.80, 0.43, 0.42, 0.90],
    "Claude Code hooks": [0.81, 0.41, 0.40, 0.92],
    "AgPlane": [0.84, 0.53, 0.52, 0.93],
}

COLORS = {
    "Baseline": "#9aa1aa",
    "Claude Code hooks": "#3286a2",
    "AgPlane": "#c9532b",
}


def main() -> None:
    x = np.arange(len(METRICS))
    width = 0.24

    plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(7.2, 3.5), dpi=220)

    offsets = {
        "Baseline": -width,
        "Claude Code hooks": 0,
        "AgPlane": width,
    }

    for name, values in SERIES.items():
        xpos = x + offsets[name]
        ax.bar(xpos, values, width, label=name, color=COLORS[name])
        for xi, yi in zip(xpos, values):
            ax.text(xi, yi + 0.012, f"{yi:.2f}", ha="center", va="bottom", fontsize=10.5)

    ax.set_ylabel("Reward", fontsize=14)
    ax.set_ylim(0, 1.04)
    ax.set_xticks(x)
    ax.set_xticklabels(METRICS)
    ax.grid(axis="y", color="#d1d5db", linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="both", labelsize=13)
    ax.legend(
        ncol=3,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.22),
        frameon=False,
        fontsize=13,
    )

    fig.tight_layout(pad=0.7)
    fig.savefig(OUT, bbox_inches="tight")


if __name__ == "__main__":
    main()
