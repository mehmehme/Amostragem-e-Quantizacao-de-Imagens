import cv2 as cv

src = cv.imread("quadrado.webp")

quadNear = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_NEAREST)
quadBil = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_LINEAR)
quadCub = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_CUBIC)

quadNear2 = cv.resize(quadNear, dsize=None,fx=4,fy=4,interpolation= cv.INTER_NEAREST)
quadBil2 = cv.resize(quadBil, dsize=None,fx=4,fy=4,interpolation= cv.INTER_LINEAR)
quadCub2 = cv.resize(quadCub, dsize=None,fx=4,fy=4,interpolation= cv.INTER_CUBIC)

cv.imshow("Nearest",quadNear2)
cv.imshow("Bilinear",quadBil2)
cv.imshow("Cubica", quadCub2)
cv.waitKey(0)
cv.destroyAllWindows()

# o pixelado é o que chega mais perto do original, definindo muito bem cada quadrado
# o bilinear e o cúbico ficam bem embaçados, mas o cúbico ainda consegue definir melhor cada quadrado

