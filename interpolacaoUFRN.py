import cv2 as cv

src = cv.imread("ufrn.png")

ufrnNear = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_NEAREST)
ufrnBil = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_LINEAR)
ufrnCub = cv.resize(src, dsize=None,fx=1/4,fy=1/4,interpolation= cv.INTER_CUBIC)

ufrnNear2 = cv.resize(ufrnNear, dsize=None,fx=4,fy=4,interpolation= cv.INTER_NEAREST)
ufrnBil2 = cv.resize(ufrnBil, dsize=None,fx=4,fy=4,interpolation= cv.INTER_LINEAR)
ufrnCub2 = cv.resize(ufrnCub, dsize=None,fx=4,fy=4,interpolation= cv.INTER_CUBIC)

cv.imshow("Nearest",ufrnNear2)
cv.imshow("Bilinear",ufrnBil2)
cv.imshow("Cubica", ufrnCub2)
cv.waitKey(0)
cv.destroyAllWindows()

# novamente o do vizinho mais próximo ficou todo pixelado
# o bilinear fica mais fácil de ler o texto abaixo da logo e a logo em si
# o cúbico parece aumentar a saturação de alguma forma, como se realssace a imagem,mas não ajuda a deixar mais légivel 

