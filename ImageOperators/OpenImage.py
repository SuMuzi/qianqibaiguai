from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("C:\\Users\\Suxiansheng\\Desktop\\juzu.jpg")
#img.show()
plt.figure("juzuo")
plt.imshow(img)
plt.show()