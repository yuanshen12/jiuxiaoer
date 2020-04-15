from Base.BaseOperate import Operate


class Search():

    def __init__(self, driver):
        self.driver = driver

    def search_page(self):
        path = "../Xls/search.xls"
        name = "search"
        data = Operate(self.driver).get_element_operate(path, name)
        return data