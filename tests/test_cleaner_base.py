import pytest

import os

from random import randint

from wagon_common.helpers.notebook import read_notebook, save_notebook


class TestCleanerBase:

    @pytest.fixture
    def notebook_path(self):
        # Arrange
        src_path = os.path.join(os.path.dirname(__file__), 'notebooks', 'base.ipynb')
        self._mix_up_execution_count(src_path)

        # Act & Assert
        yield src_path

        # Cleanup
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
