#!C:\Users\Administrator\PycharmProjects\jiuxiaoer\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sqlmap==1.3.11','console_scripts','sqlmap'
__requires__ = 'sqlmap==1.3.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sqlmap==1.3.11', 'console_scripts', 'sqlmap')()
    )
