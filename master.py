import xmlrpc.client
import configparser
from collections import namedtuple
from uuid import uuid4

import replica

class Arquivo:
    read_lock = False
    write_lock = False
    replica = None

    password = None

    def __init__(self):
        pass

    def get_write_lock(self):
        if not (self.read_lock and self.write_lock):
            self.write_lock = True
            return True
        else:
            return False

    def get_write_lock(self):
        if not self.write_lock:
            self.read_lock = True
            return True
        else:
            return False

    def read_unlock(self, password):
        if self.read_lock

class Master:
    files_map = {}

    def __init__(self):
