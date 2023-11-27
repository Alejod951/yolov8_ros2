# Importamos las librerias
from ultralytics import YOLO
import cv2

# Leer nuestro modelo
model = YOLO("Vehicles.pt")
use_camera = True
# Realizar VideoCaptura
if use_camera:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture("/home/alejo/ros2_ws/src/parcialii/parcialii/Vehicles.pt")  

# Bucle
while True:
    # Leer nuestros fotogramas
    ret, frame = cap.read()

    if use_camera:
        cv2.putText(frame, "Camara", (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    else:
        cv2.putText(frame, "Video pregrabado", (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Leemos resultados
    resultados = model.predict(frame, imgsz = 640, conf = 0.55)

    # Mostramos resultados
    anotaciones = resultados[0].plot()

    # Mostramos nuestros fotogramas
    cv2.imshow("DETECCION", anotaciones)

    # Cambiar a la cámara principal
    if cv2.waitKey(1) & 0xFF == 112:
        usar_camara = True
        cap.release()  # Liberar la captura actual
        cap = cv2.VideoCapture(0)  

    # Cambiar al video pregrabado
    if cv2.waitKey(1) & 0xFF == 116:
        usar_camara = False
        cap.release()  # Liberar la captura actual
        cap = cv2.VideoCapture('/home/alejo/ros2_ws/src/parcialii/parcialii/Vehicles.pt')

    # Cerrar nuestro programa
    if cv2.waitKey(1) == 27:
        break

        

cap.release()
cv2.destroyAllWindows()