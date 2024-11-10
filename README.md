# Enfasis de Bordes Implementado a Través del Filtro Laplaciano

Este proyecto aplica un filtro Laplaciano para detectar bordes en imágenes usando dos métodos: convolución manual y una implementación con OpenCV. La convolución manual permite observar el cálculo detallado de bordes, mientras que OpenCV ofrece una alternativa optimizada.

## Descripción

El script permite:

- Seleccionar una imagen desde el equipo.
- Convertir la imagen a escala de grises.
- Aplicar varios filtros Laplacianos usando convolución manual con tres kernels diferentes.
- Comparar estos resultados con el filtro Laplaciano aplicado por OpenCV.

El resultado muestra:

- La imagen original (en color).
- La imagen en escala de grises.
- La imagen con bordes resaltados según tres variantes del filtro Laplaciano.
- Una comparación con el filtro Laplaciano de OpenCV.

## Requisitos

Este proyecto utiliza las siguientes librerías:

- [OpenCV](https://opencv.org/) para la manipulación de imágenes.
- [NumPy](https://numpy.org/) para la manipulación de matrices.
- [Matplotlib](https://matplotlib.org/) para la visualización de resultados.

