from grpc_tools import protoc

protoc.main(
    (
        '',
        '-I./app/proto',
        '--python_out=./app/proto/dist',
        '--grpc_python_out=./app/proto/dist',
        'simple.proto'
    )
)
