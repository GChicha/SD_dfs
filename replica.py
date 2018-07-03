from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from os import getenv

class ReplicaHandler(SimpleXMLRPCRequestHandler):
    rpc_path = ("/",)

class Replica:
    def __init__(self, directory):
        """
        directory = ".data"
        open(self.directory + "/" + nome_arquivo, "r").read()
        """
        pass

    def read(nome_arquivo):
        pass

    def write(nome_arquivo, dados):
        pass

with SimpleXMLRPCServer((getenv("IP_HOST", default="localhost"), 8000),
        requestHandler=ReplicaHandler) as server:
    server.register_introspection_functions()

    server.register_instance(Replica(getenv("DFS_DIR", default=".data")))

    server.serve_forever()
