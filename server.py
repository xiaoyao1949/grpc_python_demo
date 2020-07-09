import time
import grpc
from concurrent import futures

import demo_pb2, demo_pb2_grpc


class HelloServer(demo_pb2_grpc.DemoServicer):
    def SayHello(self, request, context):
        msg = f"Hello, {request.name}"
        return demo_pb2.HelloReply(result=msg)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service = HelloServer()
    demo_pb2_grpc.add_DemoServicer_to_server(service, server)
    server.add_insecure_port("127.0.0.1:8888")
    server.start()

    try:
        print("running...")
        time.sleep(1000)
    except KeyboardInterrupt:
        print("stopping...")
        server.stop(0)


if __name__ == "__main__":
    main()
