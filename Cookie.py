import json

import Config


def set_cookie():
    """设置Cookie"""
    try:
        for cookie in json.loads(Config.CookiesDict[Config.CurrentUser]):
            Config.Browser.add_cookie(cookie)
        Config.Browser.refresh()
    except KeyError:
        return


def get_new_cookie():
    """获取新的Cookie"""
    cookies = json.dumps(Config.Browser.get_cookies())
    Config.CookiesDict[Config.CurrentUser] = cookies
    set_cookie()


def save_cookie():
    """保存Cookie"""
    print("正在保存Cookie")
    with open('cookies.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(Config.CookiesDict))
    print('cookies保存成功！')
