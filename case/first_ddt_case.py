# coding=utf-8
import sys
sys.path.append('D:\\Imooc_project')
import ddt
import unittest
import os
import time
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import unittest
import warnings
from util.excel_util import ExcelUtil
# 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息

ex = ExcelUtil()
data = ex.get_data()


@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    ''' 数据驱动 '''
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.register = RegisterBusiness(self.driver)
        self.file_name = 'D:/Imooc_project/yztp/yzm.png'

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:  # self._outcome.errors用于获取案例中的失败
            if error:
                case_name = self._testMethodName  # _testMrthodName用于获取用例名
                file_path = os.path.join(os.path.dirname(
                    os.path.dirname(os.path.realpath(__file__))) + r'\tp' + '\\' + case_name + '.png')  # 报告放的位置
                self.driver.save_screenshot(file_path)
        self.driver.quit()

    '''
    @ddt.data(
        ['12', 'zjq123', '123123', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
        ['@qq.com', 'zjq123', '123123', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
        ['232525@qq.com', 'zjq123', '123123', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    @ddt.unpack  # 如果data中含有多个数据，以元组，列表，字典等数据，需要自行在脚本中对数据进行分解或者使用unpack分解数据。
    def test_register_case(self, email, username, password, code, assertCode, assertText):
        # email, username, password, code, assertCode, assertText = data
        email_error = self.register.register_function(email, username, password, code, assertCode, assertText)
        self.assertFalse(email_error)


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')  # 现在的时间
    file_path = os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))) + r'\report' + '\\' + now + '.html')  # 报告放的位置
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title='test report',
        description='这是一个报告'
    )  # 生成测试报告
    runner.run(suite)
