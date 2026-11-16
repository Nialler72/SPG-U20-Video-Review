#!/usr/bin/env python3
"""Export the six original Liam report pages for the SPG review."""
from argparse import ArgumentParser
from pathlib import Path
import fitz

PAGES = [
    (20, "total-kickouts"),
    (18, "kickouts-overview"),
    (26, "balls-lost"),
    (8, "opposition-funnel"),
    (22, "opposition-kickouts"),
    (13, "shots-timeline"),
]

def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Liam's original 28-page match report")
    args = parser.parse_args()
    destination = Path(__file__).resolve().parent / "graphics"
    with fitz.open(args.pdf) as report:
        if len(report) != 28:
            raise ValueError("Expected Liam's 28-page SPG v Na Fianna Og report.")
        destination.mkdir(parents=True, exist_ok=True)
        for number, name in PAGES:
            output = destination / (name + ".png")
            report[number - 1].get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False).save(output)
            print(output)

if __name__ == "__main__":
    main()
