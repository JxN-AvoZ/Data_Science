from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('angle', help='rotación deseada', type=int)
parser.add_argument( '-i', '--info', help='muestra el tamaño de la imagen', action='store_true')
args = parser.parse_args()

angle = args.angle

try:
    im = Image.open(args.input_file)
    
except FileNotFoundError:
    print('Archivo de entrada no encontrado,\nIntroduce la ruta/nombre de archivo correcto.')

else:
    rotated = im.rotate(angle)
    im.close() # cerrar el archivo de imagen, eliminándolo de la memoria
    rotated.save(args.output_file)
    print("Ejecución completada.'")

if args.info:
    print('Dimensiones de la imagen de entrada:', im.size)