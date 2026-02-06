import argparse
import subprocess
from pathlib import Path


def convert(md_path, output_path, resource_root):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "pandoc",
            str(md_path),
            "-o",
            str(output_path),
            "--resource-path",
            str(resource_root),
        ],
        check=True,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="provas_v3_profissional")
    parser.add_argument("--output", default="provas_v3_profissional/docx")
    args = parser.parse_args()

    input_root = Path(args.input)
    output_root = Path(args.output)

    for md_file in input_root.glob("*_candidato.md"):
        convert(md_file, output_root / f"{md_file.stem}.docx", input_root)
    for md_file in input_root.glob("*_gabarito.md"):
        convert(md_file, output_root / f"{md_file.stem}.docx", input_root)


if __name__ == "__main__":
    main()
