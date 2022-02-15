from wagon_common.helpers.scope import resolve_scope
from wagon_common.helpers.notebook import read_notebook, save_notebook

# correspondance between cli argument and cell data or metadata key name
DATA = dict(
    execution_count="execution_count",
    meta_scrolled="scrolled",
    meta_executetime="ExecuteTime",
    meta_hidden="hidden",
    meta_collapsed="collapsed",
    meta_heading_collapsed="heading_collapsed",
)


def edit_notebook(notebook_content, notebook_path, kwargs, delete_notes=False):
    """set execution count to zero"""

    # select global metadata & challengify metadata
    global_metadata = notebook_content.get("metadata", {})
    challengify = global_metadata.get("challengify", {})

    # clean global metadata
    clean_global_metadata = {}
    notebook_content["metadata"] = clean_global_metadata

    # preserve the challengify conf if it exists
    if "challengify" in global_metadata.keys():
        clean_global_metadata["challengify"] = challengify

    # force the kernel spec
    clean_global_metadata["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    }

    # select data and metadata to clean
    clean_cell_keys = [ DATA[k] for k, v in kwargs.items() if v and k[:5] != "meta_" ]
    clean_meta_keys = [ DATA[k] for k, v in kwargs.items() if v and k[:5] == "meta_" ]

    # iterate through cells in order to apply the policies
    delete_cells = []

    for index, cell in enumerate(notebook_content.get("cells", [])):

        # check if cell must be deleted
        if delete_notes:

            # get cell slide type
            metadata = cell.get("metadata", {})
            slideshow = metadata.get("slideshow", {})
            slide_type = slideshow.get("slide_type", "")

            # test cell type
            if slide_type == "notes":

                # mark cell to be deleted
                delete_cells.append(index)

        # clean cell data
        for key in clean_cell_keys:

            # set key content
            if key in cell:
                cell[key] = None  # execution_count must not be deleted but set to None

        # clean outputs
        for output in cell.get("outputs", []):

            # clean outputs execution_count
            if "execution_count" in output:
                output["execution_count"] = None

            # clean outputs data image trailing newline
            for data_key in output.get("data", {}):
                if data_key[:6] == "image/":
                    output["data"][data_key] = output["data"][data_key].rstrip("\n")

        # clean cell metadata
        if "metadata" in cell:

            for key in clean_meta_keys:

                # delete key
                if key in cell["metadata"]:
                    del cell["metadata"][key]

    # delete flagged cells
    if delete_notes:

        # get cells
        cells = notebook_content.get("cells", [])

        # delete cells in reversed order
        for cell_index in reversed(delete_cells):

            # removing cell
            cells.pop(cell_index)

    # save updated notebook to disk
    save_notebook(notebook_content, notebook_path)


def run_clean(sources, verbose, delete_notes, kwargs):

    # resolve scope
    notebooks = resolve_scope(sources, ["*.ipynb"], verbose=verbose)[0]

    print("\nUpdates:")

    # iterate through notebooks
    for notebook in notebooks:

        # read notebook into a python dictionary
        notebook_content = read_notebook(notebook)

        # update the content of the notebook
        edit_notebook(notebook_content, notebook, kwargs, delete_notes=delete_notes)

        print(f"- {notebook}")
