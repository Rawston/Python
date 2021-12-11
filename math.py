import math
lado1 = float(input('Entre com o tamanho do primeiro seguimento:'))
lado2 = float(input('Entre com o tamanho do segundo seguimento:'))
lado3 = float(input('Entre com o tamanho do terceiro seguimento:'))
forma_triangulo = False
if (lado1 > lado2 > lado3) and (lado1 < (lado2 + lado3)):
    hiponenusa = lado1
    cateto1 = lado2
    cateto2 = lado3
    forma_triangulo = True
elif (lado2 > lado1) and (lado2 > lado3) and (lado2 < (lado1 + lado3)):
    hiponenusa = lado2
    cateto1 = lado1
    cateto2 = lado3
    forma_triangulo = True
elif (lado3 > lado2) and (lado3 > lado1) and (lado3 < (lado1 + lado2)):
    hiponenusa = lado3
    cateto1 = lado1
    cateto2 = lado2
    forma_triangulo = True
if forma_triangulo:
    if (hiponenusa ** 2) == (cateto1 ** 2) + (cateto2 ** 2):
        print(f'Os seguimentos formam um triangulo retangulo, de hipotenusa {hiponenusa} e catetos {cateto1} e {cateto2}.')
    else:
        print('Os seguimentos Não formam triangulo retangulo.')
else:
        print('Os seguimentos não formam triangulo algum.')

