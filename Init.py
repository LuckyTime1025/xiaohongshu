import json
import os

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import Config


def init_browser():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument(f'user-agent=={UserAgent().random}')
    # 无界面模式
    options.add_argument('--headless')

    Config.Browser = webdriver.Firefox(options=options)
    Config.Browser.maximize_window()


def init_cookie():
    """读取本地 Cookie"""
    if os.path.isfile("cookies.json"):
        with open("cookies.json", "r+", encoding="utf-8") as f:
            content = f.read()
            if content:
                Config.CookiesDict.update(json.loads(content))
            else:
                print("Cookie 文件为空！")
                Config.login_status = True
                return
    else:
        print("Cookie 文件不存在！")
        Config.login_status = True
        return


def init_user():
    """初始化 UserList"""
    for k, _ in Config.CookiesDict.items():
        Config.UserList.append(k)


def init():
    # 读取本地 cookie
    init_cookie()
    # 初始化所有用户
    init_user()
    # 初始化浏览器
    init_browser()
