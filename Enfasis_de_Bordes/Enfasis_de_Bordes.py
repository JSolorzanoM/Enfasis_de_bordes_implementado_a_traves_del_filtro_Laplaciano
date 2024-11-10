import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

Tk().withdraw()
ruta_imagen = filedialog.askopenfilename(title="Selecciona una imagen", 
                                         filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp")])

# Función para aplicar la convolución
def aplicar_convolucion(imagen, kernel):
    alto, ancho = imagen.shape
    k_alto, k_ancho = kernel.shape
    borde = k_alto // 2

    # Aplicar padding de ceros a la imagen
    imagen_padded = np.pad(imagen, ((borde, borde), (borde, borde)), mode='constant', constant_values=0)
    resultado = np.zeros((alto, ancho), dtype=np.float32)

    # Recorrer la imagen y aplicar el kernel
    for i in range(alto):
        for j in range(ancho):
            region = imagen_padded[i:i + k_alto, j:j + k_ancho]
            resultado[i, j] = np.sum(region * kernel)
    
    return resultado

if ruta_imagen:
    # Cargar la imagen en color
    imagen_color = cv2.imread(ruta_imagen)
    #Escala de grises
    imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

    # Definir los kernels Laplacianos
    kernels = [
        np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32),
        np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32),
        np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32)
    ]
    nombres_kernels = ["Kernel 1", "Kernel 2", "Kernel 3"]

    # Aplicar la convolución para cada kernel
    resultados_convolucion = [aplicar_convolucion(imagen_gris, kernel) for kernel in kernels]
    # Convertir a escala de 8 bits para visualizar
    resultados_convolucion = [cv2.convertScaleAbs(resultado) for resultado in resultados_convolucion]

    # Aplicar el filtro Laplaciano usando la función de OpenCV
    laplaciano_opencv = cv2.Laplacian(imagen_gris, cv2.CV_64F)
    # Convertir a escala de 8 bits para visualizar
    laplaciano_opencv = cv2.convertScaleAbs(laplaciano_opencv)

    plt.figure(figsize=(15, 10))

    # Mostrar imagen original en color
    plt.subplot(2, 3, 1)
    plt.title("Imagen Original (Color)")
    plt.imshow(cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    # Mostrar imagen en escala de grises
    plt.subplot(2, 3, 2)
    plt.title("Imagen en Escala de Grises")
    plt.imshow(imagen_gris, cmap="gray")
    plt.axis("off")

    # Mostrar las imágenes con cada kernel
    for idx, (resultado, nombre) in enumerate(zip(resultados_convolucion, nombres_kernels), start=3):
        plt.subplot(2, 3, idx)
        plt.title(f"Convolución {nombre}")
        plt.imshow(resultado, cmap="gray")
        plt.axis("off")

    # Mostrar el resultado usando la convolución de OpenCV
    plt.subplot(2, 3, 6)
    plt.title("Laplaciano con OpenCV")
    plt.imshow(laplaciano_opencv, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
else:
    print("No se seleccionó ninguna imagen.")
