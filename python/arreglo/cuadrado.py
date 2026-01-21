"""Calcular el cuadrado de numeros enteros de una lista.
params: numeros
"""
def cuadrado(numeros):
    cuadrados = []
    for i in numeros:
        cuadrados.append(i**2)
    return cuadrados

numerosNew = [1,2,3,4,5]
cuadradosNumeros = cuadrado(numerosNew)
for j in cuadradosNumeros:
    print(f"El cuadrado es: {j}")