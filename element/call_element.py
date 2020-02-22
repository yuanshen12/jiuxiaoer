class Element(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):  # duration定义滑动时间参数，毫秒单位
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def amend(self, one, two):
        name = one
        names = name[1].format(two)
        name_to = (name[0],) + (names,)
        return name_to

    def amends(self, one, two, three):
        name = one
        names = name[1].format(two, three)
        name_to = (name[0],) + (names,)
        return name_to
