# -*- coding: utf-8 -*-
"""
Universidade de São Paulo - USP
Escola de Artes, Ciências e Humanidades - EACH
ACH2147 - Desenvolvimento de Sistemas de Informação Distribuídos

Débora Atanes Buss  		nUSP: 9276860
Marcel Canhisares			nUSP: 9360603
"""

import rpyc
import time
import pandas as pd

function_tries = 20

response_df = pd.DataFrame()
response_dict = {}

def pegaTempo(f):
    def wrap(*args):
        total = 0
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        total = total + (time2 - time1) + tempoStub
        response_dict[f.__name__] = total * 1000
        return ret
    return wrap


tempoStub = 0
stub = None

class ObjectType(object):
    def __init__(self):
        self.name = "Kleber"
        self.age = 2
        self.isNicePerson = False

@pegaTempo
def createStub():
    return rpyc.connect("localhost", 18861)

@pegaTempo
def takeNothing_ReturnNothing():
    return stub.root.nothing()


@pegaTempo
def takeIntNumber_ReturnIntNumber():
    return stub.root.int(2)


@pegaTempo
def takeIntNumbers_ReturnIntNumber():
    return stub.root.int10int1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


@pegaTempo
def takeIntNumber_ReturnIntNumbers():
    return stub.root.int1int10(1)


@pegaTempo
def takeLongIntNumber_ReturnLongIntNumbers():
    return stub.root.long(long(2))


@pegaTempo
def takeFloatNumber_ReturnFloatNumber():
    return stub.root.float(0.2)


@pegaTempo
def takeString_ReturnString1(string):
    return stub.root.string(string)


@pegaTempo
def takeString_ReturnString8(string):
    return stub.root.string(string)


@pegaTempo
def takeString_ReturnString64(string):
    return stub.root.string(string)


@pegaTempo
def takeString_ReturnString512(string):
    return stub.root.string(string)


@pegaTempo
def takeBoolean_ReturnBoolean():
    return stub.root.bool(False)


@pegaTempo
def takeObject_ReturnObject():
    return stub.root.obj(ObjectType())

for i in range(function_tries):
    response_dict = {}
    stub = createStub()
    print(takeNothing_ReturnNothing())
    print(takeIntNumber_ReturnIntNumber())
    print(takeIntNumbers_ReturnIntNumber())
    print(takeIntNumber_ReturnIntNumbers())
    print(takeLongIntNumber_ReturnLongIntNumbers())
    print(takeFloatNumber_ReturnFloatNumber())
    print(takeString_ReturnString1("1"))
    print(takeString_ReturnString8("12345678"))
    print(takeString_ReturnString64("T4OvNmxk0C1DCDEz8Kj1E10prNTR7MOzYVoSO4hAPtqg48TDYpzbh3mR36C8MqBH"))
    print(takeString_ReturnString512(
        "fOR8Wq04bQNFU5TxqfnnWskQD0J19nBq1KCTdcMYB3w3foSKJasnnn3xbSUH0xnGfkoLzVwEUwlYETCuIzRKVEfHRbMmU3tvu9zOqYEto0vaKmp1SmkKF5ddO0OZlpvgXJJyugJiqhMXC4OERm3aoUP4Aya6TxNoiOhwLvgnvqW5WCHjY1fXYrESZyBfSaV4ZdqOEhMfsfSSHz7lznG9pbD1xrJGv4qhbHAAgQPrBRIlhTsLBhdU01TVdt4hFFk5JtMoiquH56MYYWcknT6npm0MRVC2aC3E1Y4tYK4y0anNavWaSxcYLax6LdYeKxYFLxJYvSTcQ8aJdILgnUt1x8NfZVtocnKGHPPu6DE9UobQAZE8FXAlnG6ss6pxQXsLFURwfmIehE1FxqZWrEAzNJkniY5mZqcNSnzj5nw7cZ6ioOUn5Kjb8UeIi8uvR5TQLgZKF8IOj0c6SDFMZUqnd5dFI8EOMBwXOhMkBPzI3igzUxCDDBWB7UkIJRxeQ7Ig"))
    print(takeBoolean_ReturnBoolean())
    print(takeObject_ReturnObject())
    response_df = response_df.append(response_dict, ignore_index=True)

response_df.to_excel("resultados_testes.xlsx")
response_df.describe().to_excel("resultados_analise.xlsx")
print(response_df)
