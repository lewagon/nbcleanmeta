import json
import os
import pytest
from random import randint

from wagon_cleaner.run_clean import run_clean
from wagon_common.helpers.notebook import read_notebook, save_notebook


class TestCleaner:
    def test_input_execution_count_is_null(self):
        src_path = os.path.join(os.path.dirname(__file__), 'notebooks', 'base.ipynb')
        content = read_notebook(src_path)
        code_cells = [cell for cell in content['cells'] if cell['cell_type'] == 'code']
        for cell in code_cells:
            cell['execution_count'] = randint(1,10)
        save_notebook(content, src_path)
        run_clean([src_path], False, False, {"execution_count": True})
        clean_content = read_notebook(src_path)
        code_cells = [cell for cell in clean_content['cells'] if cell['cell_type'] == 'code']
        for cell in code_cells:
            assert cell['execution_count'] is None
        os.system(f'git checkout HEAD {src_path}')

    def test_outputs_execution_count_is_null(self):
        src_path = os.path.join(os.path.dirname(__file__), 'notebooks', 'base.ipynb')
        content = read_notebook(src_path)
        code_cells = [cell for cell in content['cells'] if cell['cell_type'] == 'code']
        for cell in code_cells:
            cell['execution_count'] = randint(1,10)
        save_notebook(content, src_path)
        run_clean([src_path], False, False, {"execution_count": True})
        clean_content = read_notebook(src_path)
        code_cells = [cell for cell in clean_content['cells'] if cell['cell_type'] == 'code']
        for cell in code_cells:
            if cell.get('outputs', False) and bool(cell['outputs']):
                assert cell['outputs'][0]['execution_count'] is None
        os.system(f'git checkout HEAD {src_path}')
