from gendiff import parser_adapter
from gendiff import generate_diff


def main():
    args = parser_adapter()
    generate_diff(args)
