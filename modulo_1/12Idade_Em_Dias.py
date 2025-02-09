# // Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, 
# // meses e dias. 
# // Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 
# // dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, 
# // como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio 
# // matemático simples. 
# // Entrada 
# // O arquivo de entrada contém um valor inteiro. 
# // Saída 
# // Imprima a saída conforme exemplo fornecido.

d = int(input("Informe os dias: "))
print()

# Calcula anos, meses e dias
ano = d // 365  # 1 ano = 365 dias
resto_Dias = d % 365  # O que sobra após calcular os anos
meses = resto_Dias // 30  # 1 mês = 30 dias
dias = resto_Dias % 30  # O que sobra após calcular os meses

# Exibe o resultado em coluna
print(f"{ano:.0f} ano(s)")
print(f"{meses:.0f} mes(es)")
print(f"{dias:.0f} dia(s)")