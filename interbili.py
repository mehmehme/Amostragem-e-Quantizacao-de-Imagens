import cv2 as cv

src = cv.imread("tiger.jpg")

tigerBil = cv.resize(src,dsize=None,fx=2,fy=2,interpolation= cv.INTER_LINEAR)
tigerCub = cv.resize(src,dsize=None,fx=2,fy=2,interpolation= cv.INTER_CUBIC)

cv.imshow("Bilinear",tigerBil)
cv.imshow("Cubica", tigerCub)
cv.waitKey(0)
cv.destroyAllWindows()

# a imagem bilinear fica mais embaçada que a cúbica que realça os pelos do tigre