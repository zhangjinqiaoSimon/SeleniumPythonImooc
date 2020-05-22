# coding=utf-8
import sys
sys.path.append('D:\\Imooc_project')
from util.excel_util import ExcelUtil
from key_word.actionMethod import ActionMethod


class KeywordCase(object):
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil('D:/Imooc_project/config/keyword.xls')
        # get 行数
        case_lines = handle_excel.get_lines()
        if case_lines:
            # for循环，遍历每一行
            for i in range(1, case_lines):
                col_value = handle_excel.get_col_value(i, 3)
                # if 是否执行
                if col_value == 'yes':
                    method = handle_excel.get_col_value(i, 4)  # 操作方法
                    send_value = handle_excel.get_col_value(i, 5)  # 输入值
                    handle_value = handle_excel.get_col_value(i, 6)  # 操作元素
                    except_result_method = handle_excel.get_col_value(i, 7)  # 获取预期结果的方法
                    except_result = handle_excel.get_col_value(i, 8)  # 获取预期结果的值
                    self.run_method(method, send_value, handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)  # 获取预期结果的值（列表）
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')

    def get_except_result_value(self, except_result):
        ''' 获取预期结果值 '''
        return except_result.split('=')

    def run_method(self, method, send_value='', handle_value=''):
        ''' 运行方法 '''
        print(send_value)
        print(handle_value)
        method_value = getattr(self.action_method, method)  # getattr获取一个对象中的方法
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value, handle_value)
        return result


if __name__ == '__main__':
    kc = KeywordCase()
    kc.run_main()

