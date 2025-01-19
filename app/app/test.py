from django.test import SimpleTestCase

from app import calc
from rest_framwork.test import APIClient
class CalcTests(SimpleTestCase):
    
    def test_add_numbers(self):
        '''test add two numbers'''
        res = calc.add(5,6)
        self.assertEqual(res,11)
    
    def test_subtract_numbers(self):
        '''test substract two numbers'''
        res = calc.subtract(10,5)
        self.assertEqual(res, 5)

    def test_get_greetings(self):
        '''Test getting greetings'''
        client = APIClient()
        res = client.get('greetings/')
        self.assertEqual(res.status, 200)
        self.assertEqual(res.data, ["Hello!","Bonhour"])
