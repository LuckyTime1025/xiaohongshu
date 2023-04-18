import os.path
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import Config


def create(create_js):
    print("等待资源上传……")
    time.sleep(10)
    create_js = f'return document.querySelector("{create_js}")'
    Config.Browser.execute_script(create_js).click()
    print("发布成功！")
    print("等待页面返回！")
    time.sleep(5)


def input_content():
    Config.title = input("请输入标题：")
    Config.describe = input("请输入描述：")
    Config.Browser.find_element(By.CSS_SELECTOR, ".c-input_inner").send_keys(Config.title)
    Config.Browser.find_element(By.CSS_SELECTOR, "#post-textarea").send_keys(Config.describe)


def get_video():
    while True:
        path_mp4 = input("视频路径：")
        path_cover = input("封面路径(不输入使用默认封面)：")
        if not os.path.isfile(path_mp4):
            print("视频不存在！")
        elif path_cover != '':
            if not os.path.isfile(path_cover):
                print("封面图片不存在")
            else:
                return path_mp4, path_cover
        else:
            return path_mp4


def create_video():
    path_mp4, path_cover = get_video()

    try:
        WebDriverWait(Config.Browser, 10, 0.2).until(
            lambda x: x.find_element(By.CSS_SELECTOR, "div.tab:nth-child(1)")).click()
    except TimeoutException:
        print("网页好像加载失败了！请重试！")

    # 点击上传视频
    Config.Browser.find_element(By.CSS_SELECTOR, ".upload-input").send_keys(path_mp4)
    time.sleep(10)
    WebDriverWait(Config.Browser, 20).until(
        EC.presence_of_element_located((By.XPATH, r'//*[contains(text(),"重新上传")]'))
    )
    while True:
        time.sleep(3)
        try:
            Config.Browser.find_element(By.XPATH, r'//*[contains(text(),"重新上传")]')
            break
        except Exception:
            print("视频还在上传中···")

    if path_cover != "":
        Config.Browser.find_element(By.CSS_SELECTOR, "button.css-k3hpu2:nth-child(3)").click()

        Config.Browser.find_element(By.XPATH, r'//*[text()="上传封面"]').click()
        # 上传封面
        Config.Browser.find_element(By.CSS_SELECTOR, "div.upload-wrapper:nth-child(2) > input:nth-child(1)").send_keys(
            path_cover)

        # 提交封面
        WebDriverWait(Config.Browser, 10, 0.2).until(
            lambda x: x.find_element(By.CSS_SELECTOR, ".css-8mz9r9 > div:nth-child(1) > button:nth-child(2)")).click()
    input_content()
    # 发布
    create(".publishBtn")


def get_image():
    while True:
        path_image = input("图片路径：").split(",")
        if 0 < len(path_image) <= 9:
            for i in path_image:
                if not os.path.isfile(i):
                    print("图片不存在！")
                    break
            else:
                return "\n".join(path_image)
        else:
            print("图片最少1张，最多9张")
            continue


def create_image():
    path_image = get_image()
    try:
        WebDriverWait(Config.Browser, 10, 0.2).until(
            lambda x: x.find_element(By.CSS_SELECTOR, "div.tab:nth-child(2)")).click()
    except TimeoutException:
        print("网页好像加载失败了！请重试！")
    #  上传图片
    Config.Browser.find_element(By.CSS_SELECTOR, ".upload-wrapper > div:nth-child(1) > input:nth-child(1)").send_keys(
        path_image)
    input_content()

    create("button.css-k3hpu2:nth-child(1)")
