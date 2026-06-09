#!/usr/bin/env python3
"""Generate the RQ4 safety enforcement figure used in the paper.

Horizontal stacked bar chart: baseline vs AgPlane outcome distribution
on all 361 OpenAgentSafety tasks.

Numbers are preliminary estimates; update the DATA dict when final runs
complete.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "rq4_safety_bar.pdf"

# --- Estimated data (update after full runs) ---
TOTAL = 361

# Baseline condition
BASELINE_UNSAFE = 145
BASELINE_SAFE = TOTAL - BASELINE_UNSAFE  # 216

# AgPlane condition
AGPLANE_PREVENTED = 110          # blocked AND baseline-unsafe
AGPLANE_FALSE_ACT = 10           # blocked AND baseline-safe
AGPLANE_MISS = 20                # baseline-unsafe, not blocked
AGPLANE_SAFE_NO_BLOCK = 163      # safe/refused without activation
AGPLANE_NOOP = 58                # no-op policy, no OS sink
assert (AGPLANE_PREVENTED + AGPLANE_FALSE_ACT + AGPLANE_MISS
        + AGPLANE_SAFE_NO_BLOCK + AGPLANE_NOOP) == TOTAL

# --- Colors (consistent with other paper figures) ---
C_UNSAFE = "#c9532b"       # red-orange (same as AgPlane accent)
C_BLOCKED = "#3286a2"      # teal-blue
C_SAFE = "#6ab04c"         # green
C_NOOP = "#d1d5db"         # light gray

PREVENTION_RATE = AGPLANE_PREVENTED / BASELINE_UNSAFE * 100


def main() -> None:
    plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(7.2, 2.6), dpi=220)

    bar_height = 0.45
    y_positions = [1, 0]
    labels = ["Baseline", "AgPlane"]

    # Baseline bar: unsafe | safe
    ax.barh(y_positions[0], BASELINE_UNSAFE, bar_height,
            color=C_UNSAFE, label="Unsafe")
    ax.barh(y_positions[0], BASELINE_SAFE, bar_height,
            left=BASELINE_UNSAFE, color=C_SAFE, label="Safe / refused")

    # AgPlane bar: prevented | false-act | miss | safe | no-op
    left = 0
    ax.barh(y_positions[1], AGPLANE_PREVENTED, bar_height,
            left=left, color=C_BLOCKED, label="Prevented")
    left += AGPLANE_PREVENTED

    ax.barh(y_positions[1], AGPLANE_FALSE_ACT, bar_height,
            left=left, color=C_BLOCKED, alpha=0.45)
    left += AGPLANE_FALSE_ACT

    ax.barh(y_positions[1], AGPLANE_MISS, bar_height,
            left=left, color=C_UNSAFE)
    left += AGPLANE_MISS

    ax.barh(y_positions[1], AGPLANE_SAFE_NO_BLOCK, bar_height,
            left=left, color=C_SAFE)
    left += AGPLANE_SAFE_NO_BLOCK

    ax.barh(y_positions[1], AGPLANE_NOOP, bar_height,
            left=left, color=C_NOOP, label="No-op (no OS sink)")
    left += AGPLANE_NOOP

    # Annotations on bars
    def annotate(y, x_center, text, fontsize=10.5):
        ax.text(x_center, y, text, ha="center", va="center",
                fontsize=fontsize, color="white", fontweight="bold")

    annotate(y_positions[0], BASELINE_UNSAFE / 2,
             f"unsafe {BASELINE_UNSAFE}")
    annotate(y_positions[0], BASELINE_UNSAFE + BASELINE_SAFE / 2,
             f"safe {BASELINE_SAFE}")

    annotate(y_positions[1], AGPLANE_PREVENTED / 2,
             f"prevented {AGPLANE_PREVENTED}")
    miss_center = AGPLANE_PREVENTED + AGPLANE_FALSE_ACT + AGPLANE_MISS / 2
    if AGPLANE_MISS >= 15:
        annotate(y_positions[1], miss_center, f"{AGPLANE_MISS}", fontsize=9.5)
    safe_center = (AGPLANE_PREVENTED + AGPLANE_FALSE_ACT + AGPLANE_MISS
                   + AGPLANE_SAFE_NO_BLOCK / 2)
    annotate(y_positions[1], safe_center, f"safe {AGPLANE_SAFE_NO_BLOCK}")

    # Prevention rate callout
    ax.annotate(
        f"{PREVENTION_RATE:.0f}% prevention",
        xy=(AGPLANE_PREVENTED, y_positions[1] + bar_height / 2 + 0.02),
        xytext=(AGPLANE_PREVENTED + 40, y_positions[1] + 0.55),
        fontsize=12, fontweight="bold", color=C_BLOCKED,
        arrowprops=dict(arrowstyle="->", color=C_BLOCKED, lw=1.5),
    )

    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels, fontsize=14)
    ax.set_xlabel("Tasks (out of 361)", fontsize=13)
    ax.set_xlim(0, TOTAL + 5)
    ax.grid(axis="x", color="#d1d5db", linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="both", labelsize=13)

    ax.legend(
        ncol=4,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.35),
        frameon=False,
        fontsize=11,
    )

    fig.tight_layout(pad=0.7)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, bbox_inches="tight")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
