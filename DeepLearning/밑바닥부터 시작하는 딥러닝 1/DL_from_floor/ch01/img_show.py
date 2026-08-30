import matplotlib.pyplot as plt
from matplotlib.image import imread

# 파일 위치를 맞추어서 경로 설정.
img = imread("../images/snow_man.jpg")

plt.imshow(img)
plt.show()