import cv2
import img


def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbour)
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1.5, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    return coords


def detect(img, faceCascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0),"yellow":(0,255,255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color["yellow"], "face detected")

    if len(coords)==4:
        roi_img = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]]
        coords = draw_boundary(roi_img, eyecascade, 1.1, 14, color["red"], "eyes ")
    return img




faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyecascade = cv2.CascadeClassifier("haarcascade_eye.xml")

video_capture = cv2.VideoCapture(0)
while True:
    _, img = video_capture.read()
    img = detect(img, faceCascade)
    cv2.imshow("eye Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
