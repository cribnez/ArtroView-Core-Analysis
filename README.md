# ArtroView Core Analysis Engine

Este repositorio contiene el motor de análisis central de **ArtroView**, un sistema de bajo costo para el análisis postural y la cuantificación del rango de movimiento articular desarrollado en la Universidad Politécnica de Chiapas.

El código proporcionado utiliza **OpenCV** para la captura de video y **MediaPipe** para la estimación de pose en tiempo real. La función principal es calcular ángulos biomecánicos (ej. flexión del codo y abducción del hombro) a partir de las coordenadas 3D de los puntos de referencia corporales detectados.

Este proyecto busca ofrecer una base de código abierto para que investigadores, estudiantes y desarrolladores puedan crear herramientas accesibles para la telerehabilitación y el análisis de movimiento.

## Características Principales

-   Detección de 33 puntos de referencia corporales en tiempo real con MediaPipe Pose.
-   Cálculo preciso de ángulos entre tres puntos (articulaciones) en un plano 2D.
-   Visualización en tiempo real del esqueleto, los puntos de referencia y el ángulo calculado sobre el video.
-   Estructura de código base para análisis de abducción de hombro y flexión de codo.

## Instalación

Asegúrate de tener Python 3.8 o superior. Las dependencias principales se pueden instalar vía pip:

```bash
pip install opencv-python mediapipe numpy
