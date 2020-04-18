# 酒小二app商城自动化测试

使用工具：python + appium || pytest + allure

选择框架：自动化框架有模块驱动，参数驱动，关键字驱动和行为驱动四大主流模型，结合商城实际情况，暂定关键字驱动模型。


关键字驱动模型基本实现方式：通过使用关键字，对测试场景及测试用例进行遍历，达到测试场景和测试用例与脚本分离。

优势：\
1、脚本与测试用例分离，易于维护\
2、采用表格化用例，易于理解\
3、重用性好，易于扩展\
4、易于集成等

## 框架
-  Base层管理常用方法
-  log日志记录和存放失败截图
-  PageObject层处理页面逻辑
-  report层生成测试报告
-  TestCase层调用Page层，传入表格用例
-  xls层以excel表格存放测试用例
-  yaml层存放配置信息

## 框架设计模型
> [设计图](https://github.com/yuanshen12/jiuxiaoer/blob/test1/log/login.jpg)

<table>
<tr>
<td><img src="http://yuanshen.oss-cn-beijing.aliyuncs.com/appium/login.jpg?Expires=1587231781&OSSAccessKeyId=TMP.3KkSzzFVxeFgCMC9gmhQRpmqN5M3219YiQyxAYtVo91rjE9UxvGcpPGtozTEmLmFv74koerCjhLGTG8wjmJZFbRgkRV3fH&Signature=9W9IVGtWd1XpiccTLynyKKG%2FJ%2Fw%3D">
</td>
</tr>
</table>
<br>

>[测试报告](https://github.com/yuanshen12/jiuxiaoer/blob/test1/log/allure.png)
<table>
<tr>
<td><img src="http://yuanshen.oss-cn-beijing.aliyuncs.com/appium/allure.png?Expires=1587231714&OSSAccessKeyId=TMP.3KkSzzFVxeFgCMC9gmhQRpmqN5M3219YiQyxAYtVo91rjE9UxvGcpPGtozTEmLmFv74koerCjhLGTG8wjmJZFbRgkRV3fH&Signature=QbBFiMPX86QbqNlY0rYOwUCQqw0%3D">
</td>
</tr>
</table>

>[错误查询](https://github.com/yuanshen12/jiuxiaoer/blob/test1/log/log.png)
<table>
<tr>
<td><img src="http://yuanshen.oss-cn-beijing.aliyuncs.com/appium/log.png?Expires=1587231836&OSSAccessKeyId=TMP.3KkSzzFVxeFgCMC9gmhQRpmqN5M3219YiQyxAYtVo91rjE9UxvGcpPGtozTEmLmFv74koerCjhLGTG8wjmJZFbRgkRV3fH&Signature=8yBVLJSxpNIiLsE4fyDtoGuOH2s%3D">
</td>
</tr>
</table>

>[用例表](https://github.com/yuanshen12/jiuxiaoer/blob/test1/log/case.png)
<table>
<tr>
<td><img src="http://yuanshen.oss-cn-beijing.aliyuncs.com/appium/case.png?Expires=1587231853&OSSAccessKeyId=TMP.3KkSzzFVxeFgCMC9gmhQRpmqN5M3219YiQyxAYtVo91rjE9UxvGcpPGtozTEmLmFv74koerCjhLGTG8wjmJZFbRgkRV3fH&Signature=%2FZCTUkbnX4PP%2Blaxk5ElUyHvLi8%3D">
</td>
</tr>
</table>