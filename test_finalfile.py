import deepdiff
import unittest
from finalfile import *
#target = __import__("final.py") 

class Testing(unittest.TestCase):
    def test_1(self):
        with open('1.json', 'r') as f:
            b = json.load(f)
        
        with open('1.json', 'r') as f:
            a = json.load(f)
        self.assertEqual(b,a)

    def test_2(self):
        a=123
        b=234
        self.assertTrue(type(a)==type(b))
        
    def test_3(self):
        my_dict = {'name': 'John', 1: [2, 4, 3]}
        his_dict = {'name': 'John', 1: [2, 4, 3]}
        self.assertTrue(compare_dict(my_dict,his_dict))
        
    def test_4(self):
        my_dict = {'name': 'John', 1: [2, 4, 3]}
        his_dict = {'name': 'John', 1: [6, 4, 3]}
        self.assertFalse(compare_dict(my_dict,his_dict))
    
    def test_5(self):
        thislist = ["apple", "banana", "cherry"]
        thatlist = ["mango", "banana", "cherry"]    
        self.assertNotEqual(thislist,thatlist)
        
    def test_6(self):
        thislist = ["apple", "banana", "cherry"]
        thatlist = ["apple", "banana", "cherry"]    
        self.assertEqual(thislist,thatlist) 
    
    def test_7(self):
        x = isinstance(5, int)
        self.assertTrue(x) 
        
    def test_8(self):
        thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }      
        thatdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
        self.assertDictEqual(thisdict,thatdict)
        
    def test_9(self):
        py1_list = ['a', 'e', 'i', 'o', 'u']
        py2_list = ['e', 'a', 'u', 'o', 'i']
        self.assertEquals(py1_list,ordered(py2_list)) 
        
    def test_10(self):
        x={"PowerControl": [{"PowerConsumedWatts": "N/A", "Status": {"Health": "OK", "State": "Enabled"}}], "PowerSupplies": [{"LineInputVoltage": "N/A", "MemberId": "1", "PowerCapacityWatts": "800", "Status": {"Health": "OK", "State": "Enabled"}}, {"LineInputVoltage": "N/A", "MemberId": "2", "PowerCapacityWatts": "800", "Status": {}}]}              
        y={'PowerControl': [{'PowerConsumedWatts': 'N/A', 'Status': {'Health': 'OK', 'State': 'Enabled'}}], 'PowerSupplies': [{'LineInputVoltage': 'N/A', 'MemberId': '1', 'PowerCapacityWatts': '800', 'Status': {'Health': 'OK', 'State': 'Enabled'}}, {'LineInputVoltage': 'N/A', 'MemberId': '2', 'PowerCapacityWatts': '800', 'Status': {}}]}
        self.assertEqual(print(y),(print(json.dumps(x,sort_keys='True'))))
    
    def test_11(self):
        x = '{ "name":"John", "age":30, "city":"New York"}'
        y ={'name': 'John', 'age': 30, 'city': 'New York'}
        self.assertEqual(print(y),print(json.loads(x)))
        
    def test_12(self):
        y ={'name': 'John', 'age': 30, 'city': 'New York'}  
        z ={'name': 'John', 'age': 30, 'city': 'New York'}
        self.assertTrue((str(compare_obj(y, z))))
    
    def test_13(self):
        thislist = ["apple", "banana","mango" "cherry"]
        thatlist = ["apple", "grapes", "cherry"]
        self.assertFalse(compare_list(thislist,thatlist))
        
        
        
    def test_14(self):
        self.testdata = open('finalfile.py').read()
           
        

if __name__ == '__main__':
    unittest.main()
