# face_detector.py
import cv2

def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    return frame

def webcam_face_detection(save_video=False):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    if save_video:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

    while True:
        ret, frame = cap.read()
        frame = detect_faces(frame, face_cascade)
        cv2.imshow('Face Detection', frame)

        if save_video:
            out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if save_video:
        out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    webcam_face_detection(save_video=True)
