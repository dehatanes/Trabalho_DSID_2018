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
import pandas as pd

import my_remote_procedure_call_pb2
import my_remote_procedure_call_pb2_grpc

QTD_ITERACOES = 20
HOST = "localhost"
PORT = 50051

response_df = pd.DataFrame()
response_dict = {}

def pegaTempo(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        total = time2 - time1
        response_dict[f.__name__] = total * 1000
        return ret
    return wrap

class ExampleValues(object):
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

class CasosTeste():
    stub = None
    
    @pegaTempo
    def createStub(self, host, port):
        channel = grpc.insecure_channel("{}:{}".format(host, port))
        self.stub = my_remote_procedure_call_pb2_grpc.DiferentOperationsHandlerStub(channel)
    @pegaTempo
    def takeNothing_ReturnNothing(self):
        return self.stub.takeNothing_ReturnNothing(my_remote_procedure_call_pb2.NoMessage())

    @pegaTempo
    def takeIntNumber_ReturnIntNumber(self):
        return self.stub.takeIntNumber_ReturnIntNumber(my_remote_procedure_call_pb2.IntNumberMessage(item=ExampleValues.int_number))

    @pegaTempo
    def takeIntNumbers_ReturnIntNumber(self):
        return self.stub.takeIntNumbers_ReturnIntNumber(my_remote_procedure_call_pb2.TenIntNumbersMessage(item1 = ExampleValues.int_numbers[0],
                                                                                                        item2  = ExampleValues.int_numbers[1],
                                                                                                        item3  = ExampleValues.int_numbers[2],
                                                                                                        item4  = ExampleValues.int_numbers[3],
                                                                                                        item5  = ExampleValues.int_numbers[4],
                                                                                                        item6  = ExampleValues.int_numbers[5],
                                                                                                        item7  = ExampleValues.int_numbers[6],
                                                                                                        item8  = ExampleValues.int_numbers[7],
                                                                                                        item9  = ExampleValues.int_numbers[8],
                                                                                                        item10 = ExampleValues.int_numbers[9]))

    @pegaTempo
    def takeIntNumber_ReturnIntNumbers(self):
        return self.stub.takeIntNumber_ReturnIntNumbers(my_remote_procedure_call_pb2.IntNumberMessage(item=ExampleValues.int_number))

    @pegaTempo
    def takeLongIntNumber_ReturnLongIntNumbers(self):
        return self.stub.takeLongIntNumber_ReturnLongIntNumbers(my_remote_procedure_call_pb2.LongIntNumberMessage(item=ExampleValues.long_int_number))

    @pegaTempo
    def takeFloatNumber_ReturnFloatNumber(self):
        return self.stub.takeFloatNumber_ReturnFloatNumber(my_remote_procedure_call_pb2.FloatNumberMessage(item=ExampleValues.float_number))

    @pegaTempo
    def takeString_ReturnString1(self):
        return self.stub.takeString_ReturnString1(my_remote_procedure_call_pb2.StringMessage(item=ExampleValues.string_1char))

    @pegaTempo
    def takeString_ReturnString8(self):
        return self.stub.takeString_ReturnString8(my_remote_procedure_call_pb2.StringMessage(item=ExampleValues.string_8chars))

    @pegaTempo
    def takeString_ReturnString64(self):
        return self.stub.takeString_ReturnString64(my_remote_procedure_call_pb2.StringMessage(item=ExampleValues.string_64chars))

    @pegaTempo
    def takeString_ReturnString512(self):
        return self.stub.takeString_ReturnString512(my_remote_procedure_call_pb2.StringMessage(item=ExampleValues.string_512chars))

    @pegaTempo
    def takeBoolean_ReturnBoolean(self):
        return self.stub.takeBoolean_ReturnBoolean(my_remote_procedure_call_pb2.BooleanMessage(item=ExampleValues.boolean))

    @pegaTempo
    def takeObject_ReturnObject(self):
        return self.stub.takeObject_ReturnObject(my_remote_procedure_call_pb2.ObjectMessage(item=ExampleValues.objeto))


def runTests(host, port):
        casoTeste = CasosTeste()
        # Creating stub
        print "\tCreating stub..."
        casoTeste.createStub(host, port)
        # Start the tests
        casoTeste.takeNothing_ReturnNothing()
        print "\tRunning takeNothing_ReturnNothing..."
        casoTeste.takeIntNumber_ReturnIntNumber()
        print "\tRunning takeIntNumber_ReturnIntNumber..."
        casoTeste.takeIntNumbers_ReturnIntNumber()
        print "\tRunning takeIntNumbers_ReturnIntNumber..."
        casoTeste.takeIntNumber_ReturnIntNumbers()
        print "\tRunning takeIntNumber_ReturnIntNumbers..."
        casoTeste.takeLongIntNumber_ReturnLongIntNumbers()
        print "\tRunning takeLongIntNumber_ReturnLongIntNumbers..."
        casoTeste.takeFloatNumber_ReturnFloatNumber()
        print "\tRunning takeFloatNumber_ReturnFloatNumber..."
        casoTeste.takeString_ReturnString1()
        print "\tRunning takeString_ReturnString1..."
        casoTeste.takeString_ReturnString8()
        print "\tRunning takeString_ReturnString8..."
        casoTeste.takeString_ReturnString64()
        print "\tRunning takeString_ReturnString64..."
        casoTeste.takeString_ReturnString512()
        print "\tRunning takeString_ReturnString512..."
        casoTeste.takeBoolean_ReturnBoolean()
        print "\tRunning takeBoolean_ReturnBoolean..."
        casoTeste.takeObject_ReturnObject()
        print "\tRunning takeObject_ReturnObject..."


if __name__ == '__main__':
    print "----------------------"
    print "   CLIENT INICIADO    "
    print "----------------------"

    for i in range(QTD_ITERACOES):
        print ("\nIteracao [{}]".format(i))
        response_dict = {}
        runTests(HOST, PORT)
        response_df = response_df.append(response_dict, ignore_index=True)
    
    response_df.to_excel("resultados_testes_gRPC.xlsx")
    response_df.describe().transpose().to_excel("resultados_analise_gRPC.xlsx")
    print "FIM"