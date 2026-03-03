"""Entry point for ``python -m mypkg``."""

from mypkg.cli import hello


def main():
    hello()


if __name__ == "__main__":
    main()
