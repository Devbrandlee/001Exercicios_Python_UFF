# // em uma fábrica, e informe-o expresso no formato horas:minutos:segundos. 
# // Entrada 
# // O arquivo de entrada contém um valor inteiro N. 
# // Saída 
# // Imprima o tempo lido no arquivo de entrada (segundos), convertido para 
# // horas:minutos:segundos, conforme exemplo fornecido.

#n=tempo em segundos

n = int(input("Digite o tempo em segundos: "))

# Calcula as horas, minutos e segundos
hora = n // 3600  # 1 hora = 3600 segundos
resto_segundos = n % 3600  # O que sobra após calcular as horas
minutos = resto_segundos // 60  # 1 minuto = 60 segundos
segundos = resto_segundos % 60  # O que sobra após calcular os minutos

# Exibe o resultado no formato HH:MM:SS
print(f"{hora:.0f}:{minutos:.0f}:{segundos:.0f}")