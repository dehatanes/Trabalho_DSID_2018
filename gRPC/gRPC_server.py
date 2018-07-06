# -*- coding: utf-8 -*-
"""
Universidade de São Paulo - USP
Escola de Artes, Ciências e Humanidades - EACH
ACH2147 - Desenvolvimento de Sistemas de Informação Distribuídos

Débora Atanes Buss  		nUSP: 9276860
Marcel Canhisares			nUSP: 9360603
"""
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

from concurrent import futures
import time

import grpc

import my_remote_procedure_call_pb2
import my_remote_procedure_call_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DiferentOperationsHandler(my_remote_procedure_call_pb2_grpc.DiferentOperationsHandlerServicer):

    def takeNothing_ReturnNothing(self, request, context):
        return my_remote_procedure_call_pb2.NoMessage()

    def takeIntNumber_ReturnIntNumber(self, request, context):
        return my_remote_procedure_call_pb2.IntNumberMessage(item=request.item)

    def takeIntNumbers_ReturnIntNumber(self, request, context):
        return my_remote_procedure_call_pb2.IntNumberMessage(item=request.item1)

    def takeIntNumber_ReturnIntNumbers(self, request, context):
        return my_remote_procedure_call_pb2.TenIntNumbersMessage(item1 = request.item,
                                                                item2  = request.item,
                                                                item3  = request.item,
                                                                item4  = request.item,
                                                                item5  = request.item,
                                                                item6  = request.item,
                                                                item7  = request.item,
                                                                item8  = request.item,
                                                                item9  = request.item,
                                                                item10 = request.item)

    def takeLongIntNumber_ReturnLongIntNumbers(self, request, context):
        return my_remote_procedure_call_pb2.LongIntNumberMessage(item=request.item)
    
    def takeFloatNumber_ReturnFloatNumber(self, request, context):
        return my_remote_procedure_call_pb2.FloatNumberMessage(item=request.item)

    def takeString_ReturnString1(self, request, context):
        return my_remote_procedure_call_pb2.StringMessage(item=request.item)

    def takeString_ReturnString8(self, request, context):
        return my_remote_procedure_call_pb2.StringMessage(item=request.item)

    def takeString_ReturnString64(self, request, context):
        return my_remote_procedure_call_pb2.StringMessage(item=request.item)

    def takeString_ReturnString512(self, request, context):
        return my_remote_procedure_call_pb2.StringMessage(item=request.item)
    
    def takeBoolean_ReturnBoolean(self, request, context):
        return my_remote_procedure_call_pb2.BooleanMessage(item=request.item)

    def takeObject_ReturnObject(self, request, context):
        return my_remote_procedure_call_pb2.ObjectMessage(item=request.item)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_remote_procedure_call_pb2_grpc.add_DiferentOperationsHandlerServicer_to_server(DiferentOperationsHandler(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print "Iniciando o server..."
    serve()