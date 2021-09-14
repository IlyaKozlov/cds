import abc
import unittest
from typing import List

from flake8.api import legacy as flake8


class StyleTest(unittest.TestCase):

    @abc.abstractmethod
    def get_files(self) -> List[str]:
        pass

    def test_flake(self) -> None:
        """Test that we conform to flake."""
        style_guide = flake8.get_style_guide(ignore=["E501", "W504", "ANN101", "TYP101"], max_line_length=140)
        files = self.get_files()
        errors = style_guide.check_files(files)
        self.assertEqual(0, errors.total_errors)
