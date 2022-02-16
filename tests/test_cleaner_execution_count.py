from tests.test_cleaner_base import TestCleanerBase

from wagon_cleaner.run_clean import run_clean
from wagon_common.helpers.notebook import read_notebook


class TestCleanerExecutionCount(TestCleanerBase):

    def test_input_execution_count_no_clean(self, notebook_path):
        """
        # test that exec count integers are present when no action is performed
        """
        # Act
        # no action is performed

        # Assert
        clean_content = read_notebook(notebook_path)
        code_cells = self._get_code_cells(clean_content)
        for cell in code_cells:
            assert type(cell['execution_count']) == int
            if cell.get('outputs', []):
                if 'execution_count' in cell['outputs'][0]:
                    assert type(cell['outputs'][0]['execution_count']) == int

    def test_input_execution_count_is_null(self, notebook_path):
        # Act
        run_clean([notebook_path], False, False, {"execution_count": True})

        # Assert
        clean_content = read_notebook(notebook_path)
        code_cells = self._get_code_cells(clean_content)
        for cell in code_cells:
            assert cell['execution_count'] is None

    def test_outputs_execution_count_is_null(self, notebook_path):
        # Act
        run_clean([notebook_path], False, False, {"execution_count": True})

        # Assert
        clean_content = read_notebook(notebook_path)
        code_cells = self._get_code_cells(clean_content)
        for cell in code_cells:
            if cell.get('outputs', []):
                if 'execution_count' in cell['outputs'][0]:
                    assert cell['outputs'][0]['execution_count'] is None
