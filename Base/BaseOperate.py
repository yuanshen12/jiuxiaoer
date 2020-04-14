from Base.BaseXlm import get_excel_data
from Base.BaseRunner import app
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from time import sleep


class Operate:

    def __init__(self, driver):
        self.driver = driver

    def get_element_operate(self, file, name):
        try:
            self.operate_by(file, name)
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

    def operate_by(self, excel_file, excel_name):
        data = get_excel_data(excel_file, excel_name)
        for excel_cell in data:
            print("--定为方法:{}".format(excel_cell[3]))
            print("--操作元素:{}".format(excel_cell[4]))
            print("--执行方法:{}".format(excel_cell[5]))
            if len(excel_cell[4]) == 0:
                print("---元素为空---")
                break
            elif excel_cell[4] == "time":
                sleep(int(excel_cell[6]))
            elif excel_cell[5] == "click":
                self.get_click(excel_cell[3], excel_cell[4])
            elif excel_cell[5] == "text":
                self.get_text(excel_cell[3], excel_cell[4])

    def get_click(self, excel_three, excel_four):  # 操作点击
        if excel_three == "id" or excel_three == "class name" or excel_three == "xpath" or excel_three == "name":
            self.wait(excel_three, excel_four).click()
        else:
            self.waits(excel_three[:-3], excel_four)[int(excel_three[-2])].click()

    def get_text(self, excel_three, excel_four):  # 获取文本信息
        if excel_three == "id" or excel_three == "class name" or excel_three == "xpath" or excel_three == "name":
            text = self.wait(excel_three, excel_four).text
            print(text)
        else:
            text = self.waits(excel_three[:-3], excel_four)[int(excel_three[-2])].text
            print(text)

    def waits(self, *display):
        waits = WebDriverWait(self.driver, 20, 0.3).until(EC.visibility_of_any_elements_located(display))
        return waits

    def wait(self, *display):
        wait = WebDriverWait(self.driver, 20, 0.3).until(EC.element_to_be_clickable(display))
        return wait


if __name__ == '__main__':
    Operate(app()).get_element_operate("../Xls/locate.xls", "my")