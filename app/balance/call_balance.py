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
    call_balance_submit = (By.ID, "com.callme.mall:id/submit")  # 提交订单

    def balance_time(self):  # 送达时间
        time = self.wait(EC.visibility_of_element_located, self.call_balance_time)
        return time

    def balance_ok(self):  # 确定送达时间
        ok = self.wait(EC.visibility_of_element_located, self.call_balance_ok)
        return ok

    def balance_locate(self):  # 配送地址
        locate = self.wait(EC.visibility_of_element_located, self.call_balance_locate)
        return locate

    def balance_wechat(self):  # 选择微信支付
        weixin = self.wait(EC.visibility_of_element_located, self.call_balance_wechat)
        return weixin

    def balance_alipay(self):  # 选择支付宝
        alipay = self.wait(EC.visibility_of_element_located, self.call_balance_alipay)
        return alipay

    def balance_pay(self):  # 选择货到付款
        pay = self.wait(EC.visibility_of_element_located, self.call_balance_pay)
        return pay

    def balance_invoice(self):  # 选择发票
        invoice = self.wait(EC.visibility_of_element_located, self.call_balance_invoice)
        return invoice

    def balance_coupon(self):  # 选择优惠券
        coupon = self.wait(EC.visibility_of_element_located, self.call_balance_coupon)
        return coupon

    def balance_integral(self):  # 当前无积分
        integral = self.wait(EC.visibility_of_element_located, self.call_balance_integral)
        return integral

    def balance_notes(self):  # 留言
        notes = self.wait(EC.visibility_of_element_located, self.call_balance_notes)
        return notes

    def balance_all(self):  # 商品总额
        all_one = self.wait(EC.visibility_of_element_located, self.call_balance_all)
        return all_one

    def balance_promotion(self):  # 促销金额
        promotion = self.wait(EC.visibility_of_element_located, self.call_balance_promotion)
        return promotion

    def balance_money(self):  # 应付金额
        money = self.wait(EC.visibility_of_element_located, self.call_balance_money)
        return money

    def balance_submit(self):  # 提交订单
        submit = self.wait(EC.visibility_of_element_located, self.call_balance_submit)
        return submit




