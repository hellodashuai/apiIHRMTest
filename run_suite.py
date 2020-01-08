import time
import unittest
import app
from script.login import Login
from script.test_emp import TestIHRMEmp
from tools.HTMLTestRunner import HTMLTestRunner

# 初始化测试套件
suite = unittest.TestSuite()
# 2 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))
# 3 使用HTMLTestRunner执行测试套件,生成测试报告
report_path = app.BASE_DIR + "/report/ihrm.html"
with open(report_path, mode='wb') as f:
    # 初始化HTML TestRunner
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源接口测试", description="v1.0.0")
    # 使用Runner运行测试套件
    runner.run(suite)
