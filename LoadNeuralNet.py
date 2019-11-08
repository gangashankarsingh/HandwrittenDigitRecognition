import pickle as cPickle
import os

path = "./SavedModels"

print("Following are the list of Files:")

files = os.listdir(path)
filecount = 0

for i in files:
    print(filecount+1, ")" , i , "\n")
    filecount+=1