import cv2

#Use 0 para webcam
#vid = cv2.VideoCapture(0)

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("Não foi possivel ler o feed")


heigth  = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(heigth)
width  = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps  = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out = cv2.VideoWiriter('Boxing.mp4',cv2.VideoWiriter_fourcc(*'DIVX'), 30, (width,heigth))

while(True):

    # Capture o quadro do video
    # a cada quadro
    ret, frame = vid.read()

    cv2.imshow("Web cam", frame)
    out.write(frame)
    if cv2.waitKey(25) == 32:
        break

vid.release()
out.release()

cv2.destroyAllWindows()