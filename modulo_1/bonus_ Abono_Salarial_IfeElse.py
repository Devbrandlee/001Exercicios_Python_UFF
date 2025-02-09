#O programa a seguir calcula o abono salarial que uma empresa concederá aos seus funcionários 
# com mais de um ano de  tempo de serviço. Os que tem menos de 10 anos ganharão abono de  10%. Os demais
# ganharão de 25%

salario = float  (input("Digite o salário atual "))

tempo = int(input("Diga quantos anos completos tem de serviço:"))

if tempo<1:
    print("Seu salário se mantem o mesmo:", salario)
    
else:
    if tempo <10:
        salario = salario * 1.10
    else:
        salario = salario * 1.25
print("Seu novo salário com abono:", salario)


# Use 1.10 e 1.25 quando quiser calcular diretamente o novo salário com o aumento.

# Use 0.10 e 0.25 quando quiser calcular apenas o valor do aumento (e depois somar ao salário atual).

# No seu caso, como você quer calcular o novo salário diretamente, usar 1.10 e 1.25 é mais prático e eficiente.