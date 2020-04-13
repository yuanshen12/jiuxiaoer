from Base.BaseXlm import get_excel_data
from Base.BaseRunner import app, TestCase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from time import sleep


def get_error(element):
    try:
        element
    except selenium.common.exceptions.TimeoutException:
        print("---寻找元素超时---")
        return False
    except selenium.common.exceptions.NoSuchElementException:
        print("---寻找元素不存在---")
        return False
    except selenium.common.exceptions.ElementNotVisibleException:
        print("---寻找元素未能选中---")
    except selenium.common.exceptions.StaleElementReferenceException:
        print("---元素页面发生了变化---")
        return False
    except selenium.common.exceptions.WebDriverException:
        print("---WebDriver出问题了---")
        return False
    else:
        return True


class Element:
    def __init__(self, driver):
        self.driver = driver

    def wait(self, *display):
        wait = WebDriverWait(self.driver, 20, 0.3).until(EC.visibility_of_element_located(display))
        return wait

    def waits(self, *display):
        waits = WebDriverWait(self.driver, 20, 0.3).until(EC.visibility_of_any_elements_located(display))
        return waits

    def get_element(self, path, name):
        data = get_excel_data(path, name)
        for element in data:
            print("element[3]这是定位方式：{}".format(element[3]))
            print("element[4]这是定位元素：{}".format(element[4]))
            print("element[5]这是操作方式：{}".format(element[5]))
            print("element[6]这是输入数据：{}".format(element[6]))
            if len(element[4]) == 0:
                print("执行这里吗")
                break
            elif element[4] == "time":
                sleep(element[6])
            elif element[5] == "elements":
                elements_click = self.waits(element[3], element[4])[int(element[6])].click()
                get_error(elements_click)
            else:
                if element[5] == "click":
                    get_click = self.wait(element[3], element[4]).click()
                    get_error(get_click)
                elif element[5] == "send_keys":
                    get_send_keys = self.wait(element[3], element[4]).send_keys(element[6])
                    get_error(get_send_keys)
                elif element[5] == "clear":
                    get_clear = self.wait(element[3], element[4]).clear()
                    get_error(get_clear)
                elif element[5] == "text":
                    text = self.wait(element[3], element[4]).text
                    get_error(text)
                    return text


if __name__ == '__main__':
    data = Element(app()).get_element("../Xls/locate.xls", "locate_edit")
    print(data)
