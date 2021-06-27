# lib
import os
import xlrd
import xlsxwriter

# 在下方输入需要合并的文件所在文件夹位置
path = 'D:/temp/1/'
# 在下方输入合并后Excel的路径和文件名
work = xlsxwriter.Workbook('D:/temp/2/output.xlsx')
# 新建一个sheet
sheet = work.add_worksheet('combine')

file_list = os.listdir(path)
file_list.sort()

# Main
file_name = ''
x1 = 1
x2 = 1
fileNum = len(file_list)
print("在该目录下有%d个xlsx文件" % fileNum)
for file in file_list:
    if '1' in file:  # 此处需要修改！
        file_name = os.path.join(path, file)
    else:
        continue
    print(file_name)
    workbook = xlrd.open_workbook(file_name)
    sheet_name = workbook.sheet_names()

    for file_1 in sheet_name:
        print(file_1)
        table = workbook.sheet_by_name(file_1)
        rows = table.nrows
        clos = table.ncols

        for i in range(rows):
            print(x1)
            sheet.write_row('A' + str(x1), table.row_values(i))
            x1 += 1

    print('正在合并第%d个文件 ' % x2)
    print('已完成 ' + file_name)
    x2 += 1

print("已将%d个文件合并完成" % fileNum)
print(x1)
work.close()