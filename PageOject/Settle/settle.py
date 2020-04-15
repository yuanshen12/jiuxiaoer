from Base.BaseOperate import Operate


class Settle():

    def __init__(self, driver):
        self.driver = driver

    def get_settle(self):
        path = "../Xls/settle.xls"
        name = "settle01"
        data = Operate(self.driver).get_element_operate(path, name)
        return data