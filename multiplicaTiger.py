import cv2 as cv
import numpy as np

src = cv.imread("tiger.jpg")

#tiger = cv.multiply(src, 0.8)
img = np.clip(src,255,255).astype(np.uint8)
tiger = cv.multiply(img, 1.5)


cv.imshow("tigre",tiger)
cv.imshow("original",src)
cv.waitKey(0)
cv.destroyAllWindows()

# com 0.8 a imagem após a multiplicação ficou mais escura do que a original
# já com 1.5 a imagem ficou saturada
# com todos os pixels no valor máximo a imagem fica totalmente branca