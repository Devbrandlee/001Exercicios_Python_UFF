
# A fórmula para calcular a área de uma circunferência é:area = π ∙ raio2. Considerando 
# para este problema que 𝜋 = 3,14159. 
# Efetue o cálculo da área, elevando o valor de raio 
# ao quadrado e multiplicando por 𝜋. 

# Entrada 
# A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável 𝑟𝑎𝑖𝑜. 

# Saída 

# Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo 
# abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). 
# Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso 
# contrário, você receberá "Presentation Error".  

pi = 3.14159

raio = float (input("Digite o valor do raio "))

area = pi * (raio * raio)

print(f"O valor da área é A= {area:.4f}")