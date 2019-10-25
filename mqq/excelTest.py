#引入读取excel的库
import xlrd

#打开指定的文件
excel_path = r'D:\interfaceTest\testFile\case\userCase.xlsx'
workbook = xlrd.open_workbook(excel_path)

#定位sheet
sheetname = workbook.sheet_by_name(u'login')

#读取列表中的数据
cellvalue = sheetname.cell_value(0,0)
print(cellvalue)