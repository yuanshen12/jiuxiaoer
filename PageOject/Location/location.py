from Base.BaseOperate import Operate


class Location():

    def __init__(self, driver):
        self.driver = driver

    def location_switchover(self):
        path = "../Xls/locate.xls"
        name = "locate01"
        data = Operate(self.driver).get_element_operate(path, name)
        return data

