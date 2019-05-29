import cv2

def make_photo(extension = "jpg"):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()
    cv2.destroyAllWindows()

    return cv2.imencode("." + extension, frame)[1].tostring()
