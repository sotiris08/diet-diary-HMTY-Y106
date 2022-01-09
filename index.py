import importlib

c = importlib.import_module('Client')
Client = c.Client
Client.init()