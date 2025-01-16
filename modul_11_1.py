from PIL import Image
import numpy as np
from numpy.random.mtrand import randint

im_1 = Image.open('картинка 1.jpg')
im_2 = Image.open('картинка 2.jpg')
print(im_1.format, im_1.mode, im_1.size)
print(im_2.format, im_1.mode, im_2.size)
im_1.thumbnail(size=(100, 100))
new_im_1 = im_1.convert('L')
new_im_1.save('иконка 1.jpeg', 'jpeg')
#new_im_1.show()

im_2.thumbnail(size=(100, 100))
new_im_2 = im_2.convert('L')
new_im_2.save('иконка 2.jpeg', 'jpeg')
#new_im_2.show()
"""открыл картинку, изменил размер и сделал ее чёрнобелой"""

x = randint(5)
a = np.array([x, x+1, x+2, x+3])
print(a)
b = np.array([a, a, a])
print(b)
print(b.sum())
# создаю думерный массив 5х5
data_5 = np.random.random((5, 5))
print(data_5)
print(data_5.max())
print(data_5.max(axis=0)) # max по столбцам матрицы
sum_1 = data_5 + [1, 2, 3, 4, 5]
print(sum_1)
