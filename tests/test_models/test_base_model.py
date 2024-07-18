#!/usr/bin/bash

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def test_create_model(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        model_json = my_model.to_dict

        

        # self.assertEquals(print(my_model),"gkgk")

if __name__ == "__main__":
    unittest.main()

