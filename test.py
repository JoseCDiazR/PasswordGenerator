from methods import get_data
import unittest

class TestMetodo(unittest.TestCase):
    def test_get_data(self):
        result_1,result_2,result_3,result_4 = get_data("Jose",3,False,True)
        self.assertEquals(result_1,"Jose")
        self.assertEquals(result_2,3)
        self.assertEquals(result_3,0)
        self.assertEquals(result_4,1)

