import cv2 as cv
import numpy as np

src = cv.imread("tiger.jpg")

tigerCin = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
tons128 = np.where(src < 128 ,0,128).astype(np.uint8)
tons64 = np.where(src < 128 ,0,64).astype(np.uint8)
tons8 = np.where(src < 128 ,0,8).astype(np.uint8)
tons2 = np.where(src < 128 ,0,2).astype(np.uint8)

cv.imshow("Cinza",tigerCin)
cv.imshow("128",tons128)
cv.imshow("64",tons64)
cv.imshow("8",tons8)
cv.imshow("2",tons2)
cv.imshow("original",src)
cv.waitKey(0)
cv.destroyAllWindows()

# com 2 se encostar a cara na tela ou levantar da cadeira consegue ver o tigre 
# com 8 tons se vê o tigre em meio ao breu
# com 64 tons conseguimos ver um pouco do tigre
# com 128 a imagem fica um pouco mais escura
# e em tons de cinza ela fica acinzentada