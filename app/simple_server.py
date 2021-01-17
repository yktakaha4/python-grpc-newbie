import time
import grpc
from .proto.dist import simple_pb2
from .proto.dist import simple_pb2_grpc
import base64
from concurrent import futures


# シンプルサービスサーバーの定義
class SimpleServiceServicer(simple_pb2_grpc.SimpleServiceServicer):
    # 初期化
    def __init__(self):
        pass

    # 受信時の処理
    def SimpleSend(self, request, context):
        text = 'This is TEST!'
        image_b64 = base64.b64encode((open('./app/image.jpg', 'rb').read())).decode('utf8')
        return simple_pb2.SimpleResponse(text=text, image=image_b64)


# サーバーの開始
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
simple_pb2_grpc.add_SimpleServiceServicer_to_server(SimpleServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print('サーバーの開始')

# 待機
try:
    while True:
        time.sleep(3600)
except KeyboardInterrupt:
    # サーバーの停止
    server.stop(0)
