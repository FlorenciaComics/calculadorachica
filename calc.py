def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a / b

while True:
    print("Bienvenido a mi calculadora.....")    
    numerouno = float(input("ingrese el primer numero: "))
    operador = (input("ingrese el operador (opciones: +,-,*,/):"))
    numerodos = float(input("ingrese el segundo numero: "))

    if operador =="+":
        resultado = suma(numerouno, numerodos)
        print(numerouno, operador, numerodos, "=", resultado)
    elif operador =="-":
        resultado = resta(numerouno,numerodos)
        print(numerouno, operador, numerodos, "=", resultado)
    elif operador =="*":
        resultado = multiplicacion(numerouno,numerodos)
        print(numerouno, operador, numerodos, "=", resultado)
    elif operador =="/":
        resultado = division(numerouno,numerodos)
        print(numerouno, operador, numerodos, "=", resultado)
    
    
