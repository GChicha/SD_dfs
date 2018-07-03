from xmlrpc.server import SimpleXMLRPCServer
from os import getenv
from collections import namedtuple
from uuid import uuid4
from functools import reduce

import time
import random
import configparser
import xmlrpc.client

Lock = namedtuple("Lock", ["tipo", "password"])

class Arquivo:
    read_lock = []
    write_lock = False

    locks = []

    def __init__(self, name, dados, replicas):
        self.name = name
        self.write(dados, replicas, password="god")

    def write(self, dados, replicas, password=None):
        if password == "god" or reduce(lambda autorizacao, lock: autorizacao or lock.password == password,
                                       self.locks, False):
            for replica in replicas:
                replica.write(self.name, dados)
        else:
            raise Exception("Não autorizado") 
    
    def read(self, tipo, replica):
        if not self.locks or (tipo == "r"  and self.locks[0].tipo == "r"):
            password = int(((time.time() * 10 ** 4) + 1000) % 10 ** 4)        
            self.locks.append(Lock(tipo, password))            
            return (replica.read(self.name), password)
        else:
            raise Exception("Não autorizado")

    def close(self, password):
        self.locks = list(filter(lambda x: x.password != password,  self.locks))

class Master:
    files_map = {}
    replicas = []

    def __init__(self):
        with open("hosts", "r") as hosts:
            for line in hosts:
                self.replicas.append(xmlrpc.client.ServerProxy("http://%s:8000/" % line.strip()))

    def read(self, tipo, name):
        replica = random.choice(self.replicas) 
        return self.files_map[name].read(tipo, replica)

    def write(self, name, dados, password=None):
        if self.files_map.get(name) is None:
            self.files_map[name] = Arquivo(name, dados, self.replicas)
        else:
            self.files_map[name].write(dados, self.replicas, password)
    
    def close(self, name, password):
        self.files_map[name].close(password)

def main():
    server = SimpleXMLRPCServer((getenv("DFS_IP", "localhost"), int(getenv("DFS_PORT", "8000"))), allow_none=True)
    server.register_introspection_functions()
    server.register_instance(Master())
    server.serve_forever()

if __name__ == "__main__":
    main()
