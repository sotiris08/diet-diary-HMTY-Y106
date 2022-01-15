import importlib

c = importlib.import_module('Client') #import Client
Client = c.Client
Client.init()