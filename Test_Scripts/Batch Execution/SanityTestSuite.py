import unittest
from sndhdr import tests
from unittest import suite


from Test_Scripts.ActionChain_Example.Drag_Drop_Example import DragandDrop
from Test_Scripts.UnitTest_Examples.UnitTest_Decorator.UnitTest_Skip_Unless_Example import Test
from Test_Scripts.UnitTest_Examples.UnitTest_Decorator.UnitTest_SetUp_TearDown_MultipleTest import OrangeHRM_Login_Logout
from UI_Test.OrangeHRM_Text_Title_Url_Verification_Example import Verify_dashboard

name=DragandDrop
dd= unittest.TestLoader().loadTestsFromName(module=DragandDrop().testdd())

#Test1 - Module
Test1=unittest.TestLoader().loadTestsFromTestCase(Test)
Login =unittest.TestLoader().loadTestsFromTestCase(OrangeHRM_Login_Logout)
dashboard =unittest.TestLoader().loadTestsFromTestCase(Verify_dashboard)

#   suite.addTests(tests.loadTestsFromName("get_names_suite.Test_Me.test_Typescript"))

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([Test1,Login,dashboard,dd])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)

