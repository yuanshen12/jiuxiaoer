import logging
from wechat_mall.baseView.baseView import BaseView
import csv
import os,time

#  位置地址参数化
nanning  = '酒小二(南宁站)'
station = '贵阳站'
guiyangzhan = '贵阳站'
guiyang = "贵阳"
nanning = '南宁'

#  搜索参数
seek  = '自动化啤酒'

#  商品参数
wares = '燕京 燕京鲜啤8°鲜行天下高听 500ml 1听'


class Common(BaseView):
    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)