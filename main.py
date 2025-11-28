import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:

        face_roi = frame[y:y + h, x:x + w]

        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)

        frame[y:y + h, x:x + w] = blurred_face

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

    cv2.imshow('Face Blurring', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
