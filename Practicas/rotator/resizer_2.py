from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('width', type=int, help='ancho de la imagen')
parser.add_argument('height', type=int, help='alto de la imagen')

args = parser.parse_args()

try:
    im = Image.open(args.input_file)
except Exception as error_msg:
    print(error_msg)
    print('the default image is used')
    im = Image.open('default_input.png')

new_size = (args.width, args.height)

resized = im.resize(new_size)
resized.save(args.output_file)
im.close()
