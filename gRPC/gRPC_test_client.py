# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import time

import helloworld_pb2
import helloworld_pb2_grpc

#time measuring
file = open('result.html', 'w')
function_tries = 50

#html headers
file.write("<html><head><title>Timing</title></head><body><table><tr><th>function</th><th>time(ms)</th></tr>")

def timing(f):
    def wrap(*args):
        total = 0
        ret = None
        for i in range(function_tries):
            time1 = time.time()
            ret = f(*args)
            time2 = time.time()
            total = total + (time2 - time1)
        file.write("<tr>")
        file.write("<td>"+f.__name__+"</td>")
        file.write("<td>"+str(total*100)+"</td>")
        file.write("</tr>")
        return ret
    return wrap

@timing
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='otario'))
        print("Greeter client received: " + response.message)
        response = stub.SayHelloAgain(helloworld_pb2.HelloRequestNumber(number=3))
        print("Greeter client received: " + response.message)


if __name__ == '__main__':
    print ("Iniciando o client...")

    run()