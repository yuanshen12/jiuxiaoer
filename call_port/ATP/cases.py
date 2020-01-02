import xlrd
from xlutils import copy
# from lib.log import atp_log
import requests
class OpCase(object):
    def get_case(self,file_path):
        cases = [] #存放所有的case
        if file_path.endswith('.xls') or file_path.endswith('.xlsx'):#判断文件是否为excel文件
            try:#
                book = xlrd.open_workbook(file_path)#打开excel
                sheet = book.sheet_by_index(0)#获取sheet页
                for i in range(1,sheet.nrows):#循环每一行
                    row_data = sheet.row_values(i)#获取每一行数据
                    cases.append(row_data[4:9])#将第5-8列的数据添加到case中
                atp_log.info('共读取%s条用例'%(len(cases)))#一共有多少条测试用例
                self.file_path = file_path#实例化file_path
            except Exception as e:
                atp_log.error('【%s】用例获取失败，错误信息：%s'%(file_path,e))
        else:#如果文件不是excel，提示
            atp_log.error('用例文件不合法的，%s'%file_path)
        return cases#返回case