from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Base.BaseXlm import get_excel_data
import selenium.common.exceptions
from Base.BaseRunner import TestCase
from Base.BaseElement import Element
from time import sleep
from Base.BaseElement import Element


class Home(TestCase):
    call_locate = (By.ID, "com.callme.mall:id/tv_site_name")  # 首页定位
    call_seek = (By.ID, "com.callme.mall:id/et_search")  # 首页搜索
    call_carousel = (By.ID, "com.callme.mall:id/bannerViewPager")  # 首页轮播图
    call_handpick = (By.ID, "com.callme.mall:id/ll_icon")  # 首页酒类
    call_action = (By.ID, "com.callme.mall:id/ll_icon_2")  # 首页酒类下活动
    call_hours = (By.ID, "com.callme.mall:id/tv_business_hours")  # 首页营业通知
    call_hour = (By.ID, "com.callme.mall:id/tv_announce_info")  # 首页通知
    call_activity = (By.CLASS_NAME, "android.widget.Image")  # 首页活动
    call_handpicks = (By.CLASS_NAME, "android.support.v7.app.ActionBar$Tab")  # 首页酒类二
    call_title = (By.ID, "com.callme.mall:id/tv_title")  # 首页商品标题
    call_tag = (By.ID, "com.callme.mall:id/tv_price")  # 首页商品优惠后
    call_tags = (By.ID, "com.callme.mall:id/tv_old_price")  # 首页商品优惠前
    call_class = (By.CLASS_NAME, "android.widget.TextView")  # 首页酒类筛选
    call_img = (By.ID, "com.callme.mall:id/iv_wine")  # 首页商品图片
    call_add = (By.ID, "com.callme.mall:id/iv_add")  # 首页商品购物车
    call_cart = (By.ID, "com.callme.mall:id/rl_cart")  # 首页购物车
    call_more = (By.ID, "com.callme.mall:id/seeMore")  # 首页查看更多
    call_ad = (By.ID, "com.callme.mall:id/close")  # 去掉广告
    call_address = (By.ID, "com.callme.mall:id/station")  # 定位切换区域
    call_seeks = (By.ID, "com.callme.mall:id/content")  # 定位搜索区域

    def __init__(self, driver):
        self.driver = driver

    def wait(self, choose, display):  # 显示等待
        try:
            wait = WebDriverWait(self.driver, 20, 0.3).until(choose(display))
        except selenium.common.exceptions.TimeoutException:
            print("---查找元素超时---")
            sleep(2)
            return False
        except selenium.common.exceptions.NoSuchElementException:
            sleep(2)
            print("---查找元素不存在---")
            return False
        except selenium.common.exceptions.ElementNotVisibleException:
            sleep(2)
            print("---选择元素未能选中")
            return False
        except selenium.common.exceptions.StaleElementReferenceException:
            print("---页面元素发生了变化---")
            return False
        except selenium.common.exceptions.WebDriverException:
            print("---WebDriver出问题了")
            return False
        return wait

    def home_locate(self):  # 首页定位
        self.element = Element(None).get_element("../Xls/locate.xls")

        # list = get_col()
        # for x in list:
        #     pass
            # self.wait(EC.visibility_of_element_located, ("id", x)).click()

        # locate = self.wait(EC.visibility_of_element_located, self.call_locate)
        # print(locate)
        # if locate is False:
        #     print("--执行--")
        #     self.wait(EC.visibility_of_element_located, self.call_ad).click()
        # print("--执行1--")
        # locate.click()

        # print(res["result"])
        # if res["result"] is False:
        # self.wait(EC.visibility_of_element_located, self.call_ad).click()
            # self.wait(EC.visibility_of_element_located, self.call_locate).click()

        # print("---操作步骤---")


if __name__ == '__main__':
    name = Home(None)
    name.home_locate()
