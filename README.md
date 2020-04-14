# 酒小二app商城自动化测试

使用工具：python + appium 

选择框架：自动化框架有模块驱动，参数驱动，关键字驱动和行为驱动四大主流模型，结合商城实际情况，暂定关键字驱动模型。


关键字驱动模型基本实现方式：通过使用关键字，对测试场景及测试用例进行遍历，达到测试场景和测试用例与脚本分离。

优势：\
1、脚本与测试用例分离，易于维护\
2、采用表格化用例，易于理解\
3、重用性好，易于扩展\
4、易于集成等\

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
<td><img src="http://yuanshen.oss-cn-beijing.aliyuncs.com/img/login.jpg?Expires=1586795802&OSSAccessKeyId=TMP.3Kh46gpMJqe7brE9Prh9aKRVpwpVJwNXExocLS4kzWa9pet8ryAW7Hk4KUAPJHHQ59NG6jZ7Gp2Ht8Fo1BjFtysFPopQ4r&Signature=GdM8yMSCU0ok2uQpMw9LnuQOutY%3D">
</td>
</tr>
</table>