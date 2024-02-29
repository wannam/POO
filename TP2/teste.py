
from color import Color
import pickle

list_color = []
j = 0

for i in range(0,1):

    namecolor = input('Color: ')
    rgb = int(input('RGB: '))
    new_color = Color(namecolor, rgb)
    list_color.append(new_color)

    with open("colors_teste.pkl", "wb") as f:
        pickle.dump(list_color, f)

    with open("colors_teste.pkl", "rb") as f:
        list_color = pickle.load(f)
    j+= 1 
     
if j == 1:
    for cor in list_color:
        print(cor)
        print(f'color dict {new_color.__dict__}')
        print(f'\nclass dict{Color.__dict__}')

