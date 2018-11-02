#coding:utf-8
import sys
# import HTMLTestRunner
import unittest2
from caseConfig import CaseConfig
sys.path.append('testCase')
from testCase import bannerTest

# import logging

if __name__ == "__main__":
    print( "---------------------------------------start-----------------------------------------")
    case1 = CaseConfig()
    caseNames = eval(case1.get_case_list())
    testunit = unittest2.TestSuite()
    for i in range(0, len(caseNames)):
        testunit.addTest(unittest2.makeSuite(caseNames[i]))
    runner = unittest2.TextTestRunner()
    runner.run(testunit)

    # m = mail.SendMail()
    # m.send()


