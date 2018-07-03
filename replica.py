from xmlrpc.server import SimpleXMLRPCServer
from os import getenv


class Replica:
    def __init__(self, directory):
        self.directory = ".data"

    def read(self, nome_arquivo):
        with open(self.directory + "/" + nome_arquivo, 'r') as arq:
            return arq.read()

    def write(self, nome_arquivo, dados):
        with open(self.directory + "/" + nome_arquivo, 'w') as arq:
            arq.write(dados)


server = SimpleXMLRPCServer(
    (getenv("IP_HOST", default="localhost"), 8000), allow_none=True)
server.register_introspection_functions()
server.register_instance(Replica(getenv("DFS_DIR", default=".data")))
server.serve_forever()
