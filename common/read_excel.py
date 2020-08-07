import os
from common import getpathInfo
from xlrd import open_workbook

# 拿到该项目所在的绝对路径
path = getpathInfo.get_base_path()


class ReadExcel(object):

    # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
    @staticmethod
    def get_xls(xls_name, sheet_name):
        cls = []

        # 获取用例文件路径
        xls_path = os.path.join(path, "testFile", 'case', xls_name)

        # 打开用例Excel
        file = open_workbook(xls_path)

        # 获得打开Excel的sheet
        sheet = file.sheet_by_name(sheet_name)

        # 获取这个sheet内容行数
        nrows = sheet.nrows

        # 根据行数做循环
        for i in range(nrows):
            # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':

    # 我们执行该文件测试一下是否可以正确获取Excel中的值
    print(ReadExcel.get_xls('userCase.xlsx', 'login'))
    # print(ReadExcel.get_xls('userCase.xlsx', 'login')[0][1])
    print(ReadExcel.get_xls('user03Case.xlsx', 'login')[1][2])
    x = ReadExcel.get_xls('user03Case.xlsx', 'login')[1][2]
    print(type(x))
