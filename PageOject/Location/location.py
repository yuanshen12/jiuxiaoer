from selenium.webdriver.common.by import By


class Location():
    call_address = (By.ID, "com.callme.mall:id/station")  # 定位切换区域
    call_seek = (By.ID, "com.callme.mall:id/content")  # 定位搜索区域
    call_search = (By.ID, "com.callme.mall:id/addreLayout")  # 确定贵阳站
    call_home = (By.ID, "com.callme.mall:id/ll_tap")  # 首页菜单
    call_locate = (By.ID, "com.callme.mall:id/mapTipsLayout")  # 地图模式
    call_update = (By.ID, "com.callme.mall:id/getLocationBtn")  # 地图模式更新
    call_list = (By.ID, "com.callme.mall:id/nameLayout")  # 地图模式位置列表
    call_history = (By.ID, "com.callme.mall:id/clean_history")  # 地图模式历史搜索删除
    call_cancel = (By.ID, "com.callme.mall:id/cancel")  # 定位搜索取消
    call_info = (By.ID, "com.callme.mall:id/address")  # 定位当前地址(门牌号)
    call_again = (By.ID, "com.callme.mall:id/location")  # 定位重新定位
    call_location = (By.ID, "com.callme.mall:id/name")  # 定位收货地址
    call_location_sure = (By.ID, "com.callme.mall:id/btn")  # 定位收货地址确定
    call_add = (By.XPATH, "//*[@text= '新增地址']")  # 定位新增地址
    call_nearby = (By.ID, "com.callme.mall:id/image")  # 定位附近地址
    call_name = (By.ID, "com.callme.mall:id/name")  # 定位新增姓名
    call_women = (By.ID, "com.callme.mall:id/sex_women")  # 定位新增性别女
    call_phone = (By.ID, "com.callme.mall:id/phone")  # 定位新增电话
    call_add_location = (By.ID, "com.callme.mall:id/location")  # 定位新增位置
    call_tag = (By.ID, "com.callme.mall:id/tag")  # 定位新增标签
    call_save = (By.ID, "com.callme.mall:id/save")  # 定位新增保存
    call_login = (By.ID, "com.callme.mall:id/login")  # 登录


