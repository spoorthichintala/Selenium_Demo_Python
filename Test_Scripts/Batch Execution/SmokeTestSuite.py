import unittest
# get all tests from SearchText and HomePageTest class
from Test_Scripts.UnitTest_Examples.UnitTest_Decorator.UnitTest_SetUp_TearDown  import SearchText
from Test_Scripts.UnitTest_Examples.UnitTest_Decorator.UnitTest_SetUp_TearDown_Class_Level import OrangeHRM_Login_Logout
from Test_Scripts.UnitTest_Examples.UnitTest_Decorator.UnitTest_Skip_Unless_Example import Test
from Test_Scripts.UnitTest_Examples.UnitTest_Decorator.UnitTest_FirstTest import SimpleTest

search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(OrangeHRM_Login_Logout)
Test1 = unittest.TestLoader().loadTestsFromTestCase(Test)
Simple_test=unittest.TestLoader().loadTestsFromTestCase(SimpleTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text,Test1,Simple_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)