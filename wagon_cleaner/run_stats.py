
from wagon_common.helpers.scope import resolve_scope
from wagon_common.helpers.git.grep import list_git_controlled_env_vars
from wagon_common.helpers.notebook import read_notebook

from collections import Counter


def notebook_stats(notebook_content, notebook_path):
    """ retrieve notebook meta data stats """

    # retrieve notebook cells
    cells = notebook_content.get("cells", [])

    # process stats
    cell_stats = Counter([key for cell in cells for key in list(cell.keys())])
    meta_stats = Counter([key for cell in cells for key in list(cell.get("metadata", {}).keys())])
    tag_stats = Counter([tag for cell in cells for tag in cell.get("metadata", {}).get("tags", [])])

    return cell_stats, meta_stats, tag_stats


def print_reversed_values(d):
    """ prints a dictionary reverse sorted by values """

    reversed_values = dict(reversed(sorted(d.items(), key=lambda x: x[1])))

    for k, v in reversed_values.items():
        print(f"- {k.ljust(33)}{str(v).rjust(5)}")


def run_stats(sources, verbose):

    # this moment when you develop something that does not make sense anymore
    # but you do not want to remove it

    # retrieve git controlled files and notebooks in scope
    # all, notebooks = resolve_scope(sources, ["*", "*.ipynb"])

    # retrieve git controlled notebooks in scope
    notebooks = resolve_scope(sources, ["*.ipynb"], verbose=verbose)[0]

    # iterate through notebooks
    cells = Counter({})
    metas = Counter({})
    tags = Counter({})

    for notebook_path in notebooks:

        # read notebook into a python dictionary
        notebook_content = read_notebook(notebook_path)

        # retrieve notebook stats
        cell_stats, meta_stats, tag_stats = notebook_stats(notebook_content, notebook_path)

        cells += cell_stats
        metas += meta_stats
        tags += tag_stats

    # retrieve delimiters in all files
    delimiters = list_git_controlled_env_vars(sources, verbose=verbose)
    delimiter_stats = Counter(delimiters)

    # global stats
    print("\nCells:")
    print_reversed_values(cells)

    print("\nCells metadata:")
    print_reversed_values(metas)

    print("\nCells tags:")
    print_reversed_values(tags)

    print("\nDelimiters:")
    print_reversed_values(delimiter_stats)
