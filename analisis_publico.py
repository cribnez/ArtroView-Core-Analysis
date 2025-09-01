# ArtroView Core Analysis Engine - analisis_publico.py
#
# Este script es una versión simplificada del motor de análisis de ArtroView.
# Su propósito es demostrar el núcleo de la tecnología de visión por computadora
# para el análisis de rango de movimiento articular en tiempo real.
#
# Creado por: Christian Roberto Ibáñez Nangüelú
# Afiliación: Universidad Politécnica de Chiapas
#
# Dependencias: pip install opencv-python mediapipe numpy

import cv2
import mediapipe as mp
import numpy as np

# --- Función para Calcular Ángulos ---
def calculate_angle(a, b, c):
    """
    Calcula el ángulo entre tres puntos (en grados).
    Args:
        a, b, c: Tuplas o listas con las coordenadas [x, y] de los puntos.
    Returns:
        El ángulo en grados.
    """
    a = np.array(a)  # Primer punto (ej. Hombro)
    b = np.array(b)  # Punto medio (ej. Codo)
    c = np.array(c)  # Punto final (ej. Muñeca)
    
    # Vectores desde el punto medio hacia los otros puntos
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    # Asegurarse que el ángulo está en el rango [0, 180]
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

# --- Inicialización de MediaPipe ---
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# --- Captura de Video ---
cap = cv2.VideoCapture(0) # '0' para la webcam. Puedes cambiarlo por la ruta de un video.

# Configurar la instancia de MediaPipe Pose
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    
    print("Iniciando análisis... Presiona 'q' para salir.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame. Saliendo...")
            break
        
        # Recolorar la imagen de BGR a RGB para MediaPipe
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Realizar la detección de pose
        results = pose.process(image)
    
        # Recolorar de vuelta a BGR para OpenCV
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # --- Extracción y Cálculo de Ángulos ---
        try:
            landmarks = results.pose_landmarks.landmark
            
            # --- Hombro Derecho ---
            hombro_d = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            codo_d = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            cadera_d = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            
            # Calcular ángulo de abducción del hombro derecho
            angulo_hombro_d = calculate_angle(cadera_d, hombro_d, codo_d)
            
            # --- Codo Derecho ---
            muneca_d = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # Calcular ángulo de flexión del codo derecho
            angulo_codo_d = calculate_angle(hombro_d, codo_d, muneca_d)
            
            # --- Visualización en Pantalla ---
            # Mostrar el ángulo del hombro
            cv2.putText(image, f"Hombro Der: {int(angulo_hombro_d)}", 
                           tuple(np.multiply(hombro_d, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Mostrar el ángulo del codo
            cv2.putText(image, f"Codo Der: {int(angulo_codo_d)}", 
                           tuple(np.multiply(codo_d, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            
        except Exception as e:
            # Pasa si no se detectan landmarks en el frame
            pass
        
        # --- Dibujar el esqueleto ---
        # Renderiza las detecciones en la imagen
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        # --- Mostrar la ventana ---
        cv2.imshow('Motor de Analisis de ArtroView', image)

        # Lógica para salir del bucle
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # --- Liberar recursos ---
    cap.release()
    cv2.destroyAllWindows()
    print("Análisis finalizado.")
