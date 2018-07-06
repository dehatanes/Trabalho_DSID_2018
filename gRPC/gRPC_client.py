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

import grpc
import time

import my_remote_procedure_call_pb2
import my_remote_procedure_call_pb2_grpc

class ExampleValues(object):
    from ObjectExample import MyObject
    void            = None 
    int_number      = 42
    int_numbers     = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    long_int_number = 2147483647
    float_number    = 3.1514
    string_1char    = "A"
    string_8chars   = "prosaico"
    string_64chars  = "Vou gerar varias coisas X e aleatorias no gerador de lero lero.."
    string_512chars = "Aa mobilidade dos capitais internacionais desafia a capacidade de equalizacao das condicoes financeiras e administrativas exigidas. Existem duvidas a respeito de como a valorizacao de fatores subjetivos deve passar por modificacoes independentemente dos conhecimentos estrategicos para atingir a excelencia. Caros amigos, a continua expansao de nossa atividade exige a precisao das formas de acao.  Nao podemos esquecer que a consolidacao estrutural obstaculiza a apreciacao da importancia do orcamento setorial."
    boolean         = False
    objeto          = my_remote_procedure_call_pb2.MyObject()


def runTests():
    with grpc.insecure_channel('localhost:50051') as channel:
        # Creating stub
        stub = my_remote_procedure_call_pb2_grpc.DiferentOperationsHandlerStub(channel)

        # Start the tests
        response = stub.takeNothing_ReturnNothing(my_remote_procedure_call_pb2.NoMessage())
        print("Response: {\n" + str(response) + " }\n")
        response = stub.takeIntNumber_ReturnIntNumber(my_remote_procedure_call_pb2.IntNumberMessage(item=ExampleValues.int_number))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeIntNumbers_ReturnIntNumber(my_remote_procedure_call_pb2.TenIntNumbersMessage(item1 = ExampleValues.int_numbers[0],
                                                                                                        item2  = ExampleValues.int_numbers[1],
                                                                                                        item3  = ExampleValues.int_numbers[2],
                                                                                                        item4  = ExampleValues.int_numbers[3],
                                                                                                        item5  = ExampleValues.int_numbers[4],
                                                                                                        item6  = ExampleValues.int_numbers[5],
                                                                                                        item7  = ExampleValues.int_numbers[6],
                                                                                                        item8  = ExampleValues.int_numbers[7],
                                                                                                        item9  = ExampleValues.int_numbers[8],
                                                                                                        item10 = ExampleValues.int_numbers[9]))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeIntNumber_ReturnIntNumbers(my_remote_procedure_call_pb2.IntNumberMessage(item=ExampleValues.int_number))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeLongIntNumber_ReturnLongIntNumbers(my_remote_procedure_call_pb2.LongIntNumberMessage(item=ExampleValues.long_int_number))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeFloatNumber_ReturnFloatNumber(my_remote_procedure_call_pb2.FloatNumberMessage(item=ExampleValues.float_number))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeString_ReturnString1(my_remote_procedure_call_pb2.StringMessage(item=ExampleValues.string_1char))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeString_ReturnString8(my_remote_procedure_call_pb2.StringMessage(item=ExampleValues.string_8chars))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeString_ReturnString64(my_remote_procedure_call_pb2.StringMessage(item=ExampleValues.string_64chars))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeString_ReturnString512(my_remote_procedure_call_pb2.StringMessage(item=ExampleValues.string_512chars))
        print("Response: {\n " + str(response) + " }\n")
        response = stub.takeBoolean_ReturnBoolean(my_remote_procedure_call_pb2.BooleanMessage(item=ExampleValues.boolean))
        print("Response: {\n " + str(response.item) + " }\n")
        response = stub.takeObject_ReturnObject(my_remote_procedure_call_pb2.ObjectMessage(item=ExampleValues.objeto))
        print("Response: {\n " + str(response) + " }\n")


if __name__ == '__main__':
    print ("Iniciando o client...")
    runTests()