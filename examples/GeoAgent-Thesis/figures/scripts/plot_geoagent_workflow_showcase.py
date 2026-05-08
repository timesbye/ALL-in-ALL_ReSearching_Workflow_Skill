from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    data_path = project_root / "data" / "results.csv"
    output_dir = project_root / "figures" / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_path)

    methods = df["Method"].tolist()
    x = range(len(methods))

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "legend.fontsize": 9,
        }
    )

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.6), constrained_layout=True)

    ax0 = axes[0]
    width = 0.34
    offsets = [-width / 2, width / 2]
    colors = ["#2F5D8C", "#4FA18D"]

    ax0.bar([i + offsets[0] for i in x], df["Accuracy"], width=width, label="Accuracy", color=colors[0])
    ax0.bar([i + offsets[1] for i in x], df["F1"], width=width, label="F1", color=colors[1])
    ax0.set_title("Quality Comparison Across Methods")
    ax0.set_ylabel("Score (%)")
    ax0.set_xticks(list(x))
    ax0.set_xticklabels(methods, rotation=25, ha="right")
    ax0.set_ylim(75, 90)
    ax0.grid(axis="y", linestyle="--", linewidth=0.7, alpha=0.4)
    ax0.legend(frameon=False, loc="upper left")

    ax1 = axes[1]
    ax1.plot(
        df["InferenceLatencyMs"],
        df["Accuracy"],
        marker="o",
        linewidth=2.0,
        markersize=6,
        color="#C7642D",
    )
    for _, row in df.iterrows():
        ax1.annotate(
            row["Method"],
            (row["InferenceLatencyMs"], row["Accuracy"]),
            textcoords="offset points",
            xytext=(4, 5),
            fontsize=8,
        )
    ax1.set_title("Accuracy-Latency Trade-off")
    ax1.set_xlabel("Inference Latency (ms)")
    ax1.set_ylabel("Accuracy (%)")
    ax1.set_xlim(24, 62)
    ax1.set_ylim(81, 89.2)
    ax1.grid(linestyle="--", linewidth=0.7, alpha=0.4)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    png_path = output_dir / "geoagent_workflow_showcase.png"
    pdf_path = output_dir / "geoagent_workflow_showcase.pdf"
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved {png_path}")
    print(f"Saved {pdf_path}")


if __name__ == "__main__":
    main()
