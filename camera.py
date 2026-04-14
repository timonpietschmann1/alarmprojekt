#Testscript

from picamera2 import Picamera2
import cv2

#Kamera initialisieren
picam2 = Picamera2()

#Auflösung setzen
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))

#Kamera starten
picam2.start()

#Live Bild
while True:
    
    frame = picam2.capture_array()
    
    cv2.imshow("cam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
