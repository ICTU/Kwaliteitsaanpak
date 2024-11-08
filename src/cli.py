"""Command-line interface argument parser."""

import argparse


def parse_cli_arguments() -> argparse.Namespace:
    """Parse the command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "settings",
        nargs="+",
        help="One or more JSON settings files that specify the conversion options",
    )
    parser.add_argument("--version", help="Document version", default="wip")
    parser.add_argument(
        "--log",
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="log level (default: %(default)s)",
    )
    return parser.parse_args()
