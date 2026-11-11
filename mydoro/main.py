import argparse
from mydoro.app import main
from mydoro import __version__


def positive_int(value):
    """Parse a CLI duration/count, rejecting zero and negative values."""
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError(
            f"expected a positive integer, got {value}"
        )
    return number


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="MyDoro - A modern Pomodoro timer for your terminal"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"MyDoro {__version__}"
    )
    parser.add_argument("--pomodoro", type=positive_int, help="Pomodoro duration (minutes)")
    parser.add_argument("--short-break", type=positive_int, help="Short break duration (minutes)")
    parser.add_argument("--long-break", type=positive_int, help="Long break duration (minutes)")
    parser.add_argument("--cycles", type=positive_int, help="Cycles before long break")
    parser.add_argument(
        "--theme", 
        choices=["dracula", "monokai", "github_dark", "github_light"],
        help="App theme"
    )
    
    return parser.parse_args()


def main_cli():
    args = parse_arguments()
    main(args)


if __name__ == "__main__":
    main_cli()
