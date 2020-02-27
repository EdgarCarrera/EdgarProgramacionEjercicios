# Utiliza la función format de un string, para asignar valores en una salida.

def main():
  numBase = 11
  numAltura = 5
  AreaTriangulo=(numBase*numAltura)/2
  txt = "Area: {2:0.2f} ( {0} por {1} entre dos )"
  print(txt.format(numBase, numAltura, AreaTriangulo))

# {2:0,0f} es un flotante sin decimales.
# Donde el 2 del {2:0,0f} significa el resultado y el 
# 2 antes de la f significa los ceros que va a tener despues 
# del punto
# {0} por {1} entre dos y aqui el 0 significa la cantidad 
# del numero base y el 1 significa el numero de la altura