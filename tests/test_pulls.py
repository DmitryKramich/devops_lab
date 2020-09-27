from unittest import TestCase
from handlers import pulls
from tests import testJson


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_get_pulls_all(self):
        """Test checking return value when empty state"""
        self.assertEqual(pulls.get_pulls(None), testJson.resultAll)

    def test_get_pulls_state(self):
        """Test checking return value when not empty state"""
        self.assertEqual(pulls.get_pulls("open"), testJson.resultOpenAccepted)

    def test_get_git_json(self):
        """Test data received"""
        self.assertTrue(pulls.get_git_json())

    def test_get_data_state(self):
        """Test states"""
        self.assertEqual(pulls.get_data_state(testJson.json, "open"), testJson.resultOpenAccepted)
        self.assertEqual(pulls.get_data_state(testJson.json, "closed"), testJson.resultClosedNeedWork)

    def test_get_data_labels(self):
        """Test states"""
        self.assertEqual(pulls.get_data_labels(testJson.json, "accepted"), testJson.resultOpenAccepted)
        self.assertEqual(pulls.get_data_labels(testJson.json, "needs work"), testJson.resultClosedNeedWork)

    def test_get_all_data(self):
        """Test get all data"""
        self.assertEqual(pulls.get_all_data(testJson.json), testJson.resultAll)

    def tearDown(self):
        """Finish"""
