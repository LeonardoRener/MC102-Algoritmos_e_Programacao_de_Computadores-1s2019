#Leonardo Rener de Oliveira RA: 201270
#Primeiro o programa dividi a altura pela velocidade de queda
h = float(input()) #altura
vb = float(input()) #velocidade de queda
d = float(input()) #distancia da base rebelde
T = float(input()) #forca de empuxo do micro explosivo
tv = h / vb
th = d / T
t = tv - th
print("%.3f" % t)