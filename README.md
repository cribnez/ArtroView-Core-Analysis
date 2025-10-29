# ArtroView Core Analysis Engine

Este repositorio contiene el motor de análisis central de **ArtroView**, un sistema de bajo costo para el análisis postural y la cuantificación del rango de movimiento articular desarrollado en la Universidad Politécnica de Chiapas.

El código proporcionado utiliza **OpenCV** para la captura de video y **MediaPipe** para la estimación de pose en tiempo real. La función principal es calcular ángulos biomecánicos (ej. flexión del codo y abducción del hombro) a partir de las coordenadas 3D de los puntos de referencia corporales detectados.
# 🦾 ArtroView Core Analysis Engine

Este repositorio contiene el motor de análisis central de **ArtroView**, un sistema de bajo costo para el análisis postural y la cuantificación del rango de movimiento articular desarrollado en la Universidad Politécnica de Chiapas.

El código proporcionado (`analisis_publico.py`) utiliza **OpenCV** para la captura de video y **MediaPipe** para la estimación de pose en tiempo real. La función principal es calcular ángulos biomecánicos (ej. flexión del codo y abducción del hombro) a partir de las coordenadas 2D de los puntos de referencia corporales detectados.

Este proyecto busca ofrecer una base de código abierto para que investigadores, estudiantes y desarrolladores puedan crear herramientas accesibles para la telerehabilitación y el análisis de movimiento.

## ⭐ Características Principales

* **Detección en Tiempo Real:** Utiliza MediaPipe Pose para detectar 33 puntos de referencia corporales.
* **Cálculo de Ángulos:** Incluye una función (`calculate_angle`) para calcular el ángulo entre tres articulaciones.
* **Visualización:** Muestra el esqueleto, los puntos de referencia y los ángulos calculados directamente sobre el video.
* **Ejemplos Implementados:** Muestra el cálculo para la abducción del hombro derecho y la flexión del codo derecho.

---

## 🛠️ Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TU-USUARIO/TU-REPOSITORIO.git](https://github.com/TU-USUARIO/TU-REPOSITORIO.git)
    cd TU-REPOSITORIO
    ```

2.  **(Recomendado) Crea un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    El script requiere `opencv`, `mediapipe` y `numpy`.
    ```bash
    pip install opencv-python mediapipe numpy
    ```

---

## 🚀 Uso

El script principal es `analisis_publico.py`.

1.  **Para ejecutar con tu webcam (por defecto):**
    Asegúrate de que tu cámara esté conectada y ejecuta el siguiente comando en tu terminal:
    ```bash
    python analisis_publico.py
    ```

2.  **Para analizar un archivo de video:**
    Abre el archivo `analisis_publico.py` y modifica la **línea 54** para que apunte a la ruta de tu video:
    ```python
    # Cambia '0' por la ruta de tu video
    cap = cv2.VideoCapture("ruta/a/tu/video.mp4") 
    ```

3.  **Para salir:**
    Presiona la tecla **'q'** con la ventana de video seleccionada.

---

## 🧠 Cómo Funciona

El script sigue estos pasos en cada frame del video:

1.  **Captura:** Lee un frame del video (webcam o archivo).
2.  **Procesamiento:** Convierte el frame de BGR a RGB y lo pasa al modelo de MediaPipe Pose para detectar los landmarks.
3.  **Extracción:** Obtiene las coordenadas `[x, y]` de las articulaciones necesarias (hombros, codos, muñecas, caderas).
4.  **Cálculo:** Usa la función `calculate_angle` para calcular los ángulos de interés:
    * **Abducción de Hombro Derecho:** Ángulo entre `Cadera Derecha`, `Hombro Derecho` y `Codo Derecho`.
    * **Flexión de Codo Derecho:** Ángulo entre `Hombro Derecho`, `Codo Derecho` y `Muñeca Derecha`.
5.  **Visualización:** Dibuja el esqueleto y los ángulos calculados en el frame usando OpenCV.
6.  **Muestra:** Muestra el frame procesado en una ventana.

---

## Características Principales

-   Detección de 33 puntos de referencia corporales en tiempo real con MediaPipe Pose.
-   Cálculo preciso de ángulos entre tres puntos (articulaciones) en un plano 2D.
-   Visualización en tiempo real del esqueleto, los puntos de referencia y el ángulo calculado sobre el video.
-   Estructura de código base para análisis de abducción de hombro y flexión de codo.

## Instalación

Asegúrate de tener Python 3.8 o superior. Las dependencias principales se pueden instalar vía pip:

```bash
pip install opencv-python mediapipe numpy
