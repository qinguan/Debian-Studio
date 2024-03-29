#!/usr/bin/python

import unittest
import os
import commands
import GenerateScript

class ScriptTestCase(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_generate_script(self):
        scriptname_test,temp_packages_test = GenerateScript.GenerateScript()
        self.assertEqual(os.path.exists(scriptname_test), True)
        self.assertEqual(os.path.exists(temp_packages_test), True)
        self.assertEqual(commands.getstatusoutput("rm "+ scriptname_test + " " + temp_packages_test)[0],0)
#        os.system("rm " + scriptname_test + " " + temp_packages_test)


if __name__ == '__main__':
    unittest.main()
