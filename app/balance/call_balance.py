from common.call_wechat import wechat
from common.call_common import Login
from app.home.call_home import Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Balance(Login):
    call_balance_time = (By.ID, "com.callme.mall:id/time")  # 送达时间
    call_balance_ok = (By.ID, "com.callme.mall:id/ok")  # 确定送达时间
    call_balance_locate = (By.ID, "com.callme.mall:id/address")  # 配送地址（选择地址）
    call_balance_use_exist = (By.ID, "com.callme.mall:id/useExist")  # 已有收货地址
    call_balance_range = (By.ID, "com.callme.mall:id/tag_Range")  # 超范围
    call_balance_name = (By.ID, "com.callme.mall:id/name")  # 姓名
    call_balance_phone = (By.ID, "com.callme.mall:id/phone")  # 电话
    call_balance_location = (By.ID, "com.callme.mall:id/location")  # 定位
    call_balance_wechat = (By.ID, "com.callme.mall:id/pay_weixin")  # 微信支付
    call_balance_alipay = (By.ID, "com.callme.mall:id/pay_alipay")  # 支付宝
    call_balance_pay = (By.ID, "com.callme.mall:id/pay_hdfk")  # 货到付款
    call_balance_invoice = (By.ID, "com.callme.mall:id/invoice")  # 发票
    call_balance_coupon = (By.ID, "com.callme.mall:id/coupon")  # 优惠券
    call_balance_integral = (By.ID, "com.callme.mall:id/integral")  # 当前无积分
    call_balance_notes = (By.ID, "com.callme.mall:id/notes")  # 留言
    call_balance_all = (By.ID, "com.callme.mall:id/maney_all")  # 商品总额
    call_balance_promotion = (By.ID, "com.callme.mall:id/maney_promotion")  # 促销金额
    call_balance_money = (By.ID, "com.callme.mall:id/money")  # 应付金额
    call_balance_submit = (By.ID ,"com.callme.mall:id/submit")  # 提交订单

    def balance_time(self):  # 送达时间
        time = self.wait(EC.visibility_of_element_located, self.call_balance_time)
        return time

    def balance_ok(self):  # 确定送达时间
        ok = self.wait(EC.visibility_of_element_located, self.call_balance_ok)
        return ok

    def balance_locate(self):  # 配送地址
        locate = self.wait(EC.visibility_of_element_located, self.call_balance_locate)
        return locate




