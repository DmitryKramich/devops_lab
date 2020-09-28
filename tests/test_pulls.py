from unittest import TestCase
from handlers import pulls
from tests import testJson


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_get_pulls_all(self):
        """Test checking return value when empty state"""
        self.assertEqual(pulls.get_complited_data(None, testJson.json),
                         testJson.resultAll)

    def test_get_pulls_state(self):
        """Test checking return value when not empty state"""
        self.assertEqual(pulls.get_complited_data("open", testJson.json),
                         testJson.resultOpenAccepted)

    def test_get_data_state(self):
        """Test states"""
        self.assertEqual(pulls.get_data_state(testJson.json, "open"),
                         testJson.resultOpenAccepted)
        self.assertEqual(pulls.get_data_state(testJson.json, "closed"),
                         testJson.resultClosed)

    def test_get_data_labels(self):
        """Test states"""
        self.assertEqual(pulls.get_data_labels(testJson.json, "accepted"),
                         testJson.resultOpenAccepted)
        self.assertEqual(pulls.get_data_labels(testJson.json, "needs work"),
                         testJson.resultNeedWork)

    def test_get_all_data(self):
        """Test get all data"""
        self.assertEqual(pulls.get_all_data(testJson.json),
                         testJson.resultAll)

    def tearDown(self):
        """Finish"""
