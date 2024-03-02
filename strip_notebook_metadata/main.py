# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import sys
import nbformat as nbf

def strip_metadata(input_file):
    """Strip metadata from Jupyter notebooks."""
    with open(input_file, "r", encoding="utf-8") as file:
        notebook = nbf.read(file, as_version=4)

    for cell in notebook['cells']:
        if cell['cell_type'] in ['code', 'markdown']:
            cell['metadata'] = {}

    with open(input_file, "w", encoding="utf-8") as file:
        nbf.write(notebook, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m strip_notebook_metadata <notebook_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    strip_metadata(input_file)
