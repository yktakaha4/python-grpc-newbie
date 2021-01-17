# python-grpc-newbie

こちらを参考にさせていただく

https://note.com/npaka/n/n5c3263ad88ff


```shell
# インストール
poetry install

# GRPC定義作成
poetry run python -m app.proto.codegen

# サーバ起動
poetry run python -m app.simple_server

# (別ターミナルで)クライアント起動
```