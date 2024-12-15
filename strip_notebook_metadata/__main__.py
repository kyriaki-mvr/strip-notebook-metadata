import sys
from .main import strip_metadata

def main():
    if len(sys.argv) < 2:
        print("Usage: strip-notebook-metadata <notebook_file> [<notebook_file> ...]")
        sys.exit(1)
    for nb_file in sys.argv[1:]:
        strip_metadata(nb_file)
    return 0

if __name__ == "__main__":
    sys.exit(main())
