import os
import yaml
from yaml.scanner import ScannerError

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def get_yaml(path):
    try:
        with open(PATH(path), encoding="utf-8") as file:
            num = yaml.load(file)
            return num
    except FileNotFoundError:
        print("---文件不存在---")
        return False
    except yaml.scanner.ScannerError:
        print("---用例格式错误---")


if __name__ == '__main__':
    data = get_yaml("../Yaml/config.yaml")
    print(data["platformName"])