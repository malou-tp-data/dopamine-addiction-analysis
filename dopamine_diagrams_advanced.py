# dopamine_diagrams_advanced.py
# Clean hybrid diagram: VTA → NAcc → PFC (thin arrows, centered, publication-style)

import os
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

def draw_hybrid_clean(out_png="figures/dopamine_pathway_hybrid_clean.png",
                      out_svg="figures/dopamine_pathway_hybrid_clean.svg"):
    # --- Canvas ---
    fig, ax = plt.subplots(figsize=(12, 5), dpi=200)
    ax.set_axis_off()
    ax.set_xlim(-1, 11)   # margins left/right
    ax.set_ylim(-2.5, 2.5)  # margins top/bottom

    # --- Colors & style ---
    node_face = "#dfe9ff"
    node_edge = "#254a91"
    arrow_color = "#1c2b3a"   # thin, sober
    text_color = "#0e1726"

    # --- Node geometry ---
    W, H = 2.2, 3.0   # ellipse width/height
    y0 = 0.0
    x_vta, x_nacc, x_pfc = 0.5, 5.5, 10.5

    # --- Helper to add node ---
    def node(x, y, label):
        e = Ellipse((x, y), width=W, height=H, facecolor=node_face,
                    edgecolor=node_edge, linewidth=2.0)
        ax.add_patch(e)
        ax.text(x, y, label, ha="center", va="center",
                fontsize=18, color=text_color, weight="bold")

    # --- Nodes ---
    node(x_vta,  y0, "VTA")
    node(x_nacc, y0, "NAcC")
    node(x_pfc,  y0, "PFC")

    # --- Arrows (thin & clean) ---
    def arrow(x0, x1, y=0.0):
        # start/end just outside ellipse edges for perfect touching
        start = x0 + W/2 - 0.05
        end   = x1 - W/2 + 0.05
        arr = FancyArrowPatch((start, y), (end, y),
                              arrowstyle='-|>', mutation_scale=14,
                              linewidth=2.0, color=arrow_color,
                              shrinkA=0, shrinkB=0)
        ax.add_patch(arr)

    arrow(x_vta,  x_nacc, y0)
    arrow(x_nacc, x_pfc,  y0)

    # --- Small mechanistic notes (subtle, not cluttered) ---
    ax.text(x_nacc, 1.55, "Cocaine (DAT block)\n→ direct ↑ dopamine in NAcC",
            ha="center", va="bottom", fontsize=11, color=text_color)
    ax.text(x_vta, -1.9, "Cannabis (CB1)\n→ indirect ↑ dopamine in NAcC",
            ha="center", va="top", fontsize=11, color=text_color)

    # --- Title (clean) ---
    fig.suptitle("Minimal Dopaminergic Pathway  •  VTA → NAcC → PFC",
                 fontsize=16, color=text_color, y=0.96, weight="bold")

    # --- Save ---
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.92])
    fig.savefig(out_png, bbox_inches="tight", facecolor="white")
    fig.savefig(out_svg, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"✅ Saved:\n- {out_png}\n- {out_svg}")

if __name__ == "__main__":
    draw_hybrid_clean()
