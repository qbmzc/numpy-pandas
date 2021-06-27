import xlrd
import xlwt
import xlsxwriter


# 打开excel表格
def openexcel(fname):
    fh = xlrd.open_workbook(fname)
    return fh


# 获取excel中所有的sheet
def getSheet(fh):
    return fh.sheets()


# 获取sheet数
def getSheetNum(fh):
    res = 0
    sh = fh.sheets()
    for sheet in sh:
        res += 1
    return res


# 获取每个sheet的行数
def getNrow(fh, i):
    table = fh.sheets()[i]
    return table.nrows


# 获取每行的元素
def getncols(fh, i):
    table = fh.sheets()[i]
    num = table.nrows
    data = []
    for i in range(num):
        rdata = table.row_values(i)
        data.append(rdata)
    return data


if __name__ == '__main__':
    # 表头数组（根据具体情况选择是否使用）
    excelhead = ["起始时间", "终止时间", "通话时长", "呼入被叫", "呼出主叫"]
    # 表格所在位置
    filelocation = "D:/temp/1/"
    # 表格的后缀即形式
    fileform = "xlsx"
    # 合并后的表格存放的位置
    filedestination = "D:/temp/1/result.xlsx"
    # 从文件夹中读取有多少个文件需要合并
    # 首先查找默认文件夹下有多少文档需要整合
    import os

    filearray1 = os.listdir(filelocation)
    print(filearray1)
    fileNumber = len(filearray1) - 1
    filearray = []
    for i in range(0, fileNumber):
        fway = filelocation + filearray1[i + 1]
        filearray.append(fway)
    print("在" + filelocation + "中有" + str(fileNumber) + "个" + fileform + "文件")
    # 读取数据：rvalue第一重为文件名，第二重为sheet，第三重为行元素，第四重为每个单元格元素
    rvalue = [None] * fileNumber
    for k in range(fileNumber):
        fh = openexcel(filearray[k])
        num = getSheetNum(fh)
        rvalue[k] = ["sheet"] * num
        for i in range(0, num):
            rvalue[k][i] = getncols(fh, i)
    # 存储数据:四层for循环赋值，由内到外：单元格->行->文件->sheet
    import xlrd
    import xlwt
    import xlsxwriter

    res = xlsxwriter.Workbook(filedestination)
    fh = openexcel(filearray[0])
    for w in range(getSheetNum(fh)):
        ws = res.add_worksheet("sheet" + str(w + 1))
        q = -1
        for k in range(fileNumber):
            for i in range(len(rvalue[k][w])):
                q += 1
                for j in range(len(rvalue[k][w][i])):
                    if rvalue[k][w][i][j]:
                        x = rvalue[k][w][i][j]
                        ws.write(q, j, x)
    res.close()
    print("合并成功，合并后的文件所在位置：" + filedestination)
