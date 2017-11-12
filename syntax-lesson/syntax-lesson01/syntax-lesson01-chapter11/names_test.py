import unittest
from name_function import get_formatted_name
from name_function import get_formatted_name2


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_name2_1(self):
        formatted_name = get_formatted_name2("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_name2_2(self):
        formatted_name = get_formatted_name2("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


unittest.main()
