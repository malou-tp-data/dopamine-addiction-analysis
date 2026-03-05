import os
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch


def draw_dopamine_circuit():

    os.makedirs("figures", exist_ok=True)

    fig, ax = plt.subplots(figsize=(12,5), dpi=300)

    ax.set_xlim(0,12)
    ax.set_ylim(0,6)
    ax.axis("off")

    # Colors
    edge = "#1f2d3d"
    brain = "#eef2f7"
    dopamine = "#2563eb"
    hippocampus = "#dcfce7"
    amygdala = "#fee2e2"

    def node(label, x, y, color=brain):

        e = Ellipse((x,y), 1.8,0.9,
                    facecolor=color,
                    edgecolor=edge,
                    lw=2)

        ax.add_patch(e)

        ax.text(x,y,label,
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold")

    # Main nodes
    node("VTA",2,3)
    node("NAcc",6,3)
    node("PFC",10,3)

    # Modulators
    node("Hippocampus",6,5,hippocampus)
    node("Amygdala",6,1,amygdala)

    def arrow(x1,y1,x2,y2,color):

        a = FancyArrowPatch((x1,y1),(x2,y2),
                            arrowstyle="->",
                            mutation_scale=15,
                            lw=2,
                            color=color)

        ax.add_patch(a)

    # Dopamine pathway
    arrow(3,3,5,3,dopamine)
    arrow(7,3,9,3,dopamine)

    ax.text(4,3.35,"dopamine",color=dopamine,ha="center")
    ax.text(8,3.35,"dopamine",color=dopamine,ha="center")

    # Hippocampus modulation
    arrow(6,4.5,6,3.6,"#16a34a")
    ax.text(6,4.2,"context / memory",
            ha="center",
            fontsize=9,
            color="#15803d")

    # Amygdala modulation
    arrow(6,1.5,6,2.4,"#dc2626")
    ax.text(6,1.9,"affect / salience",
            ha="center",
            fontsize=9,
            color="#b91c1c")

    # Title
    ax.text(6,5.6,
            "Mesocorticolimbic Dopaminergic Circuit",
            ha="center",
            fontsize=16,
            fontweight="bold")

    plt.tight_layout()

    plt.savefig("figures/dopamine_circuit.png")
    plt.savefig("figures/dopamine_circuit.svg")

    plt.show()


draw_dopamine_circuit()