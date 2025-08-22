import cv2 as cv

src = cv.imread("tiger.jpg")

tigerNear = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_NEAREST)
tigerBil = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_LINEAR)
tigerCub = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_CUBIC)

tigerNear2 = cv.resize(tigerNear, dsize=None,fx=4,fy=4,interpolation= cv.INTER_NEAREST)
tigerBil2 = cv.resize(tigerBil, dsize=None,fx=4,fy=4,interpolation= cv.INTER_LINEAR)
tigerCub2 = cv.resize(tigerCub, dsize=None,fx=4,fy=4,interpolation= cv.INTER_CUBIC)

cv.imshow("Nearest",tigerNear2)
cv.imshow("Bilinear",tigerBil2)
cv.imshow("Cubica", tigerCub2)
cv.waitKey(0)
cv.destroyAllWindows()

# o bilinear foi o melhor mesmo ficando bem embaçado, o nearest ficou todo pixelado e o cubico é como se misturasse ambos

