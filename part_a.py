#!/usr/bin/env python3
import sys
import importlib.util
import string


def load_maze_generator(file_path):
    spec = importlib.util.spec_from_file_location("a2", file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    raise ImportError("Could not load a2.py (maze generator). Check file path.")


def get_labels(length):
    symbols = list(string.digits + string.ascii_uppercase)
    return [symbols[i % len(symbols)] for i in range(length)]


def print_maze_with_labels(maze_lines):
    height = len(maze_lines)
    width = len(maze_lines[0]) if maze_lines else 0

    col_labels = get_labels(width)
    row_labels = get_labels(height)

    print("   " + "".join(col_labels))
    for i, line in enumerate(maze_lines):
        print(f"{row_labels[i]:>2} {line}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 part_a.py <rows> <cols>")
        sys.exit(1)

    try:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
    except ValueError:
        print("Rows and columns must be integers.")
        sys.exit(1)

    a2_file = "a2.py"
    maze_module = load_maze_generator(a2_file)

    maze = maze_module.create_maze(rows, cols)
    if isinstance(maze, str):
        maze_lines = maze.splitlines()
    else:
        maze_lines = maze

    print_maze_with_labels(maze_lines)


if __name__ == "__main__":
    main()
