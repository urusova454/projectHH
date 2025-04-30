import unittest
from unittest.mock import MagicMock, patch

import requests

from src.parsers.queries.hh import get_general_vacancy


class TestVacancyApi(unittest.TestCase):

    @patch('src.parsers.queries.hh.requests.requests.get')
    def test_get_generals_vacancies(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'items': [
                '''
                Описать модель items
                '''
            ]
        }