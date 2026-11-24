import os

PART_A = "The bug that disappears when you watch it is not fixed; "
PART_B = "it is only quietly waiting for your demo."
LINE = PART_A + PART_B
assert "\n" not in LINE and len(LINE) == 97


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
