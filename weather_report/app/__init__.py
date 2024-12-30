# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # 导入并注册路由蓝图
    from .routes import app as weather_blueprint
    app.register_blueprint(weather_blueprint)

    return app
