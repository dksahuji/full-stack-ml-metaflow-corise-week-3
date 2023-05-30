import re
import argparse


def adapt_file(args):
    with open(args.file, "r") as file:
        result = re.sub(
            f"#\s*@{args.decorator}",
            " ".join([""] * args.nspaces) + f"@{args.decorator}",
            file.read(),
        )
    with open(args.file, "w") as file:
        file.write(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Uncommenter", description="Uncomment a decorator line in a flow."
    )
    parser.add_argument("--file", type=str, help="Local file path")
    parser.add_argument("--decorator", type=str, help="Metaflow decorator name")
    parser.add_argument(
        "--nspaces",
        type=int,
        default=0,
        help="Number of spaces before decorator's @ symbol",
    )
    args = parser.parse_args()
    adapt_file(args)
