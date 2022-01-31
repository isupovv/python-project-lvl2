from hexlet_code.argparse import parser_adapter
from hexlet_code.generate_diff import generate_diff


def main():
    args = parser_adapter()
    generate_diff(args)
