import json
import os
import pytest
from random import randint

from wagon_cleaner.run_clean import run_clean
from wagon_common.helpers.notebook import read_notebook, save_notebook


class TestCleanerExecutionCount:
    def test_input_execution_count_is_null(self):
        # Set up test
        src_path = os.path.join(os.path.dirname(__file__), 'notebooks', 'base.ipynb')
        self._mix_up_execution_count(src_path)
        run_clean([src_path], False, False, {"execution_count": True})

        # Perform test
        clean_content = read_notebook(src_path)
        code_cells = self._get_code_cells(clean_content)
        for cell in code_cells:
            assert cell['execution_count'] is None

        # Tear down test
        self._get_base_nb_back(src_path)

    def test_outputs_execution_count_is_null(self):
        # Set up test
        src_path = os.path.join(os.path.dirname(__file__), 'notebooks', 'base.ipynb')
        self._mix_up_execution_count(src_path)
        run_clean([src_path], False, False, {"execution_count": True})

        # Perform test
        clean_content = read_notebook(src_path)
        code_cells = self._get_code_cells(clean_content)
        for cell in code_cells:
            if cell.get('outputs', False) and bool(cell['outputs']):
                assert cell['outputs'][0]['execution_count'] is None

        # Tear down test
        self._get_base_nb_back(src_path)

    def _get_code_cells(self, content):
        return [cell for cell in content['cells'] if cell['cell_type'] == 'code']

    def _mix_up_execution_count(self, src_path):
        content = read_notebook(src_path)
        code_cells = self._get_code_cells(content)
        for cell in code_cells:
            cell['execution_count'] = randint(1, 10)
        save_notebook(content, src_path)

    def _get_base_nb_back(self, src_path):
        os.system(f'git checkout HEAD {src_path}')
