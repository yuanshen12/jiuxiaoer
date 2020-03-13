from common.call_wechat import wechat
from common.call_common import Login
from app.home.call_home import Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.call_common import config_yaml
import appium


class Search(Login):
    call_back = (By.ID, "com.callme.mall:id/back")  # 搜索页面返回
    call_content = (By.ID, "com.callme.mall:id/content")  # 搜索页面输入（包含热门搜索，历史记录）
    call_content_name = (By.ID, "com.callme.mall:id/name")  # 搜索页面确定
    call_clean = (By.ID, "com.callme.mall:id/clean_history")  # 搜索页面删除历史
    call_number = (By.ID, "com.callme.mall:id/number")  # 购物车角标
    call_shopping_cart = (By.ID, "com.callme.mall:id/shoppingCart")  # 购物车
    call_money = (By.ID, "com.callme.mall:id/money")  # 所在购物车价钱
    call_settlement = (By.ID, "com.callme.mall:id/settlement")  # 去结算

    def search_back(self):  # 搜索页面返回
        back = self.wait(EC.visibility_of_element_located, self.call_back)
        return back

    def search_content(self, stat=0, num=0):  # 搜索页面输入(初始是输入框，从1开始点热门，历史搜索）
        data = config_yaml()
        content = self.driver.find_elements(*self.call_content)
        if stat == 0:
            content[num].send_keys(data['search'])
        else:
            content[num].click()

    def search_content_name(self, num=0):  # 搜索页面确定
        content_name = self.wait(EC.visibility_of_any_elements_located, self.call_content_name)[num]
        return content_name

    def search_clean(self):  # 搜索页面清空历史记录
        clean = self.wait(EC.visibility_of_element_located, self.call_clean)
        return clean

    def search_number(self):  # 购物车角标(可获得商品数量）
        number = self.wait(EC.visibility_of_element_located, self.call_number)
        return number

    def search_cart(self):  # 购物车
        cart = self.wait(EC.visibility_of_element_located, self.call_shopping_cart)
        return cart

    def search_money(self):  # 加入购物车金额
        money = self.wait(EC.visibility_of_element_located, self.call_money)
        return money

    def search_settlement(self):
        self.wait(EC.visibility_of_element_located, self.call_settlement)


if __name__ == '__main__':
    driver = wechat()
    search = Search(driver)
    search.search_content()
    search.search_content_name().click()


