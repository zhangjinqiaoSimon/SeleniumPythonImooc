# coding=utf-8
import configparser


class ReadIni(object):
    ''' 读取ini文件 '''
    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = 'D:\Imooc_project\config\LocalElement.ini'
        if node is None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        ''' 加载ini文件 '''
        cf = configparser.ConfigParser()  # 实例化
        cf.read(file_name)  # 读取配置文件
        return cf

    def get_value(self, key):
        ''' 获取value '''
        data = self.cf.get(self.node, key)  # 获取RegisterElement下面的user_email的值
        return data


if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value('user_name'))
