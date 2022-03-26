import cv2

def captacaoVideo():
    webcam = cv2.VideoCapture(0)

    if webcam.isOpened():
        validacao, frame = webcam.read()
        while validacao:
            validacao, frame = webcam.read()
            cv2.imshow("Captação da web cam", frame)
            key = cv2.waitKey(5)

            if key == 27: #refere-se a tecla 27
                break

        cv2.imwrite("photograpy.jpg", frame)

    webcam.release()
    cv2.destroyAllWindows()