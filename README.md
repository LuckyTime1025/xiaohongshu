# 小红书自动化

## 部署

> 先决条件  
> - Python 3.11.1  
> - 下载 Firefox 提供的 WebDriver
>   - [geckodriver](https://github.com/mozilla/geckodriver)

### 克隆项目

```shell
git clone https://github.com/LuckyTime1025/xiaohongshu.git
```

### 进入项目目录

```shell
cd xiaohongshu
```

### 创建虚拟环境

```shell
python -m venv venv
```

### 激活虚拟环境

```shell
.\venv\Scripts\activate
```

### 安装 Pypi 依赖

```shell
pip install -r requirements.txt 
```

## 使用

### 运行项目

```shell
python main.py
```

> 项目启动后会先检测 cookies.json 中的 Cookie 是否有效，如果没有该文件或 Cookie 失效，则使用手机号接受验证码登陆，否则使用 Cookie 自动登陆

## 注意事项

### 使用图文上传时

当需要上传多个图片时，每个图片路径使用英文逗号 ',' 分隔！