import cv2
import numpy as np
from tensorflow.keras.models import load_model


def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255.0
    return img


#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("videoplayback.mp4")
cap.set(3, 480)
cap.set(4, 480)


model = load_model("model_v4.keras")  


while True:
    success, frame = cap.read()
    if not success:
        continue

    img = cv2.resize(frame, (32, 32))
    img = preProcess(img)
    img = img.reshape(1, 32, 32, 1)

    predictions = model.predict(img)
    classIndex = int(np.argmax(predictions))
    probVal = np.amax(predictions)

    print(classIndex, f"{probVal:.2f}")

    if probVal > 0.7:
        cv2.putText(frame, f"{classIndex}   {probVal:.2f}", (50, 50),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)

    cv2.imshow("Number Classification", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
