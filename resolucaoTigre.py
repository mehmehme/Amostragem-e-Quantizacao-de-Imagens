import cv2 as cv

src = cv.imread("tiger.jpg")

tiger2k = cv.resize(src, dsize=(2560,1440),fx=0,fy=0,interpolation= None)
tiger4k = cv.resize(src, dsize=(3840,2160),fx=0,fy=0,interpolation= None)

cv.imshow("2k",tiger2k)
cv.imshow("4k",tiger4k)
cv.waitKey(0)
cv.destroyAllWindows()

# 4k não cabe o tigre na tela, e parece ficar um pouco pixelada e borrada
# 2k dá para claramente ver o tigre perfeitamente,bastante detalhado, mas só a cabeça
