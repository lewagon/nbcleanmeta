from tests.test_cleaner_base import TestCleanerBase

from wagon_cleaner.run_clean import run_clean
from wagon_common.helpers.notebook import read_notebook


class TestCleanerOutputs(TestCleanerBase):

    def test_outputs_data_trailing_newline_is_present(self, notebook_path):
        """
        # test that newlines are present when no action is performed
        """
        # Act
        # no action is performed

        # Assert
        clean_content = read_notebook(notebook_path)
        code_cells = self._get_code_cells(clean_content)
        for cell in code_cells:
            for output in cell.get('outputs', []):
                for data_key in output.get('data', {}):
                    if data_key[:10] == 'image/png':
                        assert output['data'][data_key][-1:] == '\n'

    def test_outputs_data_trailing_newline_is_removed(self, notebook_path):
        # Act
        run_clean([notebook_path], False, False, {})

        # Assert
        clean_content = read_notebook(notebook_path)
        code_cells = self._get_code_cells(clean_content)
        for cell in code_cells:
            for output in cell.get('outputs', []):
                for data_key in output.get('data', {}):
                    if data_key[:10] == 'image/png':
                        assert output['data'][data_key][-1:] != '\n'
