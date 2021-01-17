import grpc
from .proto.dist import simple_pb2
from .proto.dist import simple_pb2_grpc
import base64

# サーバーとの接続
with grpc.insecure_channel('localhost:50051') as channel:
    stub = simple_pb2_grpc.SimpleServiceStub(channel)

    # データの取得
    response = stub.SimpleSend(simple_pb2.SimpleRequest(name='taro'))
    print('text:', response.text)
    with open('client.jpg', mode='wb') as f:
        f.write(base64.b64decode(response.image))
