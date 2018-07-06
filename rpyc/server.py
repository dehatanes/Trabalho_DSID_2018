# -*- coding: utf-8 -*-
import rpyc
import json
port = 18861

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    # operação sem argumentos e sem valor de retorno
    def exposed_nothing(self):
        pass

    # operação com um argumento long e valor de retorno long 
    def exposed_int(self, number):
        return number*number

    # operação com oito argumentos long e valor de retorno long 
    def exposed_int1int10(self, n1):
        return n1, n1, n1, n1, n1, n1, n1, n1, n1, n1
    
    # operação com um argumento String e valor de retorno String (4 args)
    def exposed_int10int1(self, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10):
        return n1+n2+n3+n4+n5+n6+n7+n8+n9+n10

    # operação com um argumento String e valor de retorno String (8 args)
    def exposed_long(self, l1):
        return l1*l1

    # operação com um argumento String e valor de retorno String (16 args)
    def exposed_float(self, f1):
        return f1*f1

    # operação com um argumento String e valor de retorno String (32 args)
    def exposed_string(self,string):
        return string

    # operação com um argumento String e valor de retorno String (64 args)
    def exposed_bool(self, b1):
        return not b1

    # operação com um argumento String e valor de retorno String (128 args)
    def exposed_obj(self, obj):
        return obj

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=port)
    t.start()