# conding=utf-8
from util.read_ini import ReadIni


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        ''' 定位元素 '''
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]  # 字符串用'>'符号分割开来
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:  # 如果没定位到元素，返回None
            return None
