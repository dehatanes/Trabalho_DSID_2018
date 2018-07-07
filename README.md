# Benchmark Remote Procedure Calls (RPC)

|                          |                                                                                                                              |
| ----------------- |------------------------------------------------------------------------------------------:|
| Linguagem       | [Python 2.7](https://www.python.org/ "Python's Homepage")                             |
| Application       | [gRPC](https://grpc.io/ "gRPC's Homepage")                                                      |
| Application       | [RPyC](https://rpyc.readthedocs.io/en/latest/# "RPyC's Homepage")                |                                                                                          |

Universidade de São Paulo - USP
</br>Escola de Artes, Ciências e Humanidades - EACH
</br>ACH2147 - Desenvolvimento de Sistemas de Informação Distribuídos

Débora Atanes Buss......nUSP: 9276860
</br>Marcel Canhisares..........nUSP: 9360603

## SOBRE

Trata-se de uma aplicação Python para execução de chamadas de procedimentos remotos que faz parte do trabalho final da disciplina Desenvolvimento de Sistemas de Informação Distribuídos do curso de Sistemas de Informação. 
O objetivo deste trabalho é analisar e comparar o desempenho quanto ao tempo de execução de diferentes mecanismos de Chamadas de Procedimentos Remotos (RPC). Para isso, foram escolhidas duas implementações distintas de sistemas RPC para serem avaliadas quando submetidas a diferentes cenários como Cliente e Servidor na mesma máquina e Cliente e Servidor em máquinas diferentes, além de quando conduzidas a realizar diferentes operações básicas.

--------------------
## BUILT WITH
Principais pontos da aplicação.
* [gRPC](https://grpc.io/docs/quickstart/python.html "Python gRPC Docs") - gRPC is a modern open source high performance RPC framework that can run in any environment.
* [RPyC](https://rpyc.readthedocs.io/en/latest/# "RPyC's Homepage") - RPyC  is a *transparent*  python library for *symmetrical*  [remote procedure calls](http://en.wikipedia.org/wiki/Remote_procedure_calls), [clustering](http://en.wikipedia.org/wiki/Clustering) and [distributed-computing](http://en.wikipedia.org/wiki/Distributed_computing).


## REQUIREMENTS
Uma forma prática de instalar de uma vez tudo o que é necessário para conseguir trabalhar com o código. </br> Obs: Certifique-se de já ter o `pip` em versão 9.0.1 ou superior instalado na máquina.
```
>> pip install -r requirements.txt
```

#### Para rodar o código no diretório raiz:
* Instanciando o server: 
```
>>  # para server gRPC
>>  python gRPC/gRPC_server.py
>>  # ou para server RPyC 
>>  python rpyc/server.py
```
* Em outro terminal, instanciando o client:
```
>>  # para client gRPC
>>  python gRPC/gRPC_client.py
>>  # ou para client RPyC
>>  python rpyc/client.py
```


# AUTHORS
* @dehatanes :heart:
* @mcanhisares :top:
