# coding=utf-8
from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    ''' 执行操作 '''
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, name, password, filename):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(filename)
        self.register_h.click_register_btn()

    def register_success(self):
        success = self.register_h.get_register_text()
        if success is None:
            print('注册成功')
            return True
        else:
            return False

    def register_email_error(self, email, name, password, filename):  # 邮箱错误
        self.user_base(email, name, password, filename)
        if self.register_h.get_user_text('user_email_error', '请输入有效的电子邮件地址') is None:
            return True
        else:
            return False

    def register_name_error(self, email, name, password, filename):  # 用户名错误
        self.user_base(email, name, password, filename)
        if self.register_h.get_user_text('user_name_error', '字符长度必须大于等于4，一个中文字算2个字符') is None:
            return True
        else:
            return False

    def register_password_error(self, email, name, password, filename):  # 密码错误
        self.user_base(email, name, password, filename)
        if self.register_h.get_user_text('password_error', '最少需要输入 5 个字符') is None:
            return True
        else:
            return False

    def register_code_error(self, email, name, password, filename):  # 验证码错误
        self.user_base(email, name, password, filename)
        if self.register_h.get_user_text('code_error', '验证码错误') is None:
            return True
        else:
            return False

    def register_function(self, email, username, password, code, assertCode, assertText):
        self.user_base(email, username, password, code)
        if self.register_h.get_user_text(assertCode, assertText) is None:
            return True
        else:
            return False
