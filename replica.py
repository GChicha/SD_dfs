from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from os import getenv

class ReplicaHandler(SimpleXMLRPCRequestHandler):
    rpc_path = ("/",)

class Replica:
    def __init__(self, directory):
        pass

    def get(self):
        pass

    def delete(self):
        pass

    def put(self, arquivo):
        pass

with SimpleXMLRPCServer((getenv("IP_HOST", default="localhost"), 8000),
        requestHandler=ReplicaHandler) as server:
    server.register_introspection_functions()

    server.register_instance(Replica(getenv("DFS_DIR", default=".data")))

    server.serve_forever()
