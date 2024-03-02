# strip_notebook_metadata/__main__.py
from .main import strip_metadata
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m strip_notebook_metadata <notebook_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    strip_metadata(input_file)
