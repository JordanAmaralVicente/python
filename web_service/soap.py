#! /usr/bin/python3.8
from zeep import Client

def CelsiusToFahrenheit(client):
    try:
        result = client.service.CelsiusToFahrenheit(TemperatureInCelsius=0)
        print(f' 0ºC = { result }ºF')
    except Exception as exception:
        print(exception)

def fahrenheitToCelsius(client):
    try:
        result = client.service.FahrenheitToCelsius(TemperatureInFahrenheit=132)
        print(f' 0ºF = { "%.2f" % result }ºC')
    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    client = Client('http://www.learnwebservices.com/services/tempconverter?wsdl')
    print('Usando Arquitetura SOAP xml de learnwebservices.com')
    CelsiusToFahrenheit(client)
    fahrenheitToCelsius(client)