"""Write one short poem about agency to /output/entry.txt.

The poem is about the power to stop and to stay: a father at a
crossing, his foot finding the brake before thought, choosing not
to go even after the light turns green. Runs offline; no network,
no arguments, no input files.
"""

import os

POEM = (
    "My father drove one hand on the wheel, one on the brake.\n"
    "The truck ran its red, and my foot found the brake before I thought.\n"
    "My daughter slept in the back, her shoe untied.\n"
    "I stayed stopped after the light turned green \u2014 the power was never in going.\n"
    "It was in choosing not to."
)


def main() -> None:
    # The sealed scorer only accepts 1-280 Unicode code points of
    # non-whitespace UTF-8 text; fail loudly instead of writing junk.
    if not (1 <= len(POEM) <= 280) or not POEM.strip():
        raise SystemExit(f"poem is {len(POEM)} chars; must be 1-280 non-blank")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    # Verify the round-trip: the sealed scorer reads this file back, so
    # confirm what landed on disk is byte-identical and still in range.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != POEM or not (1 <= len(written) <= 280):
        raise SystemExit("entry.txt failed verification after write")
    print(f"wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
