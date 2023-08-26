# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de  2m²

n1 = float(input("Informe a Largura da parede que deseja pintar: "))
n2 = float(input('Agora, informe a Altura dela: '))
area = n1 * n2
print('Para pintar esta parede será necessário {} Litros de tinta.'.format(area/2))
