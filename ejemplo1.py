# Vision Artificial
# Profesor: Juan Manuel Barrios
# Fecha: 11 de septiembre de 2023

import sys
import os
import cv2

if len(sys.argv) <= 1:
    print("uso: {} [nombre_de_imagen]".format(sys.argv[0])) 
    sys.exit()

print("Usando OpenCV {} con Python {}.{}.{}".format(cv2.__version__, sys.version_info.major, sys.version_info.minor, sys.version_info.micro))

filename = sys.argv[1]
img_color = cv2.imread(filename, cv2.IMREAD_COLOR)
if img_color is None:
    sys.exit()
img_gris = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
thresh, img_bin = cv2.threshold(img_gris, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("{} size={} binary_threshold={}".format(filename, img_color.shape, thresh))
cv2.imshow(filename + " (color)", img_color)
cv2.imshow(filename + " (gris)", img_gris)
cv2.imshow(filename + " (bin)", img_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
