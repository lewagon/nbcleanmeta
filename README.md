
# install

from gemfury with `~/.pip/pip.conf`:

``` bash
pip install wagon_common
pip install nbcleanmeta
```

from gemfury with index url:

``` bash
pip install wagon_common --extra-index-url https://$GEMFURY_PULL_TOKEN@pypi.fury.io/ssaunier
pip install nbcleanmeta --extra-index-url https://$GEMFURY_PULL_TOKEN@pypi.fury.io/ssaunier
```

from github:

``` bash
pip install git+ssh://git@github.com/lewagon/python-utilities.git
pip install git+ssh://git@github.com/lewagon/nbcleanmeta.git
```

# uninstall

``` bash
pip uninstall -y nbcleanmeta
pip uninstall -y wagon_common
```

# aliases

``` bash
alias nbc="nbcleanmeta $@"
```

# about

clean notebook cell data and metadata in order to maintain clear git diffs

# usage

## clean

clean data and metadata of the cells of the notebooks within the provided scope

``` bash
nbcleanmeta run                         # clean all notebooks in current directory tree
nbcleanmeta run sources                 # clean individual notebooks and directory trees
nbcleanmeta run --help                  # list options
```

processed cell data:
- `execution_count` (set to 0)

deleted cell metadata:
- `scrolled`
- `ExecuteTime`
- `hidden`
- `collapsed`
- `heading_collapsed`

## stats

return stats on cell data, metadata and tags used in the notebooks within the provided scope

return stats on delimiters used in the files and notebooks within the provided scope

``` bash
nbcleanmeta stats                       # retrieve stats on current directory tree
nbcleanmeta stats sources               # retrieve stats on individual files and directory trees
nbcleanmeta stats --help                # list options
```

## convert

this is deprecated and has been replaced by [challengify](https://github.com/lewagon/utils/tree/master/challengify)

converts a solutions notebook into a challenges notebook by removing all the cells with slide type set to notes (additionally to cleaning the notebook)

``` bash
nbcleanmeta run --delete-notes notebook.ipynb  # do not use
```
