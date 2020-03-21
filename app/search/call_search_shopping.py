from common.call_common import Login
from app.home.call_home import Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchShopping(Login):
    call_search_price = (By.ID, "com.callme.mall:id/price")  # 商品价格
    call_search_add = (By.ID, "com.callme.mall:id/add")  # 商品添加到购物车
    call_search_title = (By.ID, "com.callme.mall:id/text_title")  # 商品标题
    call_search_content = (By.ID, "com.callme.mall:id/content")  # 商品规格
    call_search_vi_add = (By.ID, "com.callme.mall:id/iv_add")  # 增加数量
    call_search_submit = (By.ID, "com.callme.mall:id/submit")  # 加入购物车
    call_search_go_submit = (By.ID, "com.callme.mall:id/gosubmit")  # 立即购买

    def search_shopping_price(self):  # 商品价格
        price = self.wait(EC.visibility_of_element_located, self.call_search_price)
        return price

    def search_shopping_add(self):  # 商品添加购物车
        add = self.wait(EC.visibility_of_element_located, self.call_search_add)
        return add

    def search_shopping_title(self):  # 商品标题
        title = self.wait(EC.visibility_of_element_located, self.call_search_title)
        return title

    def search_shopping_content(self):  # 商品规格
        content = self.wait(EC.visibility_of_element_located, self.call_search_content)
        return content

    def search_shopping_submit(self):  # 商品立即购买
        submit = self.wait(EC.visibility_of_element_located, self.call_search_go_submit)
        return submit

    def search_shopping_submit_cart(self):  # 加入购物车
        cart = self.wait(EC.visibility_of_element_located, self.call_search_submit)
        return cart
    

