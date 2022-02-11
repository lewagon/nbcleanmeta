import json
import os
import pytest

from wagon_cleaner.run_clean import run_clean

class TestCleaner:
    def test_input_execution_count_is_null(self):
        src = os.path.join(os.path.dirname(__file__), 'notebooks', 'base.ipynb')
        run_clean([src], False, False, {"all": True})
        with open(src) as src_file:
            src_data = json.load(src_file)
            code_cells = [cell for cell in src_data['cells'] if cell['cell_type'] == 'code']
            for cell in code_cells:
                assert cell['execution_count'] is None

    def test_outputs_execution_count_is_null(self):
        src = os.path.join(os.path.dirname(__file__), 'notebooks', 'base.ipynb')
        run_clean([src], False, False, {"all": True})
        with open(src) as src_file:
            src_data = json.load(src_file)
            code_cells = [cell for cell in src_data['cells'] if cell['cell_type'] == 'code']
            for cell in code_cells:
                assert cell['outputs'][0]['execution_count'] is None
