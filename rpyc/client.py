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

QTD_ITERACOES = 20

response_df = pd.DataFrame()
response_dict = {}

def pegaTempo(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        total = time2 - time1
        response_dict[f.__name__] = total * 100
        return ret
    return wrap


tempoStub = time.time()
c = rpyc.connect("localhost", 18861)
tempoStub = time.time() - tempoStub


class ObjectType(object):
    def __init__(self):
        self.name = "Kleber"
        self.age = 2
        self.isNicePerson = False


@pegaTempo
def takeNothing_ReturnNothing():
    return c.root.nothing()


@pegaTempo
def takeIntNumber_ReturnIntNumber():
    return c.root.int(2)


@pegaTempo
def takeIntNumbers_ReturnIntNumber():
    return c.root.int10int1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


@pegaTempo
def takeIntNumber_ReturnIntNumbers():
    return c.root.int1int10(1)


@pegaTempo
def takeLongIntNumber_ReturnLongIntNumbers():
    return c.root.long(long(2))


@pegaTempo
def takeFloatNumber_ReturnFloatNumber():
    return c.root.float(0.2)


@pegaTempo
def takeString_ReturnString1(string):
    return c.root.string(string)


@pegaTempo
def takeString_ReturnString8(string):
    return c.root.string(string)


@pegaTempo
def takeString_ReturnString64(string):
    return c.root.string(string)


@pegaTempo
def takeString_ReturnString512(string):
    return c.root.string(string)


@pegaTempo
def takeBoolean_ReturnBoolean():
    return c.root.bool(False)


@pegaTempo
def takeObject_ReturnObject():
    return c.root.obj(ObjectType())

for i in range(QTD_ITERACOES):
    response_dict = {}
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

response_df.to_excel("resultados_testes_RPyC.xlsx")
response_df.describe().to_excel("resultados_analise_RPyC.xlsx")
print(response_df)
