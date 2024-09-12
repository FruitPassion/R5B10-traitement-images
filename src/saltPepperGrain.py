import skimage as ski
import random as rd
#proablement à supprimer
# def pepperSaltGrain (inputImagePath):
#     image = ski.io.imread(inputImagePath)
#     for i in range(0, len(image)):
#         for j in range(0, len(image[i])):
#             image[i][j] = pepperSaltGrainEachPixel(image[i][j])
    
def pepperSaltGrainEachPixel(pixel: int, rate: int)->int:
    salt, pepper = False
    # default rate value 1000 ->> 0.1% of the pixels will be affected
    if rd.randint(0, rate) <= 2:
        if  rd.randint(0, 1) == 0:
            pixel = 0 # salt
        else:
            pixel = 255 # pepper   
    return pixel