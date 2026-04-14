from picamera2 import Picamera2
import cv2
import time
import motion
import config
import mailer

# Kamera initialiseiren
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

last_mail = 0

while True:
    # Framevergleich
    frame1 = picam2.capture_array()
    time.sleep(config.TIMER)
    frame2 = picam2.capture_array()

    # Live Bild
    cv2.imshow("cam", frame2)

    # Bewegung prüfen
    if motion.detect_motion(frame1, frame2):

        # Spam-Cooldown
        if time.time() - last_mail > config.COOLDOWN:
            print("ALARM!")
 
            # Bild speichern
            image_path = f"data/snapshots/alarm_{int(time.time())}.jpg"
            cv2.imwrite(image_path, frame2)

            # Mail mit Bild
            mailer.send_mail(image_path)

            # Log schreiben
            with open("logs/log.txt", "a") as f:
                f.write("Bewegung erkannt\n")

            last_mail = time.time()

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()