import unittest
from csv import CSV
class TestCSV(unittest.TestCase):
    def setUp(self):
        self.a_csv=CSV("C:/Users/ASUS/python_csv_class/demo.csv")
    def test_is_csv(self):
        a_csv=CSV("C:/Users/ASUS/python_csv_class/demo.csv")
        result=self.a_csv.is_csv()
        self.assertTrue(result)
    def test_get_head(self):
        if_head=self.a_csv.get_head()
        self.assertTrue(if_head)
unittest.main()        
