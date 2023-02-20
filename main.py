from flask import Flask, send_from_directory, make_response
from flask_restful import Resource, Api
import asyncio
from bilibili_api import video, Credential, HEADERS, sync
import httpx
import os

app = Flask(__name__)
api = Api(app)
SESSDATA = ""
BILI_JCT = ""
BUVID3 = ""

# FFMPEG 路径，查看：http://ffmpeg.org/
FFMPEG_PATH = "./ffmpeg-5.1.1-amd64-static/ffmpeg"

async def download_url(url: str, out: str, info: str):
    # 下载函数
    async with httpx.AsyncClient(headers=HEADERS) as sess:
        resp = await sess.get(url)
        length = resp.headers.get('content-length')
        with open(out, 'wb') as f:
            process = 0
            for chunk in resp.iter_bytes(1024):
                if not chunk:
                    break

                process += len(chunk)
                print(f'下载 {info} {process} / {length}')
                f.write(chunk)


# @app.route('/')
# def index():
#     return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
class HelloWorld(Resource):
    def get(self):
    #         # 实例化 Credential 类
    #     credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUVID3)
    #     # 实例化 Video 类
    #     v = video.Video(bvid="BV1AV411x7Gs", credential=credential)
    #     # 获取视频下载链接
    #     download_url_data = sync( v.get_download_url(0))
    #     # 解析视频下载信息
    #     detecter = video.VideoDownloadURLDataDetecter(data=download_url_data)
    #     streams = detecter.detect_best_streams()
    #     # 有 MP4 流 / FLV 流两种可能
    #     if detecter.check_flv_stream() == True:
    #         # FLV 流下载
    #         sync(download_url(streams[0].url, "flv_temp.flv", "FLV 音视频流")) 
    #         # 转换文件格式
    #         os.system(f'{FFMPEG_PATH} -i flv_temp.flv video.mp4')
    #         # 删除临时文件
    #         os.remove("flv_temp.flv")
    #     else:
    #         # MP4 流下载
    #         sync(download_url(streams[0].url, "video_temp.m4s", "视频流")) 
    #         sync(download_url(streams[1].url, "audio_temp.m4s", "视频流")) 
    #         # 混流
    #         os.system(f'{FFMPEG_PATH} -i video_temp.m4s -i audio_temp.m4s -vcodec copy -acodec copy video.mp4')
    #         # 删除临时文件
    # #         os.remove("video_temp.m4s")
    # #         os.remove("audio_temp.m4s")

    #     print('已下载为：video.mp4')
        return make_response(send_from_directory('./', 'video.mp4', as_attachment=True))
        

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