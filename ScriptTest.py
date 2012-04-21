#!/usr/bin/python

import unittest
import os
import generate_script

class ScriptTestCase(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_generate_script(self):
        scriptname,temp_packages = generate_script.generate_script()
        self.assertEqual(os.path.exists(scriptname), True)
        self.assertEqual(os.path.exists(temp_packages), True)
        os.system("rm " + scriptname + " " + temp_packages)


if __name__ == '__main__':
    unittest.main()
