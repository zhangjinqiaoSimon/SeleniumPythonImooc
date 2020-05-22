# coding=utf-8
import xlrd
from xlutils.copy import copy


class ExcelUtil(object):
    ''' 操作excel '''
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = 'D:/Imooc_project/config/casedata.xls'
        else:
            self.excel_path = excel_path
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)  # 打开excel
        self.table = self.data.sheets()[index]  # 获得指定的sheet

    def get_data(self):  # 获取excel数据, 每一行为一个list
        result = []
        rows = self.get_lines()
        if rows is not None:
            for i in range(rows):
                col = self.table.row_values(i)  # 获得一行的数据
                result.append(col)
        else:
            return None

    def get_lines(self):  # 获取行数
        rows = self.table.nrows  # nrows:获取总行数
        if rows >= 1:
            return rows
        return None

    def get_col_value(self, row, col):  # 获取单元格数据
        if self.get_lines() > row:
            data = self.table.cell(row, col).value  # 注意，行、列都是以0开始
            return data
        else:
            return None

    def write_value(self, row, value):  # 写入数据
        read_value = xlrd.open_workbook('D:/Imooc_project/config/keyword.xls')
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save('D:/Imooc_project/config/keyword.xls')


if __name__ == '__main__':
    ex = ExcelUtil('D:/Imooc_project/config/keyword.xls')
    print(ex.write_value(7, 'test'))
