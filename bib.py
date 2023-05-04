def metrosParaCentimetros(metros):
    return metros*100

def salario(valor, horas):
    return valor*horas

def conversaoFahrenheit(fahrenheit):
    return (fahrenheit-32)/1.8

def imc(peso, altura):
    return (peso/altura**2)

def pesoMulta(peso):
    pesoExcedente = 0
    multa = 0
    if peso > 30:
        pesoExcedente = peso - 30
        multa = pesoExcedente * 3
        return pesoExcedente, multa
    else:
        return pesoExcedente, multa     

def inss(salarioBruto):
    return salarioBruto - (salarioBruto*0.92)

def ir(salarioBruto):
    return salarioBruto - (salarioBruto*0.89)

def ex1():
    metros=float(input('Digite a quantidade em metros: '))
    cm=metrosParaCentimetros(metros)
    print(f'{cm} centimetros')

def ex2():
    valor=float(input('Digite o valor que você recebe por hora: '))
    horas=float(input('Digite quantas horas você trabalha por mês: '))
    total=salario(valor, horas)
    print(total)

def ex3():
    fahrenheit=float(input("Digite a temperatura em fahrenheit: "))
    celcius=conversaoFahrenheit(fahrenheit)
    print(f"{fahrenheit}° fahrenheit equivalem a {celcius}° celcius")

def ex4():
    altura=float(input("Digite sua altura: "))
    peso=float(input("Digite seu peso: "))
    valorImc=imc(peso, altura)
    resultado="a"

    if valorImc<18.5:
        resultado=("abaixo do peso")

    elif 18.5<=valorImc<=24.9:
        resultado=("peso normal")

    elif 25<=valorImc<=29.9:
        resultado=("sobrepeso")

    else:
        resultado=("obesidade")

    print(f"Seu IMC é de {valorImc:.2f} ou seja, {resultado}")

def ex5():
    peso=float(input("Digite o peso do peixe em Kg: "))
    excesso, multa=pesoMulta(peso)

    if excesso==0:
        print("O peso não ultrapassa o limite permitido!")
    else:
        print(f"O peso excedente é de {excesso} Kg e o valor da multa é de R${multa}")

def ex6():
    valor=float(input('Digite o valor que você recebe por hora: '))
    horas=float(input('Digite quantas horas você trabalha por mês: '))
    totalBruto=salario(valor, horas)
    valorInss=inss(totalBruto)
    valorIr=ir(totalBruto)
    totalLiquido=totalBruto-valorInss-valorIr
    print(f"Salário bruto: R${totalBruto:.2f}\nDesconto INSS: R${valorInss:.2f}\nDesconto Imposto de renda: R${valorIr:.2f}\nSalário liquido: R${totalLiquido:.2f}")

def ex7():
    import math
    largura=float(input("Digite o valor da largura da parede: "))
    altura=float(input("Digite o valor da altura da parede: "))
    area=float(largura*altura)
    totalLatas=float(area/54)

    if totalLatas<=1:
        print(f"Será necessario {math.ceil(totalLatas)} lata de tinta")
    else:
        print(f"Serão necessárias {math.ceil(totalLatas)} latas de tinta")

