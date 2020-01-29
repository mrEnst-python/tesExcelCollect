print('Hello, World')
import openpyxl as xlrd

rb = xlrd.load_workbook('./file.xlsx')
sheet = rb
.get_active_sheet
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
for c_el in row:
    print(c_el)
