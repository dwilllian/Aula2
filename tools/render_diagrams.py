import argparse
import json
import subprocess
from pathlib import Path

NODE_STYLE = "rounded,filled"
FILL_COLORS = ["#E8EEF9", "#E7F6F2", "#F9F3E8", "#F4E8F9", "#E8F9EC"]


def render_diagram(spec, output_path):
    nodes = spec["nodes"]
    edges = spec["edges"]

    lines = [
        "digraph G {",
        "  graph [rankdir=LR, splines=ortho, fontname=\"Liberation Sans\", fontsize=10, bgcolor=\"white\"];",
        "  node [shape=rect, style=\"rounded,filled\", fontname=\"Liberation Sans\", fontsize=10, penwidth=1.2, color=\"#4A4A4A\"];",
        "  edge [color=\"#5A5A5A\", penwidth=1.1, arrowsize=0.7];",
    ]

    for i, node in enumerate(nodes):
        color = FILL_COLORS[i % len(FILL_COLORS)]
        label = node["label"].replace("\n", "\\n")
        lines.append(f"  {node['id']} [label=\"{label}\", fillcolor=\"{color}\"]; ")

    for src, dst in edges:
        lines.append(f"  {src} -> {dst};")

    lines.append("}")

    dot_content = "\n".join(lines)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dot_path = output_path.with_suffix(".dot")
    dot_path.write_text(dot_content, encoding="utf-8")

    subprocess.run(["dot", "-Tpng", str(dot_path), "-o", str(output_path)], check=True)
    dot_path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="provas_v3_profissional/specs")
    parser.add_argument("--output", default="provas_v3_profissional/assets/diagrams")
    args = parser.parse_args()

    specs_root = Path(args.input)
    output_root = Path(args.output)

    for spec_file in specs_root.glob("*.json"):
        data = json.loads(spec_file.read_text(encoding="utf-8"))
        exam = data["exam"]
        for diagram in data["diagrams"]:
            q_index = diagram["question"]
            output_path = output_root / exam / f"q{q_index:02d}.png"
            render_diagram(diagram["spec"], output_path)


if __name__ == "__main__":
    main()
