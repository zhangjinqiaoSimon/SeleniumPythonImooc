# coding=utf-8
from base.find_element import FindElement


class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    def get_email_element(self):  # 获取邮箱元素
        return self.fd.get_element('user_email')

    def get_username_element(self):  # 获取用户名元素
        return self.fd.get_element('user_name')

    def get_password_element(self):  # 获取密码元素
        return self.fd.get_element('password')

    def get_code_element(self):  # 获取验证码元素
        return self.fd.get_element('code_text')

    def get_registerbtn_element(self):  # 获取注册按钮元素
        return self.fd.get_element('register_btn')

    def get_email_error_element(self):  # 获取邮箱报错信息元素
        return self.fd.get_element('user_email_error')

    def get_username_error_element(self):  # 获取用户名报错信息元素
        return self.fd.get_element('user_name_error')

    def get_password_error_element(self):  # 获取密码报错信息元素
        return self.fd.get_element('password_error')

    def get_code_error_element(self):  # 获取密码报错信息元素
        return self.fd.get_element('code_text_error')
