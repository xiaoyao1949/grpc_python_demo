import grpc
import demo_pb2
import demo_pb2_grpc

server_addr = "127.0.0.1:8888"


def main():
    with grpc.insecure_channel(server_addr) as channel:
        client = demo_pb2_grpc.DemoStub(channel)
        rsp = client.SayHello(demo_pb2.HelloRequest(name="张三"))
    print(rsp.result)


if __name__ == "__main__":
    main()
