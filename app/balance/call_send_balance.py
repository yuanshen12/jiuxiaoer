from app.balance.call_balance import Balance
from app.locate.call_locate import Locate
from common.call_common_app import config_yaml
from selenium.common.exceptions import NoSuchElementException


class SendBalance(Balance):

    def send_balance_ok(self):  # 选择送货时间
        choose = "请选择"
        time = self.balance_time()
        if choose in time.text:
            time.click()
            self.balance_ok().click()

    def send_balance_locate(self):  # 选择配送地址
        data = config_yaml()
        try:
            self.balance_tag().click()
        except NoSuchElementException:
            pass
        else:
            self.balance_locate().click()
            locate_add = Locate(self.driver)
            locate_add.locate_adds(data['name'], data['phone'], data['tablet'], data['tag'], num=2)

    def send_balance_submit(self):  # 选择支付方式并提交订单
        self.swipe(600, 1200, 600, 900, 500)
        self.balance_pay().click()
        self.balance_submit().click()

    def send_balance_go(self):  # 继续逛逛
        go = self.balance_go()
        return go
