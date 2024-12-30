from flask import Blueprint, render_template, request
import requests

app = Blueprint('weather', __name__)

# OpenWeatherMap API 设置
API_KEY = '75a959987097ae615b1e2e39b4a79262'  # 替换成你自己的 API 密钥
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error_message = None

    # 处理表单提交：获取城市名称并请求天气数据
    if request.method == 'POST':
        city = request.form.get('city')

        # 向 OpenWeatherMap API 发起请求
        params = {
            'q': city,                  # 城市名称
            'appid': API_KEY,           # API 密钥
            'units': 'metric',          # 温度单位：摄氏度
            'lang': 'zh_cn'             # 中文返回
        }

        # 发起 GET 请求并获取响应
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            weather_data = response.json()   # 将响应数据转换为 JSON 格式
        else:
            error_message = '无法获取天气数据，请检查城市名是否正确或稍后再试。'

    return render_template('index.html', weather_data=weather_data, error_message=error_message)
