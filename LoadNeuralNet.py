import pickle
import numpy as np
import os
import ImageLoader
from PIL import Image

path = "./SavedModels/"

print("Following are the list of Files: ")

files = os.listdir(path)
filecount = 0

for i in files:
    print(filecount+1, ")" , i , "\n")
    filecount+=1

print("Enter the number of the Model which you want to load")

num = int(input())

#print("You chose " , files[num-1] )

filehandler = open(path+files[num-1], 'rb')

nn = (pickle.load(filehandler))

training_data, validation_data, test_data = ImageLoader.load_data_wrapper()

for (x, y) in test_data:
    print(np.argmax(nn.feedforward(x)))
    new_im = Image.fromarray((x*255).reshape(28,28))
    new_im.resize((100,100)).show()
    #print(len(x))
    input("Press Enter to go next")
    new_im.close()
