virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt

rm *pb2*
python -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ demo.proto

python server.py &
python client.py