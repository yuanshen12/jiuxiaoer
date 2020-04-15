import xlrd
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def get_excel_data(path, name):
    workbook = xlrd.open_workbook(PATH(path))
    sheet = workbook.sheet_by_name(name)  # 获取工作簿的名字
    rows = sheet.nrows  # 获取数据的行数
    cols = sheet.ncols  # 获取数据列数
    lists = []
    for num_row in range(1, rows):
        list = []
        for num_col in range(cols):
            ctype = sheet.cell(num_row, num_col).ctype
            cell = sheet.cell_value(num_row, num_col)
            if ctype == 2 and cell % 1 == 0.0:
                cell = int(cell)
                cell = str(cell)
            list.append(cell)
        lists.append(list)
    return lists


if __name__ == '__main__':
    data = get_excel_data("../Xls/search.xls", "search")
    print(data)