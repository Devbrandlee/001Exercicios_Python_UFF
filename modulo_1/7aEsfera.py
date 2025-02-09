# Problema A: Esfera 

# Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor 
# de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * 𝑅3. Considere (atribua) 
# para pi o valor 3.14159. 
# Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens 
# (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro. 
# Entrada 
# O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), 
# correspondente ao raio da esfera. 
# Saída 
# A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, 
# com um espaço antes e um espaço depois da igualdade. O valor deverá ser apresentado 
# com 3 casas após o ponto. 


raio = float(input())
calcVolume = (4.0/3) * 3.14159 * raio * raio * raio

print(f"VOLUME = {calcVolume:.3f}")

#Deixar o códio mais limpo calculando o raio ao cubo evitando raio*raio*raio

#resultado = base ** expoente

#print(2 ** 2)  # 2² = 4
#print(2 ** 3)  # 2³ = 8
#print(2 ** 4)  # 2⁴ = 16
#print(2 ** 5)  # 2⁵ = 32
#print(2 ** 6)  # 2⁶ = 64
#print(2 ** 7)  # 2⁷ = 128
#Isso funciona para qualquer número, inclusive números negativos e frações.

raio = float(input())
calcVolume = (4.0/3) * 3.14159 * raio ** 3

print(f"VOLUME = {calcVolume:.3f}")

#ou

raio = float(input())
calcVolume = (4.0 / 3) * 3.14159 * pow(raio, 3)

print(f"VOLUME = {calcVolume:.3f}")

# Alternativa com pow()
# Outra forma de fazer isso é usando a função pow(base, expoente), que faz a mesma coisa:



# print(pow(2, 3))  # 2³ = 8
# print(pow(3, 4))  # 3⁴ = 81
# Então, sempre que precisar elevar um número a uma potência (como 2, 3, 4, 5, etc.), você pode usar ** ou pow()
