def es_primo(num):
    if num <= 1:
        return False
    if num <=3:
        return True
    if num % 2==0  or num % 3 == 0:
        return False
    
    i=5
    while i*i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        
        i+=6
    return True



def nextPrime(n):
    if n<=1:
        n=2
    else:
        n+=1

    while True:
        if es_primo(n):
            return n
        n+=1

def mediana(n1,n2,n3):
    numeros=[n1,n2,n3]
    numeros.sort()

    return numeros[1]

import random
import string

def generar_contraseña():
    longitud = random.randint(7, 10)  
    contrasena = ''.join(random.choice(string.printable[33:127]) for _ in range(longitud))
    return contrasena

import math

def calcular_hipotenusa(a, b):
    hipotenusa = math.sqrt(a**2 + b**2)
    return hipotenusa