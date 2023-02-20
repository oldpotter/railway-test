from flask import Flask, jsonify
from flask_restful import Resource, Api
import os
import asyncio
from bilibili_api import video, sync

app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def index():
#     return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
class HelloWorld(Resource):
    def get(self):
         # 实例化 Video 类
        v = video.Video(bvid="BV1uv411q7Mv")
        # 获取信息
        info = sync(v.get_info())
        # 打印信息
        print(info)
        return {'hello': info}
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

    # from flask import Flask
# from flask_restful import Resource, Api
 
# app = Flask(__name__)
# api = Api(app)
 
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
 
# api.add_resource(HelloWorld, '/')
 
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)