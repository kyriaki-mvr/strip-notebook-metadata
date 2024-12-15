![PyPI - Version](https://img.shields.io/pypi/v/strip-notebook-metadata?color=green)

# Strip Notebook Metadata
A package to strip metadata from code cells and markdowns without editing the output in Jupyter notebooks.

A simple, effective tool for cleaning metadata from Jupyter notebooks. This package helps in reducing the size of notebooks and removing potentially sensitive information stored in metadata, making notebooks cleaner for version control and sharing.

Pypi.org: https://pypi.org/project/strip-notebook-metadata/

## Features

- **Simple Command-Line interface**: Easy to use, run it directly from your terminal.
- **Cleans metadata**: Strips out metadata from both code and markdown cells.
- **Supports Jupyter Notebooks**: Works with `.ipynb` files, the standard Jupyter notebook format.

## Installation

Install `strip-notebook-metadata` using pip:

```bash
pip install strip-notebook-metadata
```

## Dependencies

- sys
- nbformat

## Usage

To strip metadata from a Jupyter notebook, run:

```bash
strip-notebook-metadata path/to/your_notebook.ipynb
```

Replace `path/to/your_notebook.ipynb` with the actual path to the notebook you wish to clean.

To add it under your pre-commit hooks, add the following under your **pre-commit-config.yaml**:
```
-   repo: https://github.com/kyriaki-mvr/strip-notebook-metadata
    rev: v0.2.0
    hooks:
    -   id: strip-notebook-metadata
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## Feedback

If you have any feedback, please file an issue on the GitHub repository page. I am always looking to improve and appreciate all feedback, bug reports, and suggestions.

## License

This project is licensed under the GPL License - see the LICENSE file for details.

## Authors

- Kyriaki Mavropoulou (kyriaki@quanterra.gr) - Initial work

## First release
02-March-2024
