from selenium import webdriver
from selenium.webdriver.common.by import By
from wechat_test.common.common_fun import Common
import time

class Reduced_web(Common):

    csv_file='../data/account.csv'  # 参数路径

    activity_a = (By.ID,"userName")  # 选择用户名
    activity_b = (By.ID,'password')  # 输入密码
    activity_c = (By.ID,'randCode')  # 输验证码
    activity_d = (By.ID,'but_login')  # 登录
    activity_e = (By.LINK_TEXT,'商城管理')  # 商城管理
    activity_f = (By.LINK_TEXT,'活动')  # 活动
    activity_g = (By.LINK_TEXT,'满减满赠')  # 满减满赠
    activity_h = (By.XPATH,'//*[@id="content-main"]/iframe[2]')  # 进入满减满赠的iframe
    activity_j = (By.LINK_TEXT,'单品促销')  # 单品促销
    activity_k = (By.LINK_TEXT,'折扣促销')  # 折扣促销
    activity_l = (By.LINK_TEXT,'优惠券')  # 优惠券
    activity_z = (By.LINK_TEXT,'加价购')  # 加价购
    activity_v = (By.LINK_TEXT,'录入')  # 录入
    activity_n = (By.XPATH,'//*[@id="textfield-1016-inputEl"]')  # 活动名称
    activity_m = (By.XPATH,'/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')  # 进入满减满赠的iframe
    activity_q = (By.LINK_TEXT,'编辑')  # 编辑
    activity_w = (By.XPATH,'//*[@id="datagrid-row-r1-1-0"]/td[2]/div')  # 选择
    activity_r = (By.ID,'combobox-1017-inputEl')  # 输入满减满赠
    activity_t = (By.ID,'combobox-1018-inputEl')  # 输入活动站点
    activity_y = (By.ID,'textfield-1019-inputEl')  # 输入广告语
    activity_u = (By.ID,'datetimefield-1020-trigger-picker')  # 选择开始时间
    activity_i = (By.LINK_TEXT,'当前时间')  # 确定当前时间
    activity_o = (By.ID,'datetimefield-1021-trigger-picker')  # 选择结束时间
    activity_p = (By.XPATH,'//*[@id="ext-element-2"]/div[6]/div/table/tbody/tr[6]/td[7]')  # 确定结束时间
    activity_s = (By.ID,'numberfield-1052-inputEl')  # 优惠门槛
    activity_qq = (By.ID,'combobox-1053-inputEl')  # 优惠门槛
    activity_ww = (By.XPATH,'//*[@id="ext-element-2"]/div[9]/div/ul/li[2]')  # 优惠方式
    activity_ee = (By.ID,'checkbox-1056-displayEl')  # 优惠积分
    activity_rr = (By.ID,'numberfield-1057-inputEl')  # 优惠方式
    activity_tt = (By.ID,'button-1092-btnInnerEl')  # 添加商品
    activity_yy = (By.ID,'textfield-1159-inputEl')  # 输入查询条件
    activity_uu = (By.LINK_TEXT,'查询')  # 点击查询
    activity_ii = (By.XPATH,'//*[@id="gridview-1138-record-86"]/tbody/tr/td[5]/div/a/span')  # 选择参加活动
    activity_oo = (By.LINK_TEXT,'确定')  # 点击确定
    activity_pp = (By.LINK_TEXT,'提交')  # 确定提交
    activity_x = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[12]/div')  # 活动名称

    activity_aa = (By.ID,"checkbox-1060-displayEl")  # 优惠成长值
    activity_ss = (By.ID,"numberfield-1061-inputEl")  # 优惠成长值
    activity_dd = (By.ID,"checkbox-1064-displayEl")  # 优惠优惠券
    activity_ff = (By.ID,"combobox-1065-inputEl")  # 优惠优惠券类型
    activity_gg = (By.ID,"boundlist-1100")  # 优惠优惠券确定类型
    activity_hh = (By.ID,"numberfield-1066-inputEl")  # 优惠优惠券张数
    activity_jj = (By.ID,"checkbox-1069-displayEl")  # 优惠赠品
    activity_kk = (By.ID,"combobox-1070-inputEl")  # 优惠赠品选择
    activity_ll = (By.ID,"numberfield-1072-inputEl")  # 优惠赠品数量
    activity_zz = (By.ID,"checkbox-1074-inputEl")  # 优惠满减
    activity_xx = (By.ID,"combobox-1075-trigger-picker")  # 优惠满减选择
    activity_vv = (By.XPATH,"//*[@id='boundlist-1100-listEl']/li[2]")  # 优惠选择打折
    activity_cc = (By.ID,"numberfield-1076-inputEl")  # 优惠选择金额
    activity_ad = (By.ID,'checkbox-1029-displayEl')  # 赠品为零时自动下架
    activity_ac = (By.LINK_TEXT,'商品')  # 商品
    activity_ab = (By.LINK_TEXT,'赠品管理')  # 赠品
    activity_ae = (By.XPATH,'//*[@id="content-main"]/iframe[3]')  # 赠品页面
    activity_af = (By.CLASS_NAME,'inuptxt')  # 赠品input
    activity_ag = (By.LINK_TEXT,'查询')  # 赠品查询
    activity_ah = (By.CLASS_NAME,'datagrid-btable')  # 赠品编辑
    activity_aj = (By.LINK_TEXT,'编辑')  # 赠品编辑
    activity_ak = (By.XPATH,'/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')  # 赠品编辑
    activity_al = (By.XPATH,'//*[@id="formobj"]/table/tbody/tr[5]/td[2]/input[2]')  # 赠品编辑为零
    activity_az = (By.ID,'availableQuantitySetting')  # 赠品编辑为零
    activity_ax = (By.CLASS_NAME,'ui_state_highlight')  # 赠品编辑为零
    activity_av = (By.XPATH,'//*[@id="formobj"]/table/tbody/tr[5]/td[2]/input[1]')  # 赠品编辑为不限
    activity_an = (By.ID,'checkbox-1031-displayEl')  # 仅限新用户参与
    activity_am = (By.LINK_TEXT,'删除')  # 删除活动
    activity_ao = (By.LINK_TEXT,'确定')  # 删除确定




    def activity(self,num):
        data = Common.get_csv_data(self, self.csv_file, 8)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(data[1])
        self.driver.implicitly_wait(30)
        try:
            self.driver.find_element(*self.activity_a).send_keys(data[5])
            self.driver.find_element(*self.activity_b).send_keys(data[3])
            self.driver.find_element(*self.activity_c).send_keys(data[4])
            self.driver.find_element(*self.activity_d).click()
        except:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(data[1])
            self.driver.implicitly_wait(30)
            self.driver.find_element(*self.activity_a).send_keys(data[5])
            self.driver.find_element(*self.activity_b).send_keys(data[3])
            self.driver.find_element(*self.activity_c).send_keys(data[4])
            self.driver.find_element(*self.activity_d).click()
        self.driver.find_element(*self.activity_e).click()
        self.driver.find_element(*self.activity_f).click()
        element = self.driver.find_element(*self.activity_e)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if num == 0:
            self.driver.find_element(*self.activity_g).click()
        elif num == 1:
            self.driver.find_element(*self.activity_j).click()
        elif num == 2:
            self.driver.find_element(*self.activity_k).click()
        elif num == 3:
            self.driver.find_element(*self.activity_l).click()
        elif num == 4:
            self.driver.find_element(*self.activity_z).click()

    def comm(self,num):
        self.activity(0)
        iframe = self.driver.find_element(*self.activity_h)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*self.activity_w).click()
        if num == 0:
            self.driver.find_element(*self.activity_v).click()
        elif num == 1:
            self.driver.find_element(*self.activity_q).click()
        self.driver.switch_to.default_content()
        iframe1 = self.driver.find_element(*self.activity_m)
        self.driver.switch_to.frame(iframe1)

    def reduced(self,num):
        if num == 0:
            self.comm(0)
            self.reduced_a()
            self.driver.find_element(*self.activity_pp).click()
            self.driver.quit()
        elif num == 1:
            self.comm(1)
            time.sleep(1)
            try:
                self.driver.find_element(*self.activity_ss).click()
            except:
                self.driver.find_element(*self.activity_ee).click()
                self.driver.find_element(*self.activity_aa).click()
                self.driver.find_element(*self.activity_ss).send_keys(21)
            self.driver.find_element(*self.activity_pp).click()
            time.sleep(3)
            self.driver.quit()
        elif num == 2:
            self.comm(1)
            time.sleep(1)
            try:
                self.driver.find_element(*self.activity_hh).click()
            except:
                self.driver.find_element(*self.activity_aa).click()
                time.sleep(1)
                self.driver.find_element(*self.activity_dd).click()
                time.sleep(2)
                self.driver.find_element(*self.activity_ff).send_keys("自动化红酒卷")
                time.sleep(3)
                self.driver.find_element(*self.activity_hh).send_keys(1)
            self.driver.find_element(*self.activity_pp).click()
            time.sleep(3)
            self.driver.quit()
        elif num == 3:
            self.comm(1)
            time.sleep(1)
            try:
                self.driver.find_element(*self.activity_ll).click()
            except:
                self.driver.find_element(*self.activity_dd).click()
                time.sleep(1)
                self.driver.find_element(*self.activity_jj).click()
                time.sleep(1)
                self.driver.find_element(*self.activity_kk).send_keys("奥丁格酒杯")
                time.sleep(2)
                self.driver.find_element(*self.activity_ll).send_keys(1)
            self.driver.find_element(*self.activity_pp).click()
            time.sleep(3)
            self.driver.quit()
        elif num == 4:
            self.comm(1)
            time.sleep(1)
            try:
                self.driver.find_element(*self.activity_cc).click()
            except:
                self.driver.find_element(*self.activity_jj).click()
                huodongbiaoqian = self.driver.find_element(*self.activity_r)
                huodongbiaoqian.clear()
                huodongbiaoqian.send_keys("满减")
                self.driver.find_element(*self.activity_zz).click()
                self.driver.find_element(*self.activity_cc).send_keys(100)
            self.driver.find_element(*self.activity_pp).click()
            time.sleep(3)
            self.driver.quit()
        elif num == 5:
            self.comm(1)
            time.sleep(1)
            try:
                self.driver.find_element(*self.activity_vv).click()
            except:
                self.driver.find_element(*self.activity_xx).click()
                time.sleep(2)
                self.driver.find_element(*self.activity_vv).click()
                self.driver.find_element(*self.activity_cc).clear()
                self.driver.find_element(*self.activity_cc).send_keys(5)
            self.driver.find_element(*self.activity_pp).click()
            time.sleep(3)
            self.driver.quit()
        elif num == 6:
            self.comm(1)
            time.sleep(1)
            self.driver.find_element(*self.activity_ad).click()
            self.driver.find_element(*self.activity_zz).click()
            self.driver.find_element(*self.activity_jj).click()
            self.driver.find_element(*self.activity_kk).send_keys("奥丁格酒杯")
            time.sleep(2)
            self.driver.find_element(*self.activity_ll).send_keys(1)
            self.driver.find_element(*self.activity_pp).click()
            self.reduced_b(0)
            time.sleep(3)
            self.driver.quit()
        elif num == 7:
            self.comm(1)
            time.sleep(2)
            self.driver.find_element(*self.activity_ad).click()
            self.driver.find_element(*self.activity_pp).click()
            time.sleep(3)
            self.driver.quit()
        elif num == 8:
            self.comm(1)
            time.sleep(2)
            self.driver.find_element(*self.activity_an).click()
            self.driver.find_element(*self.activity_pp).click()
            self.reduced_b(1)
            time.sleep(3)
            self.driver.quit()
        elif num == 9:
            self.comm(1)
            time.sleep(2)
            self.driver.find_element(*self.activity_pp).click()
            self.driver.switch_to.default_content()
            iframe = self.driver.find_element(*self.activity_h)
            self.driver.switch_to.frame(iframe)
            time.sleep(2)
            self.driver.find_element(*self.activity_am).click()
            self.driver.find_element(*self.activity_ao).click()
            time.sleep(3)
            self.driver.quit()

    def reduced_a(self):
        data = Common.get_csv_data(self, self.csv_file, 9)
        self.driver.find_element(*self.activity_n).send_keys(data[1])
        self.driver.find_element(*self.activity_r).send_keys("满赠")
        self.driver.find_element(*self.activity_t).send_keys("贵阳")
        self.driver.find_element(*self.activity_y).send_keys("自动化切换")
        time.sleep(1)
        self.driver.find_element(*self.activity_u).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_i).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_o).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_p).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_s).send_keys(2)
        time.sleep(1)
        self.driver.find_element(*self.activity_qq).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_ww).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_ee).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_rr).send_keys(21)
        time.sleep(1)
        self.driver.find_element(*self.activity_tt).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_yy).send_keys("自动化红酒")
        time.sleep(1)
        self.driver.find_element(*self.activity_uu).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_ii).click()
        time.sleep(1)
        self.driver.find_element(*self.activity_oo).click()
        time.sleep(3)

    def reduced_b(self,num=()):
            self.driver.find_element(*self.activity_ac).click()
            self.driver.find_element(*self.activity_ab).click()
            iframe = self.driver.find_element(*self.activity_ae)
            self.driver.switch_to.frame(iframe)
            self.driver.find_element(*self.activity_af).send_keys("奥丁格酒杯")
            time.sleep(1)
            self.driver.find_element(*self.activity_ag).click()
            time.sleep(1)
            self.driver.find_element(*self.activity_ah).click()
            self.driver.find_element(*self.activity_aj).click()
            self.driver.switch_to.default_content()
            iframe1 = self.driver.find_element(*self.activity_ak)
            self.driver.switch_to.frame(iframe1)
            if num == 0:
                self.driver.find_element(*self.activity_al).click()
                self.driver.find_element(*self.activity_az).clear()
                self.driver.find_element(*self.activity_az).send_keys(0)
            elif num == 1:
                self.driver.find_element(*self.activity_av).click()
            self.driver.switch_to.default_content()
            self.driver.find_element(*self.activity_ax).click()


class Item(Reduced_web):
    csv_file = '../data/account.csv'  # 参数路径
    item_a = (By.XPATH, "//*[@id='page-wrapper']/div[3]/iframe[2]")  # 切换到单品促销页面
    item_b = (By.XPATH, "//*[@id='singleProductPromotionListtb']/div[2]/span[1]/a[1]")  # 添加商品
    item_c = (By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe")  # 切换到添加商品iframe
    item_d = (By.ID, 'textfield-1042-inputEl')  # 在商品名称输入
    item_e = (By.ID, 'button-1045-btnInnerEl')  # 点击查询
    item_f = (By.LINK_TEXT, '选中')  # 在列表选择参加活动的商品
    item_g = (By.LINK_TEXT, '提交')  # 点击提交
    item_h = (By.LINK_TEXT, '是')  # 确认提交
    item_j = (By.CLASS_NAME, 'ace_button')  # 在单品促销页面点击设置或者价格
    item_k = (By.XPATH, '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')  # 切换到设置页面iframe
    item_l = (By.ID, 'activityDate')  # 选择活动日期
    item_z = (By.XPATH, '//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[3]/td[3]')  # 选择开始时间
    item_x = (By.XPATH, '//*[@id="layui-laydate1"]/div[2]/div[2]/table/tbody/tr[3]/td[3]')  # 选择结束时间
    item_v = (By.CLASS_NAME, 'laydate-btns-confirm')  # 选择生效时段
    item_n = (By.XPATH, "//*[@id='formobj']/section/article[3]/aside[3]/div/aside/div[3]/div/input")  # 点击生效时段
    item_m = (By.XPATH, '//*[@id="formobj"]/section/article[3]/aside[3]/div/aside/div[3]/dl/dd[15]')  # 选择生效时段
    item_q = (By.CLASS_NAME, 'ui_state_highlight')  # 提交活动

    # 设置
    item_sa = (By.CLASS_NAME, 'layui-icon-ok')  # 仅限新用户
    item_sb = (By.CLASS_NAME, 'layui-form-radio')  # 仅限会员

    # 价格
    item_ja = (By.XPATH, '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')  # 切换到价格页面
    item_jb = (By.ID, 'discount')  # 按折扣优惠算
    item_jc = (By.CLASS_NAME,'layui-icon')  # 按活动价算
    item_jd = (By.ID,'activityPriceShow')  # 按输入活动价
    item_je = (By.CLASS_NAME,'ui_state_highlight')  # 确定

    # 生效
    item_sx = (By.ID, 'switch')



    def item(self,num):  # 活动用例集合
        self.activity(1)
        if num == 0:
            self.item_01()
            self.item_02(0)
            self.item_03(0)
        elif num == 2:
            self.item_02(0)
            self.item_03(0)
        time.sleep(5)

    def item_01(self):  # 添加单品促销活动商品
        time.sleep(2)
        iframe = self.driver.find_element(*self.item_a)
        self.driver.switch_to.frame(iframe)  # 切换到单品页面
        self.driver.find_element(*self.item_b).click()
        self.driver.switch_to.default_content()
        time.sleep(3)
        iframe1 = self.driver.find_element(*self.item_c)
        self.driver.switch_to.frame(iframe1)   # 切换到单品添加商品
        time.sleep(1)
        self.driver.find_element(*self.item_d).send_keys("自动化啤酒")
        self.driver.find_element(*self.item_e).click()
        time.sleep(2)
        self.driver.find_elements(*self.item_f)[0].click()
        time.sleep(1)
        self.driver.find_element(*self.item_g).click()
        time.sleep(1)
        self.driver.find_element(*self.item_h).click()

    def item_02(self,num):  # 设置单品促销活动商品
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element(*self.item_a)
        self.driver.switch_to.frame(iframe)  # 切换到单品页面
        time.sleep(2)
        self.driver.find_elements(*self.item_j)[1].click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        iframe2 = self.driver.find_element(*self.item_k)
        self.driver.switch_to.frame(iframe2)  # 切换到单品页面的设置
        self.driver.find_element(*self.item_l).click()
        self.driver.find_element(*self.item_z).click()
        self.driver.find_element(*self.item_x).click()
        self.driver.find_element(*self.item_v).click()
        self.driver.find_element(*self.item_n).click()
        self.driver.find_element(*self.item_m).click()
        if num == 0:  # 活动生效
            pass
        elif num == 1:  # 活动在微商城不生效
            time.sleep(2)
            self.driver.find_element(*self.item_sa).click()
        elif num == 2:  # 活动仅限制新用户
            time.sleep(2)
            self.driver.find_elements(*self.item_sb)[1].click()
        elif num == 3:  # 活动仅限会员
            time.sleep(2)
            self.driver.find_elements(*self.item_sb)[2].click()
        elif num == 4:  # 仅限拥有指定标签的用户参与
            time.sleep(2)
            self.driver.find_elements(*self.item_sb)[3].click()
        elif num == 5:  # 仅限不含指定标签的用户参与
            time.sleep(2)
            self.driver.find_elements(*self.item_sb)[4].click()
        elif num == 6:  # 提示需要绑定手机号才可购买
            time.sleep(2)
            self.driver.find_elements(*self.item_sb)[6].click()
        elif num == 7:  # 单日库存限制一份
            self.item_04()
            self.driver.find_elements(*self.item_sb)[8].click()
        elif num == 8:  # 活动期间库存限制一份
            self.item_04()
            self.driver.find_elements(*self.item_sb)[9].click()
        elif num == 9:  # 每日限购一份
            self.item_04()
            self.driver.find_elements(*self.item_sb)[11].click()
        elif num == 10:  # 每单限购一份
            self.item_04()
            self.driver.find_elements(*self.item_sb)[12].click()
        elif num == 11:  # 活动期间限购一份
            self.item_04()
            self.driver.find_elements(*self.item_sb)[13].click()
        self.driver.switch_to.default_content()
        self.driver.find_element(*self.item_q).click()

    def item_03(self,num):  # 设置单品促销活动价格
        iframe = self.driver.find_element(*self.item_a)
        self.driver.switch_to.frame(iframe)  # 切换到单品页面
        time.sleep(5)
        self.driver.find_elements(*self.item_j)[0].click()
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element(*self.item_ja)
        self.driver.switch_to.frame(iframe)  # 切换到单品促销的价格
        if num == 0:  # 按折扣算
            self.driver.find_element(*self.item_jb).clear()
            self.driver.find_element(*self.item_jb).send_keys(9)
            self.driver.switch_to.default_content()
            self.driver.find_element(*self.item_je).click()
            self.driver.switch_to.default_content()
            iframe = self.driver.find_element(*self.item_a)
            self.driver.switch_to.frame(iframe)  # 切换到单品页面
            time.sleep(5)
            self.driver.find_elements(*self.item_sx)[0].click()

        elif num == 1:  # 按活动价算
            self.driver.find_elements(*self.item_jc)[1].click()
            self.driver.find_element(*self.item_jd).clear()
            self.driver.find_element(*self.item_jd).send_keys(4)
            self.driver.switch_to.default_content()
            self.driver.find_element(*self.item_je).click()
            self.driver.switch_to.default_content()
            self.driver.find_element(*self.item_sx).click()

        elif num == 2:
            pass


        time.sleep(5)
        self.driver.quit()

    def item_04(self):
        time.sleep(2)
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
        time.sleep(2)


if __name__ == '__main__':
    T = Item(Common)
    T.item(2)