# coding=utf-8
import sys
sys.path.append('D:\\Imooc_project')
import os
import time
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import HTMLTestRunner
import unittest
import warnings


class FirstCase(unittest.TestCase):
    def setUp(self):
        log = UserLog()  # 实例化日志
        logger = log.get_log()  # 获得logger对象
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        logger.info('this is chrome')  # 打印debug级别的日志
        log.close_handle()  # 移除handle
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

    def test_login_email_error(self):
        email_error = self.register.register_email_error('12222fff@163.com', 'test111', '123123', self.file_name)
        self.assertFalse(email_error)

    def test_login_username_error(self):
        name_error = self.register.register_name_error('122fff@163.com', 't', '123123', self.file_name)
        self.assertFalse(name_error)

    def test_login_code_error(self):
        code_error = self.register.register_code_error('122ff@163.com', 'test111', '123123',self.file_name)
        self.assertFalse(code_error)

    def test_login_password_error(self):
        password_error = self.register.register_password_error('122ff@163.com', 'test111', '12', self.file_name)
        self.assertFalse(password_error)


'''
    def test_login_success(self):
        self.register.user_base('122ff@163.com', 'test111', '123123', '11111')
        success = self.register.register_success()
        if success is True:
            print('案例成功')
'''


'''
def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_password_error()
    first.test_login_code_error()
'''


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')  # 现在的时间
    file_path = os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))) + r'\report' + '\\' + now + '.html')  # 报告放的位置
    print(file_path)
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()  # 实例化容器
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_password_error'))
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title='test report',
        description='这是一个报告'
    )  # 生成测试报告
    runner.run(suite)
